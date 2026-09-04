# Open Medical Ultrasound Dataset Atlas

A curated and continuously updated atlas of publicly accessible medical ultrasound imaging datasets.

## Overview

- 103 verified primary dataset families
- 86 open access
- 15 application/registration
- 2 controlled/restricted
- Last updated: 2026-09-03

## Scope

See [Scope](docs/scope.md).

## Dataset Atlas


### Breast
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0001](datasets/00_breast/0001.yaml) | UDIAT / Dataset B | Breast | 2D B-mode | 163 images | classification; segmentation; detection; | 🟡 Application | [Yap et al., 2018](https://doi.org/10.1109/JBHI.2017.2731873) | [MMU access page](https://helward.mmu.ac.uk/STAFF/m.yap/dataset.php) |
| [0002](datasets/00_breast/0002.yaml) | OASBUD | Breast | 2D post-beamformed RF echoes (no B-mode images) | 100 lesions / 78 women | RF/QUS analysis; visualization; segmentation; classification | 🟢 Open | [Piotrzkowska-Wróblewska et al., 2017](https://doi.org/10.1002/mp.12538) | [Zenodo](https://zenodo.org/records/545928) |
| [0003](datasets/00_breast/0003.yaml) | Medical Image Database (MID) | Breast | 2D B-mode | 180 images (paper-reported) | segmentation; classification | 🟢 Open | [Rodtook et al., 2018](https://doi.org/10.1016/j.patcog.2018.01.032) | [Online Medical Images](https://www.onlinemedicalimages.com/index.php/en/site-map) |
| [0004](datasets/00_breast/0004.yaml) | STU-Hospital | Breast | 2D B-mode | 42 image-mask pairs | segmentation | 🟢 Open | [Zhuang et al., 2019](https://doi.org/10.1371/journal.pone.0221535) | [GitHub](https://github.com/xbhlk/STU-Hospital) |
| [0005](datasets/00_breast/0005.yaml) | BUSI | Breast | 2D B-mode | 780 images | classification; segmentation | 🟢 Open | [Al-Dhabyani et al., 2020](https://doi.org/10.1016/j.dib.2019.104863) | [Mendeley Data](https://data.mendeley.com/datasets/k8t3gnx9h6/1) |
| [0006](datasets/00_breast/0006.yaml) | BreastVid | Breast | 2D B-mode cine / image sequences | 188 videos / 25,272 frames (paper-reported) | detection; classification | 🟢 Open | [Lin et al., 2022](https://doi.org/10.1007/978-3-031-16437-8_59) | [CVA-Net repository](https://github.com/jhl-Det/CVA-Net) |
| [0007](datasets/00_breast/0007.yaml) | Breast Ultrasound Image Database / QAMEBI | Breast | 2D B-mode | 232 lesions/images | classification; segmentation | 🟢 Open | [Abbasian Ardakani et al., 2023](https://doi.org/10.1016/j.compbiomed.2022.106438) | [QAMEBI](https://qamebi.com/breast-ultrasound-images-database/) |
| [0008](datasets/00_breast/0008.yaml) | BUS-BRA | Breast | 2D B-mode | 1,875 images / 1,064 women | segmentation; detection; classification | 🟢 Open | [Gómez-Flores et al., 2024](https://doi.org/10.1002/mp.16812) | [Zenodo](https://zenodo.org/records/8231412) |
| [0009](datasets/00_breast/0009.yaml) | BUSI_WHU | Breast | 2D B-mode | 927 images / 816 patients | segmentation; classification; measurement | 🟢 Open | -- | [Mendeley Data v3](https://data.mendeley.com/datasets/k6cpmwybk3/3) |
| [0010](datasets/00_breast/0010.yaml) | TDSC-ABUS2023 | Breast | 3D ABUS volumes | 200 cases / 200 volumes | classification; segmentation; detection | 🟡 Application | [Luo et al., 2025](https://doi.org/10.48550/arXiv.2501.15588) | [Grand Challenge](https://tdsc-abus2023.grand-challenge.org/Dataset/) |
| [0011](datasets/00_breast/0011.yaml) | BUS_UC | Breast | 2D static ultrasound images | 811 image-mask pairs | classification; segmentation | 🟢 Open | [Iqbal & Sharif, 2024](https://doi.org/10.1016/j.engappai.2023.107292) | [Mendeley Data](https://data.mendeley.com/datasets/3ksd7w7jkx/1) |
| [0012](datasets/00_breast/0012.yaml) | BUS-UCLM | Breast | 2D B-mode + Color Doppler | 683 image-mask pairs / 38 patients | classification; segmentation | 🟢 Open | [Vallez et al., 2025](https://doi.org/10.1038/s41597-025-04562-3) | [Mendeley Data v3](https://data.mendeley.com/datasets/7fvgj4jsp7/3) |
| [0013](datasets/00_breast/0013.yaml) | US3M | Breast |  2D B-mode + Color Doppler + Elastography | 1,532 images / 248 patients | classification | 🟢 Open | [Yan et al., 2024](https://doi.org/10.1016/j.inffus.2024.102592) | [Kaggle](https://www.kaggle.com/datasets/timesxy/multimodal-breast-ultrasound-dataset-us3m) |
| [0014](datasets/00_breast/0014.yaml) | ALN-Ultra | Breast  | Paired ultrasound images + videos | 257 patients; exact image/video counts unavailable | classification | 🔴 Controlled  | -- | [Zenodo replacement record](https://zenodo.org/records/18483501) |


### Thyroid
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0101](datasets/01_thyroid/0101.yaml) | DDTI | Thyroid nodule | 2D B-mode images | 389 cases; 637 processed images | segmentation; TI-RADS analysis | 🟢 Open | [Paper](https://doi.org/10.1117/12.2073532) | [Data](https://cimalab.unal.edu.co/projects/detail/20/) |
| [0102](datasets/01_thyroid/0102.yaml) | TN-SCUI2020 | Thyroid nodule | 2D B-mode images | 4,554 images/cases | segmentation; classification | 🟢 Open | [Paper](https://doi.org/10.5281/zenodo.3715942) | [Zenodo](https://zenodo.org/records/3715942) |
| [0103](datasets/01_thyroid/0103.yaml) | KFGNet dataset | Thyroid nodule | 2D B-mode videos | 3,668 videos | localization; classification | 🟢 Open | Project release | [GitHub](https://github.com/NeuronXJTU/KFGNet) |
| [0104](datasets/01_thyroid/0104.yaml) | TG3K | Thyroid gland | 2D B-mode frames | ~3,583–3,585 frames | segmentation | 🟢 Open | [Paper](https://doi.org/10.1016/j.compbiomed.2022.106389) | [GitHub](https://github.com/haifangong/TRFE-Net-for-thyroid-nodule-segmentation) |
| [0105](datasets/01_thyroid/0105.yaml) | TN3K | Thyroid nodule | 2D B-mode images | 3,493 images / 2,421 patients | segmentation | 🟢 Open | [Paper](https://doi.org/10.1016/j.compbiomed.2022.106389) | [GitHub](https://github.com/haifangong/TRFE-Net-for-thyroid-nodule-segmentation) |
| [0106](datasets/01_thyroid/0106.yaml) | SegThy | Thyroid | tracked US + MRI | 214 subjects in 2 subsets | 3D segmentation; volumetry | 🟢 Open | [Paper](https://doi.org/10.1371/journal.pone.0268550) | [Data](https://www.cs.cit.tum.de/en/camp/publications/segthy-dataset/) |
| [0107](datasets/01_thyroid/0107.yaml) | Thyroid Ultrasound Cine-clip | Thyroid nodule | 2D B-mode cine clips | 192 nodules / 17,412 frames | segmentation; risk stratification | 🟡 Application | [Paper](https://doi.org/10.1148/radiol.211667) | [Project page](https://aimi.stanford.edu/datasets/thyroid-ultrasound-cine-clip) |
| [0108](datasets/01_thyroid/0108.yaml) | TN5000 | Thyroid nodule | 2D B-mode images | 5,000 images | detection; classification | 🟢 Open | [Paper](https://doi.org/10.1038/s41597-025-05757-4) | [Figshare](https://springernature.figshare.com/articles/dataset/TN5000_An_Ultrasound_Image_Dataset_for_Thyroid_Nodule_Detection_and_Classification/28455641) |

### Obstetrics
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0201](datasets/02_obstetrics/0201.yaml) | HC18 | Fetus / fetal head | 2D B-mode images | 1,334 images / 551 pregnant women | head delineation; circumference measurement | 🟢 Open | [Paper](https://doi.org/10.1371/journal.pone.0200412) | [Zenodo](https://doi.org/10.5281/zenodo.1322000) |
| [0202](datasets/02_obstetrics/0202.yaml) | FETAL_PLANES_DB | Fetus / maternal cervix | 2D B-mode images | 12,400 images / 1,792 pregnant women | standard-plane classification | 🟢 Open | [Paper](https://doi.org/10.1038/s41598-020-67076-5) | [Zenodo](https://doi.org/10.5281/zenodo.3904280) |
| [0203](datasets/02_obstetrics/0203.yaml) | JNU-IFM | Maternal pubic symphysis / fetal head | 2D transperineal video frames | 6,224 frames / 78 videos / 51 women | segmentation; frame classification | 🟢 Open | [Paper](https://doi.org/10.1016/j.dib.2022.107904) | [Figshare](https://doi.org/10.6084/m9.figshare.14371652) |
| [0204](datasets/02_obstetrics/0204.yaml) | African Fetal Standard Plane Dataset | Fetus / abdomen, brain, femur, thorax | 2D B-mode images | 450 images / 125 participant records | standard-plane classification; domain adaptation | 🟢 Open | [Paper](https://doi.org/10.1038/s41598-023-29490-3) | [Zenodo](https://doi.org/10.5281/zenodo.7540448) |
| [0205](datasets/02_obstetrics/0205.yaml) | FPUS23 | 23-week fetal phantom | 2D B-mode images | 15,728 images | plane and orientation classification; object detection | 🟢 Open | [Paper](https://doi.org/10.1109/ACCESS.2023.3284315) | [GitHub](https://github.com/bharathprabakaran/FPUS23) |
| [0206](datasets/02_obstetrics/0206.yaml) | Fetal Abdominal Structures Segmentation Dataset | Fetus / fetal abdomen | 2D B-mode images | 1,588 images / 169 pregnancies | multi-structure segmentation | 🟢 Open | Mendeley data resource | [Mendeley Data](https://doi.org/10.17632/4gcpm9dsc3.1) |
| [0207](datasets/02_obstetrics/0207.yaml) | ACOUSLIC-AI | Fetus / fetal abdomen | 2D blind-sweep sequences | 300 public cases / 252,000 frames | frame localization; segmentation; circumference measurement | 🟢 Open | [Paper](https://doi.org/10.1016/j.media.2025.103640) | [Zenodo](https://doi.org/10.5281/zenodo.12697994) |
| [0208](datasets/02_obstetrics/0208.yaml) | PSFHS | Maternal pelvis / fetal head / pubic symphysis | 2D transperineal images | 1,358 images / 1,124 participants | segmentation; angle-of-progression measurement | 🟢 Open | [Paper](https://doi.org/10.1038/s41597-024-03266-4) | [Zenodo](https://doi.org/10.5281/zenodo.10969427) |
| [0209](datasets/02_obstetrics/0209.yaml) | FOCUS | Fetus / fetal heart / thorax | 2D four-chamber images | 300 images / 217 subjects | detection; segmentation; cardiothoracic ratio | 🟢 Open | Zenodo data resource | [Zenodo](https://doi.org/10.5281/zenodo.14597550) |
| [0210](datasets/02_obstetrics/0210.yaml) | Maternal-Fetal Ultrasound Video Dataset | Maternal pelvis / fetal head / pubic symphysis | 2D transperineal videos | 774 videos / 68,106 frames | plane classification; segmentation; landmark detection; biometry | 🟢 Open | [Paper](https://doi.org/10.1038/s41597-026-06900-5) | [Zenodo](https://doi.org/10.5281/zenodo.17655183) |

### Cardiac
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0301](datasets/03_cardiac/0301.yaml) | CAMUS | Heart (A2C/A4C) | 2D echo sequences | 500 patients | segmentation; function measurement | 🟢 Open | [Paper](https://doi.org/10.1109/TMI.2019.2900516) | [CAMUS](https://www.creatis.insa-lyon.fr/Challenge/camus/) |
| [0302](datasets/03_cardiac/0302.yaml) | EchoNet-Dynamic | Heart (A4C) | 2D echo videos | 10,030 videos | segmentation; EF/volume regression | 🟡 Application | [Paper](https://doi.org/10.1038/s41586-020-2145-8) | [GitHub](https://echonet.github.io/dynamic/) |
| [0303](datasets/03_cardiac/0303.yaml) | EchoCP | Heart / PFO | contrast TTE videos | 60 videos / 30 patients | PFO grading; chamber segmentation | 🟢 Open | [Paper](https://doi.org/10.48550/arXiv.2105.08267) | [Kaggle](https://www.kaggle.com/datasets/xiaoweixumedicalai/echocp) |
| [0304](datasets/03_cardiac/0304.yaml) | Tufts Medical Echocardiogram Dataset (TMED-2) | Heart / aortic stenosis | 2D TTE images | 599 fully labeled studies | AS and view classification | 🟡 Application | Machine Learning for Healthcare Conference (MLHC 2021), PMLR | [TMED](https://tmed.cs.tufts.edu/tmed_v2.html) |
| [0305](datasets/03_cardiac/0305.yaml) | EchoNet-LVH | Heart (PLAX) | 2D echo videos | 12,000 videos | wall/chamber measurement | 🟡 Application | [Paper](https://doi.org/10.1001/jamacardio.2021.6059) | [Project page](https://aimi.stanford.edu/datasets/echonet-lvh) |
| [0306](datasets/03_cardiac/0306.yaml) | CardiacUDA / CardiacUDC | Heart (4 views) | 2D echo videos | 992 videos in paper | segmentation; domain adaptation | 🟢 Open | [Paper](https://doi.org/10.48550/arXiv.2309.11145) | [Kaggle](https://www.kaggle.com/datasets/xiaoweixumedicalai/cardiacudc-dataset) |
| [0307](datasets/03_cardiac/0307.yaml) | EchoNet-Pediatric | Pediatric heart | 2D echo videos | 7,643 videos | segmentation; EF/volume regression | 🟡 Application | [Paper](https://doi.org/10.1016/j.echo.2023.01.015) | [GitHub](https://echonet.github.io/pediatric/) |
| [0308](datasets/03_cardiac/0308.yaml) | CACTUS | Cardiac phantom | 2D B-mode images | 37,736 images | view classification; quality grading | 🟢 Open | [Paper](https://doi.org/10.1016/j.compbiomed.2025.110003) | [Data](https://doi.org/10.20383/103.01484) |
| [0309](datasets/03_cardiac/0309.yaml) | MIMIC-IV-Echo | Heart | DICOM + measurements | 206,488 studies | measurement; multimodal learning | 🔴 Controlled | [Paper](https://doi.org/10.13026/307c-mr50) | [PhysioNet](https://physionet.org/content/mimic-iv-echo/1.0.1/) |

### Lung
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0401](datasets/04_lung/0401.yaml) | POCUS Dataset for COVID-19 Detection | Lung | 2D POCUS videos and images | Paper: 261 recordings / 216 patients; current metadata: 374 records | classification; severity scoring; feature segmentation | 🟢 Open | [Paper](https://doi.org/10.3390/app11020672) | [GitHub](https://github.com/jannisborn/covid19_ultrasound) |
| [0402](datasets/04_lung/0402.yaml) | COVIDx-US | Lung | 2D POCUS videos and extracted frames | Repository: 242 videos / 29,651 frames | classification; severity assessment | 🟢 Open | [Paper](https://doi.org/10.31083/j.fbl2707198) | [GitHub](https://github.com/nrc-cnrc/COVID-US) |
| [0403](datasets/04_lung/0403.yaml) | LUSS_phantom | Lung ultrasound phantom | 2D cine loops and extracted frames | 564 annotated frames | artefact segmentation; B-line quantification | 🟢 Open | [Paper](https://doi.org/10.1016/j.ultras.2024.107251) | [Data](https://doi.org/10.5518/1485) |
| [0404](datasets/04_lung/0404.yaml) | Lung Ultrasound Images for Automated AI-based Lung Disease Classification | Lung | 2D B-mode images | 1,062 images / 149 patients | 3-class lung condition classification | 🟢 Open | [Paper](https://doi.org/10.1016/j.dib.2025.112034) | [Mendeley Data](https://data.mendeley.com/datasets/hb3p34ytvx/2) |
| [0405](datasets/04_lung/0405.yaml) | POCUS LUS Datasets | Lung | 2D POCUS images | 10 images / 8 upstream patient/source IDs | 3-class classification | 🟢 Open | No dedicated paper | [Figshare](https://doi.org/10.6084/m9.figshare.29364743.v1) |
| [0406](datasets/04_lung/0406.yaml) | PU2756 | Lung / peripheral pulmonary tumor | 2D B-mode images | 2,756 images / 2,756 patients | segmentation; binary classification | 🟢 Open | [Paper](https://doi.org/10.1038/s41597-026-07715-0) | [Figshare](https://doi.org/10.6084/m9.figshare.32672274) |

### Liver and Gallbladder
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0501](datasets/05_liver_gallbladder/0501.yaml) | Dataset of B-mode fatty liver ultrasound images | Liver / hepatic steatosis | 2D B-mode image sequences | 550 images / 55 patients | classification; steatosis regression | 🟢 Open | [Paper](https://doi.org/10.1007/s11548-018-1843-2) | [Zenodo](https://zenodo.org/records/1009146) |
| [0502](datasets/05_liver_gallbladder/0502.yaml) | B-mode-and-CEUS-Liver | Liver / focal liver mass | 2D B-mode images + CEUS cine loops | 120 subjects / 1,859 DICOM instances | lesion classification; temporal analysis; response assessment | 🟢 Open | TCIA collection | [TCIA](https://www.cancerimagingarchive.net/collection/b-mode-and-ceus-liver/) |
| [0503](datasets/05_liver_gallbladder/0503.yaml) | Annotated Ultrasound Liver images | Liver / liver mass | 2D B-mode images | 735 images | classification; segmentation; detection | 🟢 Open | [Paper](https://doi.org/10.1093/bib/bbac569) | [Zenodo](https://zenodo.org/records/7272660) |
| [0504](datasets/05_liver_gallbladder/0504.yaml) | GBCU | Gallbladder / gallbladder pathology | 2D grayscale B-mode images | 1,255 images / 218 patients | classification; object detection | 🟡 Application | [Paper](https://doi.org/10.1109/CVPR52688.2022.02022) | [Project page](https://gbc-iitd.github.io/data/gbcu) |
| [0505](datasets/05_liver_gallbladder/0505.yaml) | GBUSV | Gallbladder / gallbladder pathology | 2D grayscale B-mode videos | 64 videos / 15,800 frames | representation learning; video classification | 🟡 Application | [Paper](https://doi.org/10.1007/978-3-031-16440-8_41) | [Project page](https://gbc-iitd.github.io/data/gbusv) |
| [0506](datasets/05_liver_gallbladder/0506.yaml) | liver_ultrasound | Liver / adjacent abdominal structures | 2D grayscale images | 400 images | 14-class object detection | 🟢 Open | Roboflow project | [Roboflow](https://universe.roboflow.com/joe-klepich/liver_ultrasound) |
| [0507](datasets/05_liver_gallbladder/0507.yaml) | BEHSOF | Liver / NAFLD | 2D ultrasound + clinical data | 1,669 images / 113 individuals | classification; grading; regression | 🟢 Open | Figshare data resource | [Figshare](https://figshare.com/articles/dataset/BEHSOF/26389069) |
| [0508](datasets/05_liver_gallbladder/0508.yaml) | Saudi NAFLD Liver Ultrasound Dataset | Liver / NAFLD | 2D grayscale and color images | 10,352 images / 384 patients | steatosis grading; fibrosis staging; classification | 🟡 Application | [Paper](https://doi.org/10.1016/j.dib.2024.111266) | [OSF](https://doi.org/10.17605/OSF.IO/C2YG8) |
| [0509](datasets/05_liver_gallbladder/0509.yaml) | SMC-LUD | Liver / focal liver lesions | 2D B-mode images | 5,385 images / 1,021 patients | HCC vs hemangioma classification | 🟢 Open | [Paper](https://doi.org/10.1038/s41597-026-07023-7) | [Figshare](https://doi.org/10.6084/m9.figshare.31112716) |


### Musculoskeletal
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0601](datasets/06_musculoskeletal/0601.yaml) | LUMINOUS | Lumbar multifidus | 2D B-mode images | 109 subjects | segmentation; CSA/echo intensity | 🟢 Open | [Paper](https://doi.org/10.1186/s12891-020-03679-3) | [Data](http://data.sonography.ai/) |
| [0602](datasets/06_musculoskeletal/0602.yaml) | deepMTJ test set | Muscle-tendon junction | 2D B-mode images | 1,344 images | localization; tracking | 🟢 Open | [Paper](https://doi.org/10.1109/TBME.2021.313054) | [Figshare](https://doi.org/10.6084/m9.figshare.16822978.v2) |
| [0603](datasets/06_musculoskeletal/0603.yaml) | FALLMUD | Lower-leg muscle | 2D B-mode images | 812 images | fascicle/aponeurosis segmentation | 🟢 Open | ACM BCB 2021 | [Data](https://kalisteo.cea.fr/index.php/fallmud/) |
| [0604](datasets/06_musculoskeletal/0604.yaml) | TUS-REC2024 | Forearm | tracked freehand US | 2,040 scans / 85 volunteers | 3D reconstruction; pose estimation | 🟡 Application | [Paper](https://doi.org/10.48550/arXiv.2506.21765) | [GitHub](https://github-pages.ucl.ac.uk/tus-rec-challenge/TUS-REC2024/) |
| [0605](datasets/06_musculoskeletal/0605.yaml) | Machine Learning-Driven Heckmatt Grading in FSHD | Muscle / FSHD | 2D B-mode images | 25,005 images / 290 participants | grading; segmentation | 🟢 Open | [Paper](https://doi.org/10.17632/yzg86vb895.1) | [Mendeley Data](https://data.mendeley.com/datasets/yzg86vb895/1) |
| [0606](datasets/06_musculoskeletal/0606.yaml) | Transverse Musculoskeletal Ultrasound Dataset for NMD Assessment | Muscle / NMD | 2D B-mode images | 3,917 images / 1,283 subjects | segmentation; quantitative assessment | 🟢 Open | [Paper](https://doi.org/10.1016/j.compbiomed.2021.104623) | [Mendeley Data](https://data.mendeley.com/datasets/3jykz7wz8d/1) |
| [0607](datasets/06_musculoskeletal/0607.yaml) | Paired robotic and handheld lumbar spine ultrasound | Lumbar spine / vertebral bone surface | Paired CT + tracked 2D B-mode sweeps | 598 US scans / 63 volunteers; 6,091 annotated frames | segmentation; US-CT registration; 3D reconstruction | 🟢 Open | [Paper](https://doi.org/10.1038/s41597-025-06047-9) | [Data](https://doi.org/10.48804/3XPCAE) |

### Vessel
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0701](datasets/07_vessel/0701.yaml) | OPULM PALA | Microvasculature / ultrasound contrast microbubbles | ultrafast contrast-enhanced ultrasound / ULM microbubble data | 6 benchmark datasets including simulated and in vivo acquisitions | microbubble localization; trajectory tracking; vascular reconstruction; ULM algorithm benchmarking | 🟢 Open | [Paper](https://doi.org/10.1038/s41551-021-00824-8) | [Zenodo](https://zenodo.org/records/4343435) |
| [0702](datasets/07_vessel/0702.yaml) | CUBS | Carotid artery | 2D B-mode static carotid ultrasound images | 1,088 participants; 2,176 common carotid artery images | carotid LI/MA boundary segmentation; carotid intima-media thickness measurement | 🟢 Open | [Paper](https://doi.org/10.1016/j.ultrasmedbio.2021.03.003) | [Mendeley Data](https://data.mendeley.com/datasets/fpv535fss7/1) |
| [0703](datasets/07_vessel/0703.yaml) | CCA | Carotid artery | 2D B-mode carotid ultrasound images | 2,307 images: 2,107 training images and 200 held-out validation images; additional external-device test sets are referenced | carotid artery segmentation; unseen-device / cross-domain generalization | 🟢 Open | [Paper](https://doi.org/10.1007/978-3-031-43901-8_13) | [GitHub](https://github.com/yuan-12138/MI-SegNet) |
| [0704](datasets/07_vessel/0704.yaml) | ULMShare | Mouse microvasculature / ultrasound localization microscopy | raw RF channel data and ULM-related acquisitions | 99 acquisitions from 61 mice; approximately 30 TB | ULM reconstruction; microbubble localization/tracking; vessel imaging; algorithm benchmarking | 🟢 Open | FRDR data resource | [FRDR](https://www.frdr-dfdr.ca/repo/dataset/10.20383/103.01550) |
| [0705](datasets/07_vessel/0705.yaml) | UK Biobank carotid ultrasound | Carotid artery | carotid 2D B-mode ultrasound imaging fields | large UK Biobank imaging resource; participant/image counts depend on the specific field and release | carotid phenotype analysis; intima-media thickness / vascular measurement; epidemiology and risk-association research | 🟡 Application | UK Biobank imaging resource | [UK Biobank Showcase](https://biobank.ndph.ox.ac.uk/showcase/) |


### Brain
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0801](datasets/08_brain/0801.yaml) | BITE | Brain / brain tumor / resection cavity | Contrast-enhanced T1 MRI + intraoperative 2D/3D B-mode US | 14 patients | MRI-US and longitudinal registration; TRE evaluation | 🟢 Open | [Paper](https://doi.org/10.1118/1.4709600) | [BITE](https://nist.mni.mcgill.ca/bite-brain-images-of-tumors-for-evaluation-database/) |
| [0802](datasets/08_brain/0802.yaml) | RESECT | Brain / low-grade glioma | preoperative MRI + intraoperative ultrasound (tracked 2D sweeps / reconstructed 3D iUS) | 23 low-grade glioma surgery cases | multimodal registration; landmark-error evaluation; tumor / resection-cavity segmentation in extension resources | 🟢 Open | [Paper](https://doi.org/10.1002/mp.12268) | [Sigma2 / NIRD](https://archive.sigma2.no/pages/public/datasetDetail.jsf?id=10.11582/2017.00004) |
| [0803](datasets/08_brain/0803.yaml) | In vivo rat brain for Ultrasound Localization Microscopy | Rat brain / cerebral microvasculature | raw RF ultrasound channel data + beamformed B-mode / ULM data | 23 Zenodo files; about 156.9 GB; approximately 200,000 frames/images | beamforming; image reconstruction; ULM; microbubble localization/tracking | 🟢 Open | [Paper](https://doi.org/10.1038/s41551-021-00824-8) | [Zenodo](https://zenodo.org/records/7883227) |
| [0804](datasets/08_brain/0804.yaml) | ReMIND | Brain / brain tumor / neurosurgery | preoperative MRI + intraoperative MRI + intraoperative ultrasound | 114 neurosurgical cases | MRI-ultrasound registration; tumor/resection-cavity segmentation; residual lesion analysis | 🟢 Open | [Paper](https://doi.org/10.1038/s41597-024-03295-z) | [TCIA](https://www.cancerimagingarchive.net/collection/remind/) |
| [0805](datasets/08_brain/0805.yaml) | BraTioUS | Brain / glioma | intraoperative 2D B-mode ultrasound | 1,669 B-mode iUS images from 142 glioma patients | brain tumor binary segmentation; derived tumor/no-tumor classification | 🟢 Open | Zenodo data resource | [Zenodo](https://zenodo.org/records/20800464) |
| [0806](datasets/08_brain/0806.yaml) | Dataset of 3D ultrasound neuroimages | Neonatal brain / transfontanelle ultrasound | 3D transfontanellar ultrasound volumes and derived 2D slices | small 3D neuroimage resource; current record has 9 files and supporting information | data augmentation; 2D slice synthesis; GAN training; image enhancement / representation research | 🟢 Open | Zenodo data resource | [Zenodo](https://zenodo.org/records/19593033) |
| [0807](datasets/08_brain/0807.yaml) | Mouse Brain Tumor Ultrasound | Mouse brain / brain tumor | high-resolution B-mode ultrasound images/videos | 1,856 images: 1,448 tumor images and 408 no-tumor images | tumor segmentation; derived tumor/no-tumor binary classification | 🟢 Open | [Paper](https://doi.org/10.1038/s41597-025-05619-z) | [Figshare](https://doi.org/10.6084/m9.figshare.27237894) |
| [0808](datasets/08_brain/0808.yaml) | Open-3DULM / Transcranial mice brain | Mouse brain / transcranial microvasculature | ultrafast ultrasound localization microscopy cine / 4D data | 5 mice; 370 ultrafast cine videos | 3D ULM reconstruction; cerebral blood-flow / vascular analysis; 4D spatiotemporal representation | 🟢 Open | [Paper](https://doi.org/10.1038/s44172-025-00415-4) | [Zenodo](https://zenodo.org/records/14289690) |


### Kidney
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [0901](datasets/09_kidney/0901.yaml) | The Open Kidney Ultrasound Data Set | Kidney / native and transplanted kidney | 2D B-mode images | 534 files / 514 unique patients and images | segmentation; view and transplant-status classification | 🟡 Application | [Paper](https://doi.org/10.1007/978-3-031-44521-7_15) | [GitHub](https://github.com/rsingla92/kidneyUS#data-access) |
| [0902](datasets/09_kidney/0902.yaml) | Ultrasound Normal Kidney Image | Kidney / liver / spleen | 2D B-mode images | 1,080 images | abdominal organ instance segmentation | 🟢 Open | Roboflow project | [Roboflow](https://universe.roboflow.com/jeevaws/ultrasound-normal-kidney-image) |


### Multi‑anatomy
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [1901](datasets/19_multi‑anatomy/1901.yaml) | Clinical Ultrasound Image Repository | Abdominal; cardiac; OB/GYN | clinical DICOM | 2,000 studies | representation learning | 🟢 Open | AWS Registry of Open Data | [AWS](https://registry.opendata.aws/clinical-ultrasound-image-data/) |
| [1902](datasets/19_multi‑anatomy/1902.yaml) | USenhance 2023 | Thyroid; carotid; liver; kidney; breast | 2D grayscale ultrasound PNG | 1,050 public training pairs + 364 public test inputs; 109 patients stated | low-to-high image reconstruction/enhancement | 🟢 Open download; CC BY-SA stated | [Challenge design](https://doi.org/10.5281/zenodo.7841250) | [Grand Challenge](https://ultrasoundenhance2023.grand-challenge.org/datasets/) |
| [1903](datasets/19_multi‑anatomy/1903.yaml) | Chinese multi-organ ultrasound image-text datasets | Breast; thyroid; liver | 2D ultrasound image pairs + Chinese reports | paper: 7,390 patients; public archive: 7,364 records / 17,149 images | report generation; image-text learning | 🟢 Open download; no stated dataset license | [Li et al., 2025](https://doi.org/10.1109/TMI.2024.3424978) | [Author repository](https://github.com/LijunRio/Ultrasound-Report-Generation) |


### Other
| ID | Dataset | Anatomy | Modality | Size | Task | Access | Paper | Data |
|---|---|---|---|---|---|---|---|---|
| [2001](datasets/20_other/2001.yaml) | GIST514-DB | GI tract tumors | endoscopic US | 514 cases/images | classification; detection; segmentation | 🟢 Open | [Paper](https://doi.org/10.1016/j.compbiomed.2022.106424) | [GitHub](https://github.com/WuJunde/Query2) |
| [2002](datasets/20_other/2002.yaml) | LEPset | Pancreas | endoscopic US | 11,500 images / 420 patients | classification; pretraining | 🟢 Open | [Dataset](https://doi.org/10.5281/zenodo.8041285) | [Zenodo](https://zenodo.org/records/8041285) |
| [2003](datasets/20_other/2003.yaml) | C-TRUS | Colon wall | 2D B-mode images | 827 images / 13 patients | segmentation | 🟢 Open | [Paper](https://doi.org/10.1007/978-3-031-73647-6_10) | [GitHub](https://github.com/wwu-mmll/c-trus) |
| [2004](datasets/20_other/2004.yaml) | OpticNerveSheaths | Optic nerve sheath | transorbital 2D ultrasound images | 464 ultrasound images | optic nerve sheath segmentation/localization; optic nerve sheath diameter measurement | 🟢 Open | [Paper](https://doi.org/10.1016/j.ultrasmedbio.2023.05.011) | [Mendeley Data](https://data.mendeley.com/datasets/kw8gvp8m8x/2) |
| [2005](datasets/20_other/2005.yaml) | Spinal Cord Injury Ultrasound Dataset | Porcine spinal cord / spinal cord injury | B-mode sagittal ultrasound images | 10,223 images: 4,467 pre-injury and 5,756 post-injury; 2,245 images include injury-localization annotations | injury-status classification; anatomical structure segmentation; injury localization / object detection | 🟢 Open | [Paper](https://doi.org/10.1038/s41598-025-16275-z) | [GitHub](https://github.com/HEPIUSLAB/ultrasound_spinal_cord_dataset) |
| [2006](datasets/20_other/2006.yaml) | Common Carotid Artery Ultrasound Images | Common carotid artery | 2D ultrasound PNG frames | 1,100 image/mask pairs / 11 subjects | artery-region segmentation; geometry measurement | 🟢 Open; CC BY 4.0 | [Data resource](https://doi.org/10.17632/d4xt63mgjm.1) | [Mendeley Data](https://data.mendeley.com/datasets/d4xt63mgjm/1) |
| [2007](datasets/20_other/2007.yaml) | Regensburg Pediatric Appendicitis Dataset | Appendix / pediatric abdomen | 2D B-mode images + tabular clinical data | release: 782 records / 2,097 images; paper: 579 patients / 1,709 images | diagnosis; management; severity; multimodal learning | 🟢 Open; CC BY-NC 4.0 | [Paper](https://doi.org/10.1016/j.media.2023.103042) | [Zenodo](https://doi.org/10.5281/zenodo.7711412) |
| [2008](datasets/20_other/2008.yaml) | Ultrasound Elastography Dataset for Unsupervised Training | CIRS Model 059 breast phantom | Paired ultrasound RF data | 2,200 unlabeled RF pairs | displacement/optical-flow estimation; unsupervised fine-tuning | 🟢 Public download; license not stated | [Paper](https://doi.org/10.1007/978-3-030-59716-0_48) | [IMPACT Lab](https://users.encs.concordia.ca/~impact/ultrasound-elastography-dataset-for-unsupervised-training/) |

## Contributing

New datasets and corrections are welcome through Issues or Pull Requests.

## Citation
