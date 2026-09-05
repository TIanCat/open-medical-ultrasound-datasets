#!/usr/bin/env python3
"""
Validate dataset YAML files for open-medical-ultrasound-datasets.

Usage
-----
python scripts/validate_datasets.py
python scripts/validate_datasets.py --root .
python scripts/validate_datasets.py --warnings-as-errors\npython scripts/validate_datasets.py --log logs/validation.log\npython scripts/validate_datasets.py --verbose

Dependency
----------
pip install pyyaml

Exit codes
----------
0: validation passed
1: one or more validation errors
2: missing dependency / invalid repository root

Design
------
- YAML files are the single source of truth.
- Unknown top-level fields are errors.
- Core fields are strict; descriptive detail fields are optional.
- Annotation subfields are extensible: unknown fields are warnings.
- Cross-file checks catch duplicate IDs, broken family references, and likely duplicates.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

try:
    import yaml
    from yaml.constructor import ConstructorError
except ImportError:
    print("ERROR: PyYAML is required. Install it with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)


# =============================================================================
# Dataset Schema v1
# =============================================================================

CATEGORY_CODES = {
    "00": "Breast",
    "01": "Thyroid",
    "02": "Obstetrics",
    "03": "Cardiac",
    "04": "Lung",
    "05": "Liver & Gallbladder",
    "06": "Musculoskeletal",
    "07": "Vessel",
    "08": "Brain",
    "09": "Kidney",
    "10": "Prostate",
    "11": "Nerve",
    "12": "Ovary",
    "13": "Animal",
    "19": "Multi-anatomy",
    "20": "Other",
}

REQUIRED_TOP_LEVEL = {
    "id", "name", "full_name", "release_year",
    "anatomy", "modality", "scale", "annotations", "tasks",
    "access", "paper", "data", "family", "verification",
}

OPTIONAL_TOP_LEVEL = {"aliases", "splits", "acquisition", "notes"}
ALLOWED_TOP_LEVEL = REQUIRED_TOP_LEVEL | OPTIONAL_TOP_LEVEL

MODALITY_TYPES = {
    "Ultrasound",
    "B-mode",
    "M-mode",
    "Color Doppler",
    "Doppler",
    "Power Doppler",
    "Spectral Doppler",
    "CEUS",
    "Elastography",
    "Micro-ultrasound",
    "Ultrafast ultrasound",
    "RF",
    "IQ",
    "Raw channel data",
    "MRI",
    "CT",
}

DIMENSIONS = {"2D", "3D", "4D", "mixed"}
TEMPORAL_TYPES = {"static", "cine", "sweep", "sequence", "mixed"}

REPRESENTATIONS = {
    "image",
    "video",
    "volume",
    "sequence",
    "RF",
    "IQ",
    "raw_channel",
    "mixed",
}

SCALE_UNITS = {
    "patient",
    "participant",
    "subject",
    "case",
    "study",
    "exam",
    "series",
    "image",
    "video",
    "frame",
    "volume",
    "scan",
    "acquisition",
    "pair",
    "lesion",
    "nodule",
    "record",
    "file",
    "biopsy_core",
}

TASKS = {
    "classification",
    "standard_plane_classification",
    "segmentation",
    "detection",
    "localization",
    "landmark_detection",
    "tracking",
    "measurement",
    "grading",
    "registration",
    "reconstruction",
    "enhancement",
    "beamforming",
    "signal_analysis",
    "pose_estimation",
    "report_generation",
    "pretraining",
    "quality_assessment",
    "reasoning",
}

ACCESS_LEVELS = {"open", "application", "controlled"}
FAMILY_TYPES = {"primary", "version", "subset", "derived", "aggregate"}
VERIFICATION_STATUS = {"verified", "partial"}
SPLIT_LABEL_STATUS = {"public", "withheld", "partial", "unknown"}

CLASSIFICATION_LABEL_TYPES = {
    "binary", "multiclass", "multilabel", "ordinal", "hierarchical"
}
SEGMENTATION_TYPES = {"binary", "multiclass", "instance", "surface"}

ANNOTATION_TYPES = {
    "classification",
    "segmentation",
    "detection",
    "localization",
    "landmarks",
    "measurements",
    "grading",
    "registration",
    "tracking",
    "quality",
    "reports",
    "reasoning",
}

ANNOTATION_ALLOWED_FIELDS = {
    "classification": {
        "unit", "label_type", "classes", "distribution", "label_sets",
        "class_system", "superclasses", "subgroups", "num_classes",
        "annotators", "format", "reference_standard", "note",
    },
    "segmentation": {
        "unit", "type", "targets", "format", "count",
        "annotators", "annotation_method", "note",
    },
    "detection": {
        "unit", "targets", "format", "count",
        "annotators", "annotation_method", "note",
    },
    "localization": {
        "unit", "targets", "format", "count",
        "annotators", "annotation_method", "note",
    },
    "landmarks": {
        "unit", "targets", "format", "count",
        "annotators", "annotation_method", "note",
    },
    "measurements": {
        "unit", "targets", "format", "count", "units",
        "annotators", "annotation_method", "note",
    },
    "grading": {
        "unit", "system", "categories", "distribution", "label_sets",
        "format", "annotators", "note",
    },
    "registration": {
        "unit", "modalities", "format", "count", "note",
    },
    "tracking": {
        "unit", "targets", "format", "count", "note",
    },
    "quality": {
        "unit", "targets", "categories", "format", "note",
    },
    "reports": {
        "unit", "type", "format", "note",
    },
    "reasoning": {
        "unit", "format", "components", "annotators", "note",
    },
}

TASK_TO_ANNOTATION = {
    "classification": "classification",
    "segmentation": "segmentation",
    "detection": "detection",
    "localization": "localization",
    "landmark_detection": "landmarks",
    "tracking": "tracking",
    "measurement": "measurements",
    "grading": "grading",
    "registration": "registration",
    "report_generation": "reports",
    "quality_assessment": "quality",
    "reasoning": "reasoning",
}


# =============================================================================
# YAML loader with duplicate-key detection
# =============================================================================

class UniqueKeyLoader(yaml.SafeLoader):
    pass


def _construct_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key: {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


# =============================================================================
# Reporting
# =============================================================================

@dataclass
class Issue:
    severity: str
    file: Path
    field: str
    message: str
    hint: str | None = None


class Reporter:
    def __init__(self):
        self.issues: list[Issue] = []

    def error(self, file, field, message, hint=None):
        self.issues.append(Issue("ERROR", file, field, message, hint))

    def warning(self, file, field, message, hint=None):
        self.issues.append(Issue("WARNING", file, field, message, hint))

    @property
    def errors(self):
        return [x for x in self.issues if x.severity == "ERROR"]

    @property
    def warnings(self):
        return [x for x in self.issues if x.severity == "WARNING"]

    def render_report(self, root: Path) -> str:
        lines = []

        if not self.issues:
            lines.append("PASS: all dataset YAML files passed validation.")
            return "\n".join(lines) + "\n"

        grouped = defaultdict(list)
        for issue in self.issues:
            grouped[issue.file].append(issue)

        for file in sorted(grouped, key=str):
            try:
                display = file.relative_to(root)
            except ValueError:
                display = file

            lines.append("")
            lines.append(str(display))

            for issue in grouped[file]:
                field = f" [{issue.field}]" if issue.field else ""
                lines.append(f"  {issue.severity}{field}: {issue.message}")
                if issue.hint:
                    lines.append(f"    Hint: {issue.hint}")

        lines.append("")
        lines.append(
            f"Summary: {len(self.errors)} error(s), "
            f"{len(self.warnings)} warning(s)."
        )
        return "\n".join(lines) + "\n"

    def print_report(self, root: Path):
        print(self.render_report(root), end="")


# =============================================================================
# Helpers
# =============================================================================

def is_string(value):
    return isinstance(value, str) and bool(value.strip())


def as_mapping(value, file, field, reporter):
    if not isinstance(value, dict):
        reporter.error(file, field, "must be a mapping/object.")
        return None
    return value


def as_list(value, file, field, reporter):
    if not isinstance(value, list):
        reporter.error(file, field, "must be a list.")
        return None
    return value


def string_list(value, file, field, reporter, allow_empty=True):
    items = as_list(value, file, field, reporter)
    if items is None:
        return None

    if not allow_empty and not items:
        reporter.error(file, field, "must contain at least one item.")

    valid = []
    for i, item in enumerate(items):
        if not is_string(item):
            reporter.error(file, f"{field}[{i}]", "must be a non-empty string.")
        else:
            valid.append(item.strip())

    if len(valid) != len(set(valid)):
        reporter.warning(file, field, "contains duplicate values.")

    return valid


def check_keys(
    mapping,
    *,
    allowed,
    required,
    file,
    field,
    reporter,
    unknown_as_warning=False,
):
    keys = set(mapping)

    for key in sorted(required - keys):
        child = f"{field}.{key}" if field else key
        reporter.error(file, child, "required field is missing.")

    for key in sorted(keys - allowed):
        child = f"{field}.{key}" if field else key
        fn = reporter.warning if unknown_as_warning else reporter.error
        fn(
            file,
            child,
            "field is not part of Dataset Schema v1.",
            "Remove it, move the information to a note field, "
            "or explicitly extend the schema if it is reusable.",
        )


def normalize_doi(value: str):
    value = value.strip().lower()
    value = re.sub(r"^https?://(dx\.)?doi\.org/", "", value)
    return value.rstrip("/")


def normalize_url(value: str):
    value = value.strip()
    try:
        p = urlsplit(value)
        return urlunsplit(
            (p.scheme.lower(), p.netloc.lower(), p.path.rstrip("/"), p.query, "")
        )
    except ValueError:
        return value.rstrip("/").lower()


def normalize_name(value: str):
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def is_url(value: str):
    try:
        p = urlsplit(value)
        return p.scheme in {"http", "https"} and bool(p.netloc)
    except ValueError:
        return False


# =============================================================================
# Per-file validation
# =============================================================================

def load_yaml(file: Path, reporter: Reporter):
    try:
        with file.open("r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        field = ""
        if mark is not None:
            field = f"line {mark.line + 1}, column {mark.column + 1}"
        reporter.error(file, field, f"invalid YAML: {exc}")
        return None
    except UnicodeDecodeError as exc:
        reporter.error(file, "", f"file is not UTF-8: {exc}")
        return None

    if not isinstance(data, dict):
        reporter.error(file, "", "YAML root must be a mapping/object.")
        return None
    return data


def validate_identity(data, file, reporter):
    dataset_id = data.get("id")

    if not isinstance(dataset_id, str) or not re.fullmatch(r"\d{4}", dataset_id):
        reporter.error(
            file,
            "id",
            f"must be a four-digit string; got {dataset_id!r}.",
            'Example: id: "1303"',
        )
        return

    if dataset_id != file.stem:
        reporter.error(
            file,
            "id",
            f'id "{dataset_id}" does not match filename "{file.name}".',
            f'Use id: "{file.stem}".',
        )

    code = dataset_id[:2]
    if code not in CATEGORY_CODES:
        reporter.error(
            file,
            "id",
            f'unknown category code "{code}".',
            f"Allowed: {', '.join(sorted(CATEGORY_CODES))}",
        )

    m = re.match(r"^(\d{2})_", file.parent.name)
    if not m:
        reporter.error(
            file,
            "",
            f'parent directory "{file.parent.name}" must start with NN_.',
        )
    elif m.group(1) != code:
        reporter.error(
            file,
            "id",
            f'ID category "{code}" does not match directory "{file.parent.name}".',
        )

    for key in ("name", "full_name"):
        if not is_string(data.get(key)):
            reporter.error(file, key, "must be a non-empty string.")

    if "aliases" in data:
        aliases = string_list(data["aliases"], file, "aliases", reporter)
        if aliases:
            canonical = {
                normalize_name(str(data.get("name", ""))),
                normalize_name(str(data.get("full_name", ""))),
            }
            for i, alias in enumerate(aliases):
                if normalize_name(alias) in canonical:
                    reporter.warning(
                        file,
                        f"aliases[{i}]",
                        "duplicates name or full_name.",
                        "Keep aliases only for genuine alternative names.",
                    )


def validate_release_year(data, file, reporter):
    value = data.get("release_year")
    if value is None:
        return

    if not isinstance(value, int) or isinstance(value, bool):
        reporter.error(file, "release_year", "must be an integer or null.")
        return

    year = date.today().year
    if not 1900 <= value <= year:
        reporter.error(
            file,
            "release_year",
            f"must be between 1900 and {year}, or null.",
        )


def validate_anatomy(data, file, reporter):
    block = as_mapping(data.get("anatomy"), file, "anatomy", reporter)
    if block is None:
        return

    check_keys(
        block,
        allowed={"primary", "target"},
        required={"primary"},
        file=file,
        field="anatomy",
        reporter=reporter,
    )

    if not is_string(block.get("primary")):
        reporter.error(file, "anatomy.primary", "must be a non-empty string.")

    if "target" in block:
        string_list(block.get("target"), file, "anatomy.target", reporter)


def validate_modality(data, file, reporter):
    block = as_mapping(data.get("modality"), file, "modality", reporter)
    if block is None:
        return

    required = {"type", "dimension", "temporal", "representation"}
    check_keys(
        block,
        allowed=required,
        required=required,
        file=file,
        field="modality",
        reporter=reporter,
    )

    values = string_list(
        block.get("type"),
        file,
        "modality.type",
        reporter,
        allow_empty=False,
    )
    if values:
        for i, value in enumerate(values):
            if value not in MODALITY_TYPES:
                reporter.error(
                    file,
                    f"modality.type[{i}]",
                    f'"{value}" is not allowed.',
                    f"Allowed: {', '.join(sorted(MODALITY_TYPES))}",
                )

    dimension = block.get("dimension")
    if dimension is not None and dimension not in DIMENSIONS:
        reporter.error(
            file,
            "modality.dimension",
            f"{dimension!r} is invalid.",
            f"Allowed: {', '.join(sorted(DIMENSIONS))}, or null when unknown",
        )

    temporal = block.get("temporal")
    if temporal is not None and temporal not in TEMPORAL_TYPES:
        reporter.error(
            file,
            "modality.temporal",
            f"{temporal!r} is invalid.",
            f"Allowed: {', '.join(sorted(TEMPORAL_TYPES))}, or null when unknown",
        )

    reps = string_list(
        block.get("representation"),
        file,
        "modality.representation",
        reporter,
        allow_empty=False,
    )
    if reps:
        for i, value in enumerate(reps):
            if value not in REPRESENTATIONS:
                reporter.error(
                    file,
                    f"modality.representation[{i}]",
                    f'"{value}" is not allowed.',
                    f"Allowed: {', '.join(sorted(REPRESENTATIONS))}",
                )


def validate_scale(data, file, reporter):
    items = as_list(data.get("scale"), file, "scale", reporter)
    if items is None:
        return

    if not items:
        reporter.error(file, "scale", "must contain at least one item.")
        return

    for i, item in enumerate(items):
        field = f"scale[{i}]"

        if not isinstance(item, dict):
            reporter.error(file, field, "must be a mapping/object.")
            continue

        check_keys(
            item,
            allowed={"unit", "count", "approximate", "note"},
            required={"unit", "count"},
            file=file,
            field=field,
            reporter=reporter,
        )

        if item.get("unit") not in SCALE_UNITS:
            reporter.error(
                file,
                f"{field}.unit",
                f"{item.get('unit')!r} is not an allowed unit.",
                f"Allowed: {', '.join(sorted(SCALE_UNITS))}",
            )

        count = item.get("count")
        if count is None:
            if not is_string(item.get("note")):
                reporter.error(
                    file,
                    f"{field}.count",
                    "may be null only when a non-empty note explains why the exact count is unavailable.",
                )
        elif not isinstance(count, int) or isinstance(count, bool) or count <= 0:
            reporter.error(file, f"{field}.count", "must be a positive integer or null with an explanatory note.")

        if "approximate" in item and not isinstance(item["approximate"], bool):
            reporter.error(file, f"{field}.approximate", "must be boolean.")

        if (
            "note" in item
            and item["note"] is not None
            and not isinstance(item["note"], str)
        ):
            reporter.error(file, f"{field}.note", "must be a string or null.")


def validate_annotations(data, file, reporter):
    anns = as_mapping(data.get("annotations"), file, "annotations", reporter)
    if anns is None:
        return

    for kind in sorted(set(anns) - ANNOTATION_TYPES):
        reporter.error(
            file,
            f"annotations.{kind}",
            "unknown annotation type.",
            f"Allowed: {', '.join(sorted(ANNOTATION_TYPES))}",
        )

    for kind, block in anns.items():
        if kind not in ANNOTATION_TYPES:
            continue

        field = f"annotations.{kind}"

        if not isinstance(block, dict):
            reporter.error(file, field, "must be a mapping/object.")
            continue

        check_keys(
            block,
            allowed=ANNOTATION_ALLOWED_FIELDS[kind],
            required=set(),
            file=file,
            field=field,
            reporter=reporter,
            unknown_as_warning=True,
        )

        if "num_classes" in block:
            reporter.error(
                file,
                f"{field}.num_classes",
                "num_classes is redundant and is not allowed.",
                "Use len(classes) in build scripts.",
            )

        for key in ("targets", "annotators", "modalities", "components", "categories"):
            if key in block and block[key] is not None:
                string_list(block[key], file, f"{field}.{key}", reporter)

        if "count" in block:
            count = block["count"]
            if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
                reporter.error(file, f"{field}.count", "must be a positive integer.")

        if kind == "classification":
            if "label_type" in block and block.get("label_type") not in CLASSIFICATION_LABEL_TYPES:
                reporter.error(
                    file,
                    f"{field}.label_type",
                    f"{block.get('label_type')!r} is invalid.",
                    f"Allowed: {', '.join(sorted(CLASSIFICATION_LABEL_TYPES))}",
                )

            if "classes" in block and block["classes"] is not None:
                string_list(
                    block["classes"],
                    file,
                    f"{field}.classes",
                    reporter,
                    allow_empty=False,
                )

            distribution = block.get("distribution")
            if distribution is not None and not isinstance(distribution, dict):
                reporter.error(
                    file,
                    f"{field}.distribution",
                    "must be a mapping/object.",
                )

        elif kind == "segmentation":
            if "type" in block and block.get("type") not in SEGMENTATION_TYPES:
                reporter.error(
                    file,
                    f"{field}.type",
                    f"{block.get('type')!r} is invalid.",
                    f"Allowed: {', '.join(sorted(SEGMENTATION_TYPES))}",
                )
            if "targets" in block and block["targets"] is not None:
                string_list(block["targets"], file, f"{field}.targets", reporter)

        elif kind in {"detection", "localization", "landmarks", "measurements", "tracking"}:
            if "targets" in block and block["targets"] is not None:
                string_list(block["targets"], file, f"{field}.targets", reporter)

        elif kind == "registration":
            if "modalities" in block and block["modalities"] is not None:
                string_list(block["modalities"], file, f"{field}.modalities", reporter)



def validate_tasks(data, file, reporter):
    tasks = string_list(
        data.get("tasks"),
        file,
        "tasks",
        reporter,
        allow_empty=False,
    )
    if tasks is None:
        return

    for i, task in enumerate(tasks):
        if task not in TASKS:
            reporter.error(
                file,
                f"tasks[{i}]",
                f'"{task}" is not allowed.',
                f"Allowed: {', '.join(sorted(TASKS))}",
            )

    anns = data.get("annotations")
    if not isinstance(anns, dict):
        return

    task_set = set(tasks)

    for task, ann in TASK_TO_ANNOTATION.items():
        has_task = task in task_set
        has_ann = ann in anns

        if has_task and not has_ann:
            reporter.warning(
                file,
                "tasks",
                f'task "{task}" exists but annotations.{ann} is absent.',
            )

        if has_ann and not has_task:
            reporter.warning(
                file,
                "tasks",
                f'annotations.{ann} exists but task "{task}" is absent.',
            )


def validate_splits(data, file, reporter):
    if "splits" not in data:
        return

    block = as_mapping(data["splits"], file, "splits", reporter)
    if block is None:
        return

    check_keys(
        block,
        allowed={"unit", "training", "validation", "test", "note"},
        required=set(),
        file=file,
        field="splits",
        reporter=reporter,
    )

    if "unit" in block and not is_string(block.get("unit")):
        reporter.error(file, "splits.unit", "must be a non-empty string.")
    if "note" in block and block.get("note") is not None and not isinstance(block.get("note"), str):
        reporter.error(file, "splits.note", "must be a string or null.")

    names = [x for x in ("training", "validation", "test") if x in block]
    if not names:
        reporter.error(
            file,
            "splits",
            "must define at least one of training/validation/test.",
        )

    for name in names:
        split = block[name]
        field = f"splits.{name}"

        if not isinstance(split, dict):
            reporter.error(file, field, "must be a mapping/object.")
            continue

        check_keys(
            split,
            allowed={"count", "labels", "distribution", "note"},
            required={"count"},
            file=file,
            field=field,
            reporter=reporter,
        )

        count = split.get("count")
        if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
            reporter.error(file, f"{field}.count", "must be a positive integer.")

        if "labels" in split and split["labels"] not in SPLIT_LABEL_STATUS:
            reporter.error(
                file,
                f"{field}.labels",
                f"{split['labels']!r} is invalid.",
                f"Allowed: {', '.join(sorted(SPLIT_LABEL_STATUS))}",
            )


def validate_access(data, file, reporter):
    block = as_mapping(data.get("access"), file, "access", reporter)
    if block is None:
        return

    allowed = {"level", "license", "requirements"}
    check_keys(
        block,
        allowed=allowed,
        required={"level"},
        file=file,
        field="access",
        reporter=reporter,
    )

    if block.get("level") not in ACCESS_LEVELS:
        reporter.error(
            file,
            "access.level",
            f"{block.get('level')!r} is invalid.",
            f"Allowed: {', '.join(sorted(ACCESS_LEVELS))}",
        )

    if block.get("license") is not None and not isinstance(block.get("license"), str):
        reporter.error(file, "access.license", "must be a string or null.")

    if "requirements" in block:
        string_list(block.get("requirements"), file, "access.requirements", reporter)


def validate_paper(data, file, reporter):
    paper = data.get("paper")
    if paper is None:
        return

    if not isinstance(paper, dict):
        reporter.error(file, "paper", "must be a mapping/object or null.")
        return

    allowed = {"title", "venue", "doi"}
    check_keys(
        paper,
        allowed=allowed,
        required={"title"},
        file=file,
        field="paper",
        reporter=reporter,
    )

    if not is_string(paper.get("title")):
        reporter.error(file, "paper.title", "must be a non-empty string.")

    for key in ("venue", "doi"):
        if paper.get(key) is not None and not isinstance(paper.get(key), str):
            reporter.error(file, f"paper.{key}", "must be a string or null.")


def validate_data(data, file, reporter):
    block = as_mapping(data.get("data"), file, "data", reporter)
    if block is None:
        return

    allowed = {"repository", "url", "doi", "version"}
    check_keys(
        block,
        allowed=allowed,
        required={"repository", "url"},
        file=file,
        field="data",
        reporter=reporter,
    )

    if not is_string(block.get("repository")):
        reporter.error(file, "data.repository", "must be a non-empty string.")

    url = block.get("url")
    if not is_string(url) or not is_url(url):
        reporter.error(file, "data.url", "must be a valid http(s) URL.")

    doi = block.get("doi")
    if doi is not None:
        if not isinstance(doi, str):
            reporter.error(file, "data.doi", "must be a string or null.")
        elif not normalize_doi(doi).startswith("10."):
            reporter.warning(file, "data.doi", f"{doi!r} does not look like a DOI.")

    version = block.get("version")
    if version is not None and not isinstance(version, (str, int, float)):
        reporter.error(file, "data.version", "must be string, number, or null.")


def validate_acquisition(data, file, reporter):
    if "acquisition" not in data:
        return

    block = as_mapping(data.get("acquisition"), file, "acquisition", reporter)
    if block is None:
        return

    allowed = {
        "countries",
        "institutions",
        "period",
        "scanners",
        "transducers",
        "frequencies",
        "note",
    }

    check_keys(
        block,
        allowed=allowed,
        required=set(),
        file=file,
        field="acquisition",
        reporter=reporter,
    )

    for key in ("countries", "institutions", "scanners", "transducers", "frequencies"):
        value = block.get(key)
        if value is not None:
            string_list(value, file, f"acquisition.{key}", reporter)

    for key in ("period", "note"):
        value = block.get(key)
        if value is not None and not isinstance(value, str):
            reporter.error(file, f"acquisition.{key}", "must be a string or null.")


def validate_family(data, file, reporter):
    block = as_mapping(data.get("family"), file, "family", reporter)
    if block is None:
        return

    allowed = {"type", "parent", "related"}
    check_keys(
        block,
        allowed=allowed,
        required={"type"},
        file=file,
        field="family",
        reporter=reporter,
    )

    family_type = block.get("type")
    if family_type not in FAMILY_TYPES:
        reporter.error(
            file,
            "family.type",
            f"{family_type!r} is invalid.",
            f"Allowed: {', '.join(sorted(FAMILY_TYPES))}",
        )

    parent = block.get("parent")
    if parent is not None and (
        not isinstance(parent, str) or not re.fullmatch(r"\d{4}", parent)
    ):
        reporter.error(
            file,
            "family.parent",
            "must be null or a four-digit atlas ID.",
            'Example: parent: "0401"',
        )

    related = None
    if "related" in block:
        related = string_list(block.get("related"), file, "family.related", reporter)
    if related is not None:
        for i, value in enumerate(related):
            if not re.fullmatch(r"\d{4}", value):
                reporter.error(
                    file,
                    f"family.related[{i}]",
                    f'"{value}" is not a four-digit atlas ID.',
                )

    if family_type == "primary" and parent is not None:
        reporter.error(file, "family.parent", "primary datasets must use parent: null.")

    if family_type in {"version", "subset", "derived"} and parent is None:
        reporter.error(
            file,
            "family.parent",
            f"{family_type} datasets must specify parent.",
        )

    dataset_id = data.get("id")
    if isinstance(dataset_id, str):
        if parent == dataset_id:
            reporter.error(file, "family.parent", "dataset cannot be its own parent.")
        if isinstance(related, list) and dataset_id in related:
            reporter.error(file, "family.related", "dataset cannot be related to itself.")


def validate_verification(data, file, reporter):
    block = as_mapping(data.get("verification"), file, "verification", reporter)
    if block is None:
        return

    required = {"status", "date", "sources"}
    check_keys(
        block,
        allowed=required,
        required=required,
        file=file,
        field="verification",
        reporter=reporter,
    )

    if block.get("status") not in VERIFICATION_STATUS:
        reporter.error(
            file,
            "verification.status",
            f"{block.get('status')!r} is invalid.",
            f"Allowed: {', '.join(sorted(VERIFICATION_STATUS))}",
        )

    value = block.get("date")
    if not isinstance(value, str):
        reporter.error(file, "verification.date", "must be YYYY-MM-DD string.")
    else:
        try:
            d = datetime.strptime(value, "%Y-%m-%d").date()
            if d > date.today():
                reporter.warning(file, "verification.date", "is in the future.")
        except ValueError:
            reporter.error(file, "verification.date", "must use YYYY-MM-DD format.")

    sources = string_list(
        block.get("sources"),
        file,
        "verification.sources",
        reporter,
        allow_empty=False,
    )
    if sources:
        for i, source in enumerate(sources):
            if not is_url(source):
                reporter.warning(
                    file,
                    f"verification.sources[{i}]",
                    f"{source!r} is not an http(s) URL.",
                )


def validate_one(file, reporter):
    data = load_yaml(file, reporter)
    if data is None:
        return None

    check_keys(
        data,
        allowed=ALLOWED_TOP_LEVEL,
        required=REQUIRED_TOP_LEVEL,
        file=file,
        field="",
        reporter=reporter,
    )

    validate_identity(data, file, reporter)
    validate_release_year(data, file, reporter)
    validate_anatomy(data, file, reporter)
    validate_modality(data, file, reporter)
    validate_scale(data, file, reporter)
    validate_annotations(data, file, reporter)
    validate_tasks(data, file, reporter)
    validate_splits(data, file, reporter)
    validate_access(data, file, reporter)
    validate_paper(data, file, reporter)
    validate_data(data, file, reporter)
    validate_acquisition(data, file, reporter)
    validate_family(data, file, reporter)
    validate_verification(data, file, reporter)

    if "notes" in data and data["notes"] is not None and not isinstance(data["notes"], str):
        reporter.error(file, "notes", "must be a string or null.")

    return data


# =============================================================================
# Cross-file checks
# =============================================================================

def check_cross_file(datasets, reporter):
    by_id = defaultdict(list)
    by_data_url = defaultdict(list)
    by_data_doi = defaultdict(list)
    by_paper_doi = defaultdict(list)
    by_name = defaultdict(list)

    id_to_file = {}

    for file, data in datasets:
        dataset_id = data.get("id")

        if isinstance(dataset_id, str) and re.fullmatch(r"\d{4}", dataset_id):
            by_id[dataset_id].append(file)
            id_to_file[dataset_id] = file

        data_block = data.get("data")
        if isinstance(data_block, dict):
            if is_string(data_block.get("url")):
                by_data_url[normalize_url(data_block["url"])].append(file)

            if is_string(data_block.get("doi")):
                by_data_doi[normalize_doi(data_block["doi"])].append(file)

        paper = data.get("paper")
        if isinstance(paper, dict) and is_string(paper.get("doi")):
            by_paper_doi[normalize_doi(paper["doi"])].append(file)

        names = []
        for key in ("name", "full_name"):
            if is_string(data.get(key)):
                names.append(data[key])

        if isinstance(data.get("aliases"), list):
            names.extend(x for x in data["aliases"] if is_string(x))

        for name in names:
            norm = normalize_name(name)
            if norm:
                by_name[norm].append(file)

    # Duplicate atlas IDs = ERROR
    for dataset_id, files in by_id.items():
        if len(set(files)) > 1:
            for file in files:
                reporter.error(
                    file,
                    "id",
                    f'duplicate atlas ID "{dataset_id}".',
                )

    # Shared source identifiers = WARNING
    for label, groups, field in (
        ("data URL", by_data_url, "data.url"),
        ("data DOI", by_data_doi, "data.doi"),
        ("paper DOI", by_paper_doi, "paper.doi"),
    ):
        for _, files in groups.items():
            unique = sorted(set(files), key=str)
            if len(unique) > 1:
                ids = ", ".join(x.stem for x in unique)
                for file in unique:
                    reporter.warning(
                        file,
                        field,
                        f"{label} is shared by atlas IDs: {ids}.",
                        "Verify family relationships and possible duplication.",
                    )

    # Same normalized name = WARNING
    for _, files in by_name.items():
        unique = sorted(set(files), key=str)
        if len(unique) > 1:
            ids = ", ".join(x.stem for x in unique)
            for file in unique:
                reporter.warning(
                    file,
                    "name/aliases",
                    f"normalized dataset name overlaps atlas IDs: {ids}.",
                    "Verify that these are not the same resource under different names.",
                )

    # Family references + parent cycles
    parent_map = {}

    for file, data in datasets:
        dataset_id = data.get("id")
        family = data.get("family")

        if not isinstance(dataset_id, str) or not isinstance(family, dict):
            continue

        parent = family.get("parent")
        if isinstance(parent, str) and re.fullmatch(r"\d{4}", parent):
            if parent not in id_to_file:
                reporter.error(
                    file,
                    "family.parent",
                    f'parent "{parent}" does not exist.',
                )
            else:
                parent_map[dataset_id] = parent

        related = family.get("related")
        if isinstance(related, list):
            for i, rel in enumerate(related):
                if isinstance(rel, str) and re.fullmatch(r"\d{4}", rel):
                    if rel not in id_to_file:
                        reporter.error(
                            file,
                            f"family.related[{i}]",
                            f'related ID "{rel}" does not exist.',
                        )

    for start in parent_map:
        seen = set()
        cur = start

        while cur in parent_map:
            if cur in seen:
                reporter.error(
                    id_to_file[start],
                    "family.parent",
                    f"family parent cycle detected involving {cur}.",
                )
                break

            seen.add(cur)
            cur = parent_map[cur]


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Validate dataset YAML files against Dataset Schema v1."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Repository root. Default: current directory.",
    )
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Return exit code 1 when warnings exist.",
    )
    parser.add_argument(
        "--log",
        type=Path,
        default=Path("validation_report.log"),
        help=(
            "Write the complete validation report to this file. "
            "Default: validation_report.log in the repository root."
        ),
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Also print the complete validation report to the console. By default, only a summary is printed.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    dataset_root = root / "datasets"

    if not dataset_root.is_dir():
        print(f"ERROR: {dataset_root} does not exist.", file=sys.stderr)
        return 2

    files = sorted(dataset_root.glob("*/*.yaml"))

    if not files:
        print("ERROR: no dataset YAML files found.", file=sys.stderr)
        return 2

    reporter = Reporter()
    datasets = []

    for file in files:
        data = validate_one(file, reporter)
        if data is not None:
            datasets.append((file, data))

    check_cross_file(datasets, reporter)

    report_text = reporter.render_report(root)

    # Write the complete log FIRST. This guarantees that the report is preserved
    # even when a terminal/IDE truncates or interrupts very long stdout output.
    log_path = args.log
    if not log_path.is_absolute():
        log_path = root / log_path

    log_path.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    log_header = (
        "Dataset validation report\n"
        f"Generated: {timestamp}\n"
        f"Repository: {root}\n"
        f"Checked YAML files: {len(files)}\n"
        + "=" * 80
        + "\n"
    )
    log_footer = (
        "=" * 80
        + "\n"
        f"Errors: {len(reporter.errors)}\n"
        f"Warnings: {len(reporter.warnings)}\n"
    )

    try:
        log_path.write_text(
            log_header + report_text + log_footer,
            encoding="utf-8",
        )
    except OSError as exc:
        print(f"ERROR: failed to write validation log: {log_path}", file=sys.stderr)
        print(f"       {exc}", file=sys.stderr)
        return 2

    try:
        display_log = log_path.relative_to(root)
    except ValueError:
        display_log = log_path

    # Keep the console compact by default.
    if args.verbose:
        print(report_text, end="")

    print(f"Checked {len(files)} YAML file(s).")
    print(f"Errors: {len(reporter.errors)}")
    print(f"Warnings: {len(reporter.warnings)}")
    print(f"Full report written to: {display_log}")

    if reporter.errors:
        return 1

    if args.warnings_as_errors and reporter.warnings:
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
