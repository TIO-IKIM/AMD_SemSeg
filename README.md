[![DOI](https://zenodo.org/badge/DOI/10.1167/tvst.14.7.8.svg)](https://doi.org/10.1167/tvst.14.7.8)
[![Python 3.11.6](https://img.shields.io/badge/python-3.11.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Three-Dimensional Quantification of Macular OCT Alterations Improves the Diagnostic Performance of Artificial Intelligence Models

This repository provides the model checkpoints and dummy data of our abovementioned work.

## Prerequisites
- Python3 >= 3.11.6 [Get Python](https://www.python.org/downloads/)
- Conda (optional) [Get Conda](https://docs.conda.io/en/latest/#install-svg-version-1-1-width-1-0em-height-1-0em-class-sd-octicon-sd-octicon-download-sd-text-primary-viewbox-0-0-16-16-aria-hidden-true-path-d-m2-75-14a1-75-1-75-0-0-1-1-12-25v-2-5a-75-75-0-0-1-1-5-0v2-5c0-138-112-25-25-25h10-5a-25-25-0-0-0-25-25v-2-5a-75-75-0-0-1-1-5-0v2-5a1-75-1-75-0-0-1-13-25-14z-path-path-d-m7-25-7-689v2a-75-75-0-0-1-1-5-0v5-689l1-97-1-969a-749-749-0-1-1-1-06-1-06l-3-25-3-25a-749-749-0-0-1-1-06-0l4-22-6-78a-749-749-0-1-1-1-06-1-06l1-97-1-969z-path-svg)
- GPU (optional, recommended)

## Getting started
1. Clone the repository

```bash
git clone https://github.com/TIO-IKIM/AMD_SemSeg.git
```
2. (Optional) Create a conda environment.
3. Install the requirements using `pip` or `conda`

```bash
pip install -r requirements.txt
```

## Relabeled data
You can find a relabeled version of Chiu et al.'s data [here](https://drive.google.com/drive/folders/1fe142pLOqKLe_vOUOHxMv-V11chLWCXP?usp=share_link).

Please find the original raw images [here](https://people.duke.edu/~sf59/Chiu_BOE_2014_dataset.htm).

## Inference
### nn-UNet
For a detailed overview on how to use nnU-Net's checkpoints to make predictions please refer to the [original repository](https://github.com/MIC-DKFZ/nnUNet/blob/f1851fbaf2c53dcb51b079b60a01de528a7d0c17/nnunetv2/inference/predict_from_raw_data.py#L39).

### Encoder only (embeddings)
You can find an example on how to load and use torch models [here](examples/01_using_pretrained_models.py).

## Inquiries

If you have any questions regarding the code, collaborations or different encoders, please raise an issue.

## Citation

```
@article{10.1167/tvst.14.7.8,
    author = {Heine, Lukas and Vahldiek, Anna and Vahldiek Benja and Hörst, Fabian and Seibold, Constantin and Lever, Mael and Pauleikhoff, Laurenz and Bechrakis, Nikolaos and Pauleikhoff, Daniel and Kleesiek, Jens},
    title = {Three-Dimensional Quantification of Macular OCT Alterations Improves the Diagnostic Performance of Artificial Intelligence Models},
    journal = {Translational Vision Science & Technology},
    volume = {14},
    number = {7},
    pages = {8-8},
    year = {2025},
    month = {07},
    issn = {2164-2591},
    doi = {10.1167/tvst.14.7.8},
    url = {https://doi.org/10.1167/tvst.14.7.8},
    eprint = {https://arvojournals.org/arvo/content\_public/journal/tvst/938722/i2164-2591-14-7-8\_1752659133.67454.pdf},
}
```