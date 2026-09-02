# Methodology

This repository uses a structured, multi-stage search and verification process to identify publicly accessible medical ultrasound imaging datasets.

The objective is not only to discover datasets, but also to verify their provenance, access status, associated publications, annotations, and relationships with other datasets.

## 1. Search Strategy

Dataset discovery is performed using multiple complementary sources rather than relying on a single review or repository.

### 1.1 Systematic reviews and dataset surveys

Published reviews of public ultrasound datasets are used as seed sources.

A major starting point is the systematic review:

> *On the public dissemination and open sourcing of ultrasound resources, datasets and deep learning models*, npj Digital Medicine, 2025.

Datasets identified in reviews are treated as **candidate records** and are subsequently re-verified using their original sources.

Information from a review is not automatically treated as authoritative when more recent or primary information is available.

### 1.2 Ultrasound-specific dataset directories

Specialized directories are searched to identify additional datasets and updated access information.

An important resource is the NIDUS/RadOSS open-access ultrasound dataset directory:

> https://ultrasound-open-access.nidusai.ca/

Directory entries are cross-checked against original publications and dataset repositories whenever possible.

### 1.3 General-purpose data repositories

Major scientific data repositories are searched using combinations of ultrasound-related keywords and anatomical terms.

Repositories include:

* Zenodo
* Mendeley Data
* Figshare
* Dryad
* OSF
* Harvard Dataverse
* PhysioNet
* The Cancer Imaging Archive (TCIA)
* Grand Challenge
* Kaggle
* IEEE DataPort
* institutional repositories

Typical search terms include:

* `ultrasound dataset`
* `ultrasonography dataset`
* `sonography dataset`
* `ultrasound database`
* `ultrasound benchmark`

### 1.4 Anatomy-based searches

Generic searches for "ultrasound dataset" may miss datasets whose titles only mention a disease, organ, or task.

Therefore, searches are also performed by anatomy or clinical target.

Examples include:

* fetal ultrasound dataset
* obstetric ultrasound dataset
* echocardiography dataset
* breast ultrasound dataset
* thyroid ultrasound dataset
* liver ultrasound dataset
* kidney ultrasound dataset
* lung ultrasound dataset
* prostate ultrasound dataset
* carotid ultrasound dataset
* musculoskeletal ultrasound dataset
* nerve ultrasound dataset
* brain ultrasound dataset
* ovarian ultrasound dataset
* endoscopic ultrasound dataset

### 1.5 Ultrasound modality-based searches

Additional searches are performed by acquisition modality and signal type.

Examples include:

* B-mode ultrasound dataset
* Doppler ultrasound dataset
* CEUS dataset
* ultrasound elastography dataset
* 3D ultrasound dataset
* 4D ultrasound dataset
* ultrasound video dataset
* ultrasound RF dataset
* ultrasound IQ dataset
* raw ultrasound dataset
* ultrafast ultrasound dataset
* ultrasound beamforming dataset

### 1.6 Literature searches

Dataset papers and papers describing newly released datasets are searched in:

* PubMed
* Google Scholar
* Web of Science
* Scopus
* Scientific Data
* Data in Brief
* Medical Image Analysis
* IEEE Transactions on Medical Imaging
* MICCAI proceedings
* relevant biomedical engineering and imaging journals

Backward and forward citation searches are used when useful.

---

## 2. Candidate Dataset Identification

Every potentially relevant resource is first treated as a candidate.

At this stage, we record:

* dataset name;
* possible official URL;
* anatomical target;
* approximate size;
* associated paper if available;
* source from which the dataset was discovered.

A candidate is promoted to the verified master dataset list only after sufficient evidence is available to establish that it represents an accessible medical ultrasound dataset.

Resources that cannot yet be fully verified are retained in the candidate list rather than discarded.

---

## 3. Primary-Source Verification

Whenever possible, dataset metadata are verified from two independent evidence chains.

### 3.1 Dataset evidence

Preferred sources are:

1. official dataset repository;
2. original project website;
3. institutional repository;
4. challenge website;
5. official GitHub repository maintained by the dataset authors.

Examples include:

* Zenodo
* Mendeley Data
* Figshare
* TCIA
* PhysioNet
* Grand Challenge
* institutional data repositories

Third-party mirrors are avoided when an original source is available.

### 3.2 Publication evidence

Publication metadata are verified separately using:

1. publisher webpage;
2. PubMed;
3. Crossref or DOI resolver;
4. conference proceedings;
5. the original manuscript.

The following information is checked:

* paper title;
* journal or conference;
* publication year;
* paper DOI.

---

## 4. Paper DOI and Dataset DOI

A strict distinction is maintained between a **publication DOI** and a **dataset DOI**.

For example:

```text
Paper DOI:
10.xxxx/xxxxx

Dataset DOI:
10.5281/zenodo.xxxxxxx
```

The paper DOI field contains only the DOI of the corresponding journal or conference publication.

Repository identifiers such as:

* Zenodo DOI;
* Figshare DOI;
* Mendeley Data DOI;
* TCIA DOI;
* Dataverse DOI

are stored separately as dataset identifiers.

