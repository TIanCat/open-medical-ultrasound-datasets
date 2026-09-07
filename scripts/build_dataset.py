#!/usr/bin/env python3
"""
Build datasets.csv from datasets/**/*.yaml.

YAML files are the single source of truth. This script validates the repository
first and refuses to build when validation fails.

Usage
-----
python scripts/build_dataset.py
python scripts/build_dataset.py --root .
python scripts/build_dataset.py --strict
python scripts/build_dataset.py --check
python scripts/build_dataset.py --output datasets.csv

Dependency
----------
pip install pyyaml

Exit codes
----------
0: build/check succeeded
1: validation failed, or --check found a stale/missing CSV
2: invalid repository/build configuration or I/O failure
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install it with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)


CATEGORY_NAMES = {
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

FIELDNAMES = [
    "id",
    "name",
    "full_name",
    "aliases",
    "release_year",
    "category_code",
    "category",
    "anatomy_primary",
    "anatomy_target",
    "modality_type",
    "dimension",
    "temporal",
    "representation",
    "scale",
    "annotation_types",
    "tasks",
    "split_summary",
    "access_level",
    "license",
    "paper_title",
    "paper_venue",
    "paper_doi",
    "data_repository",
    "data_url",
    "data_doi",
    "data_version",
    "family_type",
    "family_parent",
    "family_related",
    "verification_status",
    "verification_date",
    "notes",
]


def collapse_text(value: Any) -> str:
    """Convert a scalar to one stable, single-line CSV cell."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return re.sub(r"\s+", " ", str(value)).strip()


def join_list(value: Any) -> str:
    """Serialize a list as a stable human-readable cell."""
    if value is None:
        return ""
    if not isinstance(value, list):
        return collapse_text(value)
    return " | ".join(collapse_text(x) for x in value if x is not None)


def format_count(value: Any, approximate: bool = False) -> str:
    if value is None:
        text = "unknown"
    else:
        text = collapse_text(value)
    return f"~{text}" if approximate and value is not None else text


def serialize_scale(scale: Any) -> str:
    """
    Example:
        patient=290 | image=25005
        frame=~200000 | file=23
    """
    if not isinstance(scale, list):
        return ""

    parts: list[str] = []
    for item in scale:
        if not isinstance(item, dict):
            continue
        unit = collapse_text(item.get("unit"))
        if not unit:
            continue
        count = format_count(item.get("count"), bool(item.get("approximate")))
        parts.append(f"{unit}={count}")
    return " | ".join(parts)


