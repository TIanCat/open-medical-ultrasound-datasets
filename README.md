# Open Medical Ultrasound Dataset Atlas

A curated and continuously updated atlas of publicly accessible medical ultrasound imaging datasets.

## Overview

- 104 verified primary dataset families
- 89 open access
- 13 application/registration
- 2 controlled/restricted
- Last updated: 2026-09-02

## Scope

See [Scope](docs/scope.md).

## Dataset Atlas


### Breast
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0001](datasets/0001.yaml) | UDIAT / Dataset B | Breast | 2D B-mode | 163 images / 163 women | detection; segmentation; binary classification | 🟡 Application | [Yap et al., 2018](https://doi.org/10.1109/JBHI.2017.2731873) | [MMU access page](https://helward.mmu.ac.uk/STAFF/m.yap/dataset.php) |
| [0002](datasets/0002.yaml) | OASBUD | Breast | 2D post-beamformed RF echoes (no B-mode images) | 100 lesions / 78 women / 2 RF planes per lesion | RF/QUS analysis; B-mode visualization; segmentation; binary classification | 🟢 Open | [Piotrzkowska-Wróblewska et al., 2017](https://doi.org/10.1002/mp.12538) | [Zenodo](https://zenodo.org/records/545928) |
| [0003](datasets/0003.yaml) | Medical Image Database (MID) | Breast | 2D B-mode | 180 test images / 180 patients (+15 tuning images) | segmentation; contour initialization/evaluation | 🟢 Open; no stated license | [Rodtook et al., 2018](https://doi.org/10.1016/j.patcog.2018.01.032) | [Online Medical Images](https://www.onlinemedicalimages.com/index.php/en/site-map) |
| [0004](datasets/0004.yaml) | STU-Hospital | Breast | 2D B-mode PNG | 42 image/mask pairs (external test set) | lesion segmentation | 🟢 Open; no stated dataset license | [Zhuang et al., 2019](https://doi.org/10.1371/journal.pone.0221535) | [GitHub](https://github.com/xbhlk/STU-Hospital) |
| [0005](datasets/0005.yaml) | BUSI | Breast | 2D B-mode PNG | 780 images / 600 women | 3-class classification; lesion segmentation; mask-derived localization | 🟢 Open; no stated dataset license | [Al-Dhabyani et al., 2020](https://doi.org/10.1016/j.dib.2019.104863) | [MathWorks mirror](https://ssd.mathworks.com/supportfiles/image/data/Dataset_BUSI.zip) |

### Thyroid
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [US044](datasets/US044.yaml) | DDTI | Thyroid nodule | 2D B-mode images | 389 cases; 637 processed images | segmentation; TI-RADS analysis | 🟢 Open | [Paper](https://doi.org/10.1117/12.2073532) | [Data](https://cimalab.unal.edu.co/projects/detail/20/) |
| [US045](datasets/US045.yaml) | TN-SCUI2020 | Thyroid nodule | 2D B-mode images | 4,554 images/cases | segmentation; classification | 🟢 Open | [Paper](https://doi.org/10.5281/zenodo.3715942) | [Zenodo](https://zenodo.org/records/3715942) |
| [US046](datasets/US046.yaml) | KFGNet dataset | Thyroid nodule | 2D B-mode videos | 3,668 videos | localization; classification | 🟢 Open | Project release | [GitHub](https://github.com/NeuronXJTU/KFGNet) |
| [US047](datasets/US047.yaml) | TG3K | Thyroid gland | 2D B-mode frames | ~3,583–3,585 frames | segmentation | 🟢 Open | [Paper](https://doi.org/10.1016/j.compbiomed.2022.106389) | [GitHub](https://github.com/haifangong/TRFE-Net-for-thyroid-nodule-segmentation) |
| [US048](datasets/US048.yaml) | TN3K | Thyroid nodule | 2D B-mode images | 3,493 images / 2,421 patients | segmentation | 🟢 Open | [Paper](https://doi.org/10.1016/j.compbiomed.2022.106389) | [GitHub](https://github.com/haifangong/TRFE-Net-for-thyroid-nodule-segmentation) |
| [US049](datasets/US049.yaml) | SegThy | Thyroid | tracked US + MRI | 214 subjects in 2 subsets | 3D segmentation; volumetry | 🟢 Open | [Paper](https://doi.org/10.1371/journal.pone.0268550) | [Data](https://www.cs.cit.tum.de/en/camp/publications/segthy-dataset/) |
| [US050](datasets/US050.yaml) | Thyroid Ultrasound Cine-clip | Thyroid nodule | 2D B-mode cine clips | 192 nodules / 17,412 frames | segmentation; risk stratification | 🟡 Application | [Paper](https://doi.org/10.1148/radiol.211667) | [Project page](https://aimi.stanford.edu/datasets/thyroid-ultrasound-cine-clip) |
| [US051](datasets/US051.yaml) | TN5000 | Thyroid nodule | 2D B-mode images | 5,000 images | detection; classification | 🟢 Open | [Paper](https://doi.org/10.1038/s41597-025-05757-4) | [Figshare](https://springernature.figshare.com/articles/dataset/TN5000_An_Ultrasound_Image_Dataset_for_Thyroid_Nodule_Detection_and_Classification/28455641) |

### Obstetrics
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|

### Heart
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [US031](datasets/US031.yaml) | CAMUS | Heart (A2C/A4C) | 2D echo sequences | 500 patients | segmentation; function measurement | 🟢 Open | [Paper](https://doi.org/10.1109/TMI.2019.2900516) | [CAMUS](https://www.creatis.insa-lyon.fr/Challenge/camus/) |
| [US032](datasets/US032.yaml) | EchoNet-Dynamic | Heart (A4C) | 2D echo videos | 10,030 videos | segmentation; EF/volume regression | 🟡 Application | [Paper](https://doi.org/10.1038/s41586-020-2145-8) | [GitHub](https://echonet.github.io/dynamic/) |
| [US033](datasets/US033.yaml) | EchoCP | Heart / PFO | contrast TTE videos | 60 videos / 30 patients | PFO grading; chamber segmentation | 🟢 Open | [Paper](https://doi.org/10.48550/arXiv.2105.08267) | [Kaggle](https://www.kaggle.com/datasets/xiaoweixumedicalai/echocp) |
| [US034](datasets/US034.yaml) | Tufts Medical Echocardiogram Dataset (TMED-2) | Heart / aortic stenosis | 2D TTE images | 599 fully labeled studies | AS and view classification | 🟡 Application | Machine Learning for Healthcare Conference (MLHC 2021), PMLR | [TMED](https://tmed.cs.tufts.edu/tmed_v2.html) |
| [US035](datasets/US035.yaml) | EchoNet-LVH | Heart (PLAX) | 2D echo videos | 12,000 videos | wall/chamber measurement | 🟡 Application | [Paper](https://doi.org/10.1001/jamacardio.2021.6059) | [Project page](https://aimi.stanford.edu/datasets/echonet-lvh) |
| [US036](datasets/US036.yaml) | CardiacUDA / CardiacUDC | Heart (4 views) | 2D echo videos | 992 videos in paper | segmentation; domain adaptation | 🟢 Open | [Paper](https://doi.org/10.48550/arXiv.2309.11145) | [Kaggle](https://www.kaggle.com/datasets/xiaoweixumedicalai/cardiacudc-dataset) |
| [US037](datasets/US037.yaml) | EchoNet-Pediatric | Pediatric heart | 2D echo videos | 7,643 videos | segmentation; EF/volume regression | 🟡 Application | [Paper](https://doi.org/10.1016/j.echo.2023.01.015) | [GitHub](https://echonet.github.io/pediatric/) |
| [US038](datasets/US038.yaml) | CACTUS | Cardiac phantom | 2D B-mode images | 37,736 images | view classification; quality grading | 🟢 Open | [Paper](https://doi.org/10.1016/j.compbiomed.2025.110003) | [Data](https://doi.org/10.20383/103.01484) |
| [US039](datasets/US039.yaml) | MIMIC-IV-Echo | Heart | DICOM + measurements | 206,488 studies | measurement; multimodal learning | 🔴 Controlled | [Paper](https://doi.org/10.13026/307c-mr50) | [PhysioNet](https://physionet.org/content/mimic-iv-echo/1.0.1/) |

### Musculoskeletal
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [US053](datasets/US053.yaml) | LUMINOUS | Lumbar multifidus | 2D B-mode images | 109 subjects | segmentation; CSA/echo intensity | 🟢 Open | [Paper](https://doi.org/10.1186/s12891-020-03679-3) | [Data](http://data.sonography.ai/) |
| [US054](datasets/US054.yaml) | deepMTJ test set | Muscle-tendon junction | 2D B-mode images | 1,344 images | localization; tracking | 🟢 Open | [Paper](https://doi.org/10.1109/TBME.2021.313054) | [Figshare](https://doi.org/10.6084/m9.figshare.16822978.v2) |
| [US055](datasets/US055.yaml) | FALLMUD | Lower-leg muscle | 2D B-mode images | 812 images | fascicle/aponeurosis segmentation | 🟢 Open | ACM BCB 2021 | [Data](https://kalisteo.cea.fr/index.php/fallmud/) |
| [US057](datasets/US057.yaml) | TUS-REC2024 | Forearm | tracked freehand US | 2,040 scans / 85 volunteers | 3D reconstruction; pose estimation | 🟡 Application | [Paper](https://doi.org/10.48550/arXiv.2506.21765) | [GitHub](https://github-pages.ucl.ac.uk/tus-rec-challenge/TUS-REC2024/) |
| [US058](datasets/US058.yaml) | Machine Learning-Driven Heckmatt Grading in FSHD | Muscle / FSHD | 2D B-mode images | 25,005 images / 290 participants | grading; segmentation | 🟢 Open | [Paper](https://doi.org/10.17632/yzg86vb895.1) | [Mendeley Data](https://data.mendeley.com/datasets/yzg86vb895/1) |
| [US059](datasets/US059.yaml) | Transverse Musculoskeletal Ultrasound Dataset for NMD Assessment | Muscle / NMD | 2D B-mode images | 3,917 images / 1,283 subjects | segmentation; quantitative assessment | 🟢 Open | [Paper](https://doi.org/10.1016/j.compbiomed.2021.104623) | [Mendeley Data](https://data.mendeley.com/datasets/3jykz7wz8d/1) |

### Multi‑anatomy
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [US040](datasets/US040.yaml) | Clinical Ultrasound Image Repository | Abdominal; cardiac; OB/GYN | clinical DICOM | 2,000 studies | representation learning | 🟢 Open | AWS Registry of Open Data | [AWS](https://registry.opendata.aws/clinical-ultrasound-image-data/) |

### Other
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [US041](datasets/US041.yaml) | GIST514-DB | GI tract tumors | endoscopic US | 514 cases/images | classification; detection; segmentation | 🟢 Open | [Paper](https://doi.org/10.1016/j.compbiomed.2022.106424) | [GitHub](https://github.com/WuJunde/Query2) |
| [US042](datasets/US042.yaml) | LEPset | Pancreas | endoscopic US | 11,500 images / 420 patients | classification; pretraining | 🟢 Open | [Dataset](https://doi.org/10.5281/zenodo.8041285) | [Zenodo](https://zenodo.org/records/8041285) |
| [US043](datasets/US043.yaml) | C-TRUS | Colon wall | 2D B-mode images | 827 images / 13 patients | segmentation | 🟢 Open | [Paper](https://doi.org/10.1007/978-3-031-73647-6_10) | [GitHub](https://github.com/wwu-mmll/c-trus) |


## Contributing

New datasets and corrections are welcome through Issues or Pull Requests.

## Citation