A dataset repository DOI must never be used as a substitute for the publication DOI.

If no dedicated peer-reviewed publication can be identified, the publication field is explicitly marked as:

> No dedicated dataset paper

rather than assigning an unrelated downstream paper.

---

## 5. Dataset Size Verification

Dataset size is recorded using the unit reported by the original source.

Possible units include:

* patients;
* cases;
* studies;
* images;
* videos;
* frames;
* volumes;
* acquisitions;
* RF sequences.

When multiple values are available, priority is generally given to:

1. the latest official dataset release;
2. the official repository;
3. the original dataset paper.

If different versions report different sizes, the difference is documented rather than forcing them into a single value.

---

## 6. Annotation and Task Verification

Dataset annotations are described as specifically as possible.

### Classification

For classification datasets, we attempt to record:

* number of classes;
* class names;
* number of samples per class when available.

Example:

```text
3 classes:
- Normal
- Benign
- Malignant
```

### Segmentation

For segmentation datasets, we record the segmentation target.

Example:

```text
Segmentation targets:
- left ventricular cavity
- myocardium
- left atrium
```

rather than simply recording:

```text
Task: segmentation
```

### Detection

For detection datasets, we record:

* target lesion or structure;
* bounding-box or localization annotation when known.

### Measurement

For measurement datasets, we specify the target variable, such as:

* fetal head circumference;
* abdominal circumference;
* ejection fraction;
* intima-media thickness.

### Registration and Reconstruction

For registration datasets, we record:

* modalities being registered;
* reference landmarks or transformations when available.

For reconstruction datasets, we record:

* raw data or frame inputs;
* tracking or pose information;
* reconstruction target.

---

## 7. Access Classification

Dataset access is normalized into three mutually exclusive categories.

### `open`

The dataset can be directly downloaded or accessed without an approval process.

### `application`

The user must complete one or more steps such as:

* registration;
* signing a data-use agreement;
* institutional application;
* request to the dataset owner.

### `controlled`

Access requires formal credentialing, ethical approval, institutional authorization, or controlled-access procedures.

These categories describe **access**, not the legal license.

A dataset may be publicly downloadable while still restricting commercial redistribution.

---

## 8. Dataset Family Deduplication

One of the main challenges in cataloging public datasets is that a single data source may appear under multiple names.

Potential relationships include:

```text
Primary dataset
    ├── new version
    ├── subset
    ├── challenge release
    ├── curated benchmark
    └── derived dataset
```

Each resource is therefore evaluated for provenance.

Relationship types include:

* `primary`
* `version`
* `subset`
* `derived`
* `aggregate`

Only independent `primary` datasets are counted in the headline dataset total.

For example, if Dataset B is constructed entirely from Dataset A, both may be documented, but only Dataset A is counted as an independent acquisition source.

---

## 9. Multimodal Medical Datasets

Some medical datasets contain ultrasound together with CT, MRI, mammography, pathology, clinical variables, or other modalities.

These resources are evaluated according to the role of ultrasound.

If ultrasound is a major component of the resource, the dataset may be included in the main atlas.

If ultrasound is only an incidental component of a large multimodal cohort, the resource is listed separately as a multimodal dataset containing ultrasound.

This prevents large oncology repositories from artificially inflating the number of dedicated ultrasound datasets.

---

## 10. Exclusion Review

Resources are excluded from the primary atlas when they:

* are not medical ultrasound imaging datasets;
* contain no accessible ultrasound data;
* only provide source code or trained models;
* are duplicate mirrors of another dataset;
* are derived entirely from an existing dataset;
* are non-medical applications of ultrasound.

Excluded and merged records are retained whenever useful so that the decision remains transparent and reproducible.

---

## 11. Handling Uncertainty

We avoid filling missing information by inference when the original source is ambiguous.

When information cannot be reliably verified, we prefer statements such as:

* `Not specified by the original source`
* `No dedicated dataset paper identified`
* `License not explicitly stated`
* `Version-dependent`
* `Candidate — further verification required`

rather than assigning an unsupported value.

Candidate resources remain visible in the repository so that they can be revisited or corrected through future updates.

---

## 12. Update Process

The atlas is intended to be continuously updated.

New datasets may be identified through:

* newly published data papers;
* newly released repositories;
* challenge datasets;
* community Issues or Pull Requests;
* periodic systematic searches.

Before a new dataset is added to the verified master list, the following items should be checked:

* medical ultrasound scope;
* official data source;
* access status;
* anatomical target;
* data type;
* dataset size;
* annotations;
* supported tasks;
* corresponding publication;
* publication venue;
* publication DOI;
* relationship to existing dataset families.

Corrections to existing records follow the same verification process.

---

## 13. Search Cutoff and Versioning

Each release of the repository should report a search cutoff date.

For example:

```text
Search cutoff: 2026-09-02
```

Major updates should be released using repository versions such as:

```text
v1.0
v1.1
v2.0
```

The changelog should document:

* newly added datasets;
* removed datasets;
* merged dataset families;
* corrected links;
* corrected paper metadata;
* changes to inclusion criteria.

This makes each release reproducible even as the online atlas continues to evolve.