def serialize_splits(splits: Any) -> str:
    """
    Example:
        image: training=5635 [public] | test=5508 [withheld]
    """
    if not isinstance(splits, dict):
        return ""

    unit = collapse_text(splits.get("unit"))
    parts: list[str] = []

    for name, block in splits.items():
        if name in {"unit", "note"} or not isinstance(block, dict):
            continue

        count = format_count(block.get("count"), bool(block.get("approximate")))
        labels = collapse_text(block.get("labels"))

        part = f"{name}={count}"
        if labels:
            part += f" [{labels}]"
        parts.append(part)

    if not parts:
        return ""

    prefix = f"{unit}: " if unit else ""
    return prefix + " | ".join(parts)


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except (OSError, yaml.YAMLError) as exc:
        raise RuntimeError(f"failed to read {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise RuntimeError(f"{path} does not contain a YAML mapping/object.")
    return data


def category_from_file(path: Path, data: dict[str, Any]) -> tuple[str, str]:
    dataset_id = collapse_text(data.get("id"))
    if not re.fullmatch(r"\d{4}", dataset_id):
        raise RuntimeError(f"{path}: invalid id {dataset_id!r}.")

    code = dataset_id[:2]
    if code not in CATEGORY_NAMES:
        raise RuntimeError(f"{path}: unknown category code {code!r}.")

    # Validation should already guarantee this. Keep the build defensive so a
    # CSV can never silently assign an entry to the wrong category.
    parent_name = path.parent.name
    if not parent_name.startswith(code):
        raise RuntimeError(
            f"{path}: directory {parent_name!r} does not match ID prefix {code!r}."
        )

    return code, CATEGORY_NAMES[code]


def dataset_to_row(path: Path, data: dict[str, Any]) -> dict[str, str]:
    code, category = category_from_file(path, data)

    anatomy = data.get("anatomy") if isinstance(data.get("anatomy"), dict) else {}
    modality = data.get("modality") if isinstance(data.get("modality"), dict) else {}
    annotations = (
        data.get("annotations") if isinstance(data.get("annotations"), dict) else {}
    )
    access = data.get("access") if isinstance(data.get("access"), dict) else {}
    paper = data.get("paper") if isinstance(data.get("paper"), dict) else {}
    data_block = data.get("data") if isinstance(data.get("data"), dict) else {}
    family = data.get("family") if isinstance(data.get("family"), dict) else {}
    verification = (
        data.get("verification")
        if isinstance(data.get("verification"), dict)
        else {}
    )

    row = {
        "id": collapse_text(data.get("id")),
        "name": collapse_text(data.get("name")),
        "full_name": collapse_text(data.get("full_name")),
        "aliases": join_list(data.get("aliases")),
        "release_year": collapse_text(data.get("release_year")),
        "category_code": code,
        "category": category,
        "anatomy_primary": collapse_text(anatomy.get("primary")),
        "anatomy_target": join_list(anatomy.get("target")),
        "modality_type": join_list(modality.get("type")),
        "dimension": collapse_text(modality.get("dimension")),
        "temporal": collapse_text(modality.get("temporal")),
        "representation": join_list(modality.get("representation")),
        "scale": serialize_scale(data.get("scale")),
        "annotation_types": " | ".join(annotations.keys()),
        "tasks": join_list(data.get("tasks")),
        "split_summary": serialize_splits(data.get("splits")),
        "access_level": collapse_text(access.get("level")),
        "license": collapse_text(access.get("license")),
        "paper_title": collapse_text(paper.get("title")),
        "paper_venue": collapse_text(paper.get("venue")),
        "paper_doi": collapse_text(paper.get("doi")),
        "data_repository": collapse_text(data_block.get("repository")),
        "data_url": collapse_text(data_block.get("url")),
        "data_doi": collapse_text(data_block.get("doi")),
        "data_version": collapse_text(data_block.get("version")),
        "family_type": collapse_text(family.get("type")),
        "family_parent": collapse_text(family.get("parent")),
        "family_related": join_list(family.get("related")),
        "verification_status": collapse_text(verification.get("status")),
        "verification_date": collapse_text(verification.get("date")),
        "notes": collapse_text(data.get("notes")),
    }

    return row


def render_csv(rows: list[dict[str, str]]) -> str:
    # newline="" plus an explicit "\n" lineterminator gives reproducible output
    # across Windows/macOS/Linux.
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        buffer,
        fieldnames=FIELDNAMES,
        extrasaction="raise",
        lineterminator="\n",
        quoting=csv.QUOTE_MINIMAL,
    )
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def run_validator(
    root: Path,
    strict: bool,
    validation_log: Path,
    verbose: bool,
) -> int:
    validator = root / "scripts" / "validate_yamls.py"
    if not validator.is_file():
        print(f"ERROR: validator not found: {validator}", file=sys.stderr)
        return 2

    cmd = [
        sys.executable,
        str(validator),
        "--root",
        str(root),
        "--log",
        str(validation_log),
    ]
    if strict:
        cmd.append("--warnings-as-errors")
    if verbose:
        cmd.append("--verbose")

    print("Validating dataset YAML files...", flush=True)
    try:
        completed = subprocess.run(cmd, cwd=root)
    except OSError as exc:
        print(f"ERROR: failed to run validator: {exc}", file=sys.stderr)
        return 2

    if completed.returncode != 0:
        if strict:
            print(
                "\nERROR: validation failed (strict mode: warnings also block the build).",
                file=sys.stderr,
            )
        else:
            print(
                "\nERROR: validation failed. datasets.csv was not generated.",
                file=sys.stderr,
            )
        return completed.returncode

    print()
    return 0


def resolve_under_root(root: Path, path: Path) -> Path:
    return path if path.is_absolute() else root / path


def print_summary(rows: list[dict[str, str]], output: Path, check_mode: bool) -> None:
    category_counts = Counter(row["category"] for row in rows)
    family_counts = Counter(row["family_type"] for row in rows)

    action = "Checked" if check_mode else "Generated"
    print(f"{action} {output}")
    print(f"Rows: {len(rows)}")

    print("\nCategories:")
    for code, name in CATEGORY_NAMES.items():
        count = category_counts.get(name, 0)
        if count:
            print(f"  {name:<22} {count:>3}")

    print("\nFamily types:")
    for family_type in ("primary", "version", "subset", "derived", "aggregate"):
        count = family_counts.get(family_type, 0)
        if count:
            print(f"  {family_type:<22} {count:>3}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate dataset YAML files and build datasets.csv."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=(
            "Repository root. Default: inferred from this script "
            "(parent of scripts/)."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("datasets.csv"),
        help="Output CSV path, relative to repository root by default.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat validation warnings as errors and refuse to build.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help=(
            "Do not write the CSV. Exit 1 if the existing output is missing "
            "or differs from the YAML-derived CSV. Intended for CI."
        ),
    )
    parser.add_argument(
        "--validation-log",
        type=Path,
        default=Path("validation_report.log"),
        help="Validation log path passed to scripts/validate_yamls.py.",
    )
    parser.add_argument(
        "--verbose-validation",
        action="store_true",
        help="Print the complete validation report to the console.",
    )
    args = parser.parse_args()

    inferred_root = Path(__file__).resolve().parents[1]
    root = (args.root or inferred_root).resolve()
    dataset_root = root / "datasets"

    if not dataset_root.is_dir():
        print(f"ERROR: dataset directory not found: {dataset_root}", file=sys.stderr)
        return 2

    validation_log = resolve_under_root(root, args.validation_log)
    validation_code = run_validator(
        root=root,
        strict=args.strict,
        validation_log=validation_log,
        verbose=args.verbose_validation,
    )
    if validation_code != 0:
        return validation_code if validation_code in {1, 2} else 2

    yaml_files = sorted(dataset_root.glob("*/*.yaml"))
    if not yaml_files:
        print("ERROR: no dataset YAML files found.", file=sys.stderr)
        return 2

    try:
        loaded = [(path, load_yaml(path)) for path in yaml_files]
        loaded.sort(key=lambda item: int(collapse_text(item[1].get("id"))))
        rows = [dataset_to_row(path, data) for path, data in loaded]
        csv_text = render_csv(rows)
    except (RuntimeError, ValueError, TypeError) as exc:
        print(f"ERROR: build failed: {exc}", file=sys.stderr)
        return 2

    output = resolve_under_root(root, args.output)

    if args.check:
        if not output.is_file():
            print(
                f"ERROR: {output} does not exist. Run build_dataset.py first.",
                file=sys.stderr,
            )
            return 1

        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"ERROR: failed to read {output}: {exc}", file=sys.stderr)
            return 2

        if current != csv_text:
            print(
                f"ERROR: {output} is stale. Re-run scripts/build_dataset.py.",
                file=sys.stderr,
            )
            return 1

        print_summary(rows, output, check_mode=True)
        print("\nCSV is up to date.")
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_name(output.name + ".tmp")

    try:
        with temp.open("w", encoding="utf-8", newline="") as f:
            f.write(csv_text)
        temp.replace(output)
    except OSError as exc:
        try:
            temp.unlink(missing_ok=True)
        except OSError:
            pass
        print(f"ERROR: failed to write {output}: {exc}", file=sys.stderr)
        return 2

    print_summary(rows, output, check_mode=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
