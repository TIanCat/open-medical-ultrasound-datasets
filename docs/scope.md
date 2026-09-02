# Scope

This repository catalogs **publicly accessible medical ultrasound imaging datasets** for research in medical imaging, computer vision, machine learning, and related biomedical applications.

The goal is to provide a curated and continuously updated index of ultrasound datasets while maintaining a clear and reproducible definition of what is considered a medical ultrasound dataset.

## Inclusion Criteria

A dataset is eligible for inclusion if it satisfies all of the following criteria:

1. **Contains ultrasound imaging data**

   Eligible ultrasound data types include, but are not limited to:

   * 2D B-mode ultrasound
   * Ultrasound video or cine loops
   * Doppler ultrasound
   * Contrast-enhanced ultrasound (CEUS)
   * Ultrasound elastography
   * 3D or 4D ultrasound
   * Ultrafast ultrasound
   * Radio-frequency (RF) data
   * In-phase/quadrature (IQ) data
   * Raw channel data
   * Ultrasound data for beamforming or image reconstruction

2. **Has a medical or biomedical imaging purpose**

   The dataset should support at least one medical imaging or biomedical ultrasound application, such as:

   * Disease diagnosis or classification
   * Anatomical structure recognition
   * Standard-plane or view recognition
   * Lesion detection or localization
   * Semantic or instance segmentation
   * Biometric measurement
   * Functional measurement
   * Disease grading or staging
   * Image registration
   * 2D-to-3D or 3D reconstruction
   * Ultrasound beamforming
   * Image enhancement
   * Treatment guidance
   * Interventional navigation
   * Robotic ultrasound
   * Ultrasound report generation
   * Multimodal medical imaging
   * Foundation-model pretraining

3. **Uses medically relevant subjects or imaging targets**

   The dataset may contain ultrasound acquired from:

   * Humans
   * Animals used in biomedical research
   * Medical or anatomical phantoms

   Animal and phantom datasets are included when their primary purpose is medical ultrasound research, such as imaging reconstruction, segmentation, localization, elastography, or intervention.

4. **Is publicly accessible in some form**

   Public accessibility does not necessarily mean that the dataset can be downloaded without restrictions.

   We distinguish three access levels:

   * `open`: directly downloadable or accessible from a public repository
   * `application`: registration, data-use agreement, institutional approval, or application is required
   * `controlled`: access is restricted and requires credentialing, ethical approval, or other controlled-access procedures

## Exclusion Criteria

The following resources are outside the scope of this repository.

### Non-medical ultrasound

Examples include:

* Industrial ultrasound
* Non-destructive testing
* Materials inspection
* Sonar
* Acoustic sensing unrelated to medicine
* Structural engineering ultrasound

### Ultrasound used primarily for non-medical purposes

Datasets are excluded when ultrasound is merely the sensing technology but the primary research objective is not medical imaging.

Examples include:

* Articulatory ultrasound for speech recognition
* Tongue ultrasound for phonetics or pronunciation analysis
* Human-computer interaction using ultrasound sensing

For example, an ultrasound dataset synchronized with speech audio for analyzing tongue motion would not be included unless the primary objective is medical diagnosis, rehabilitation, or clinical assessment.

### Resources without usable ultrasound data

A paper, benchmark, or project is not included as a dataset if:

* no ultrasound data are publicly available;
* only trained models or source code are released;
* only example images are shown;
* the data source cannot be identified or accessed;
* the resource only redistributes metadata without the underlying ultrasound data.

## Primary Datasets and Dataset Families

A major goal of this repository is to avoid double counting.

A single ultrasound acquisition source may later appear as:

* a new version;
* a subset;
* a challenge dataset;
* a curated benchmark;
* a derived dataset;
* a multimodal extension.

Each resource is assigned a relationship type:

* `primary`: an independently acquired dataset or dataset family
* `version`: a later release of the same dataset
* `subset`: a subset of an existing dataset
* `derived`: a dataset constructed from an existing dataset
* `aggregate`: a benchmark combining multiple existing datasets

Only `primary` datasets are counted when reporting the number of independent medical ultrasound datasets.

Derived datasets, subsets, versions, and aggregates are retained in the repository when useful, but their relationship to the original dataset is explicitly documented.

## Multimodal Datasets

Datasets containing ultrasound together with other medical modalities, such as MRI, CT, mammography, pathology, or clinical data, are eligible when ultrasound represents a substantial component of the resource.

However, large multimodal cancer cohorts in which ultrasound is only a minor or incidental modality may be listed separately rather than counted as primary ultrasound datasets.

## Dataset Unit

Dataset size may be reported using different units depending on the source, including:

* patients;
* studies;
* examinations;
* images;
* videos;
* frames;
* volumes;
* acquisitions;
* RF/IQ sequences.

We preserve the unit reported by the original source whenever possible.

Dataset sizes should therefore **not be summed directly across datasets without accounting for differences in units**.

## Annotation and Task Description

We aim to describe annotations at a level that is useful for machine-learning research.

For classification datasets, we record:

* the number of classes;
* class names;
* class distribution when available.

For segmentation datasets, we record:

* the anatomical structure or lesion being segmented;
* whether the annotation is binary or multiclass when available.

For detection datasets, we record:

* the detection target;
* annotation format when known.

For measurement datasets, we record the target measurements, such as:

* fetal head circumference;
* abdominal circumference;
* ejection fraction;
* intima-media thickness.

For registration and reconstruction datasets, we describe the relevant modalities, transformations, poses, landmarks, or reference data.

## Access Does Not Imply Reuse Permission

Inclusion in this repository does **not** imply that the original dataset can be freely redistributed, used commercially, or used without ethical or institutional approval.

Each dataset remains governed by its original:

* license;
* data-use agreement;
* repository terms;
* institutional restrictions;
* ethical requirements.

Users must verify the current terms directly from the original dataset provider before using a dataset.

## Scope Updates

The scope may evolve as new forms of medical ultrasound data become publicly available.

Substantial changes to the inclusion or exclusion criteria will be documented in the repository changelog.
