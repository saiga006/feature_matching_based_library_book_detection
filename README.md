# Feature Matching Based Library Book Detection
This repository contains relevant code, research paper and the dataset for my bachelor thesis project (2018) on feature matching based library book detection system

# Paper Title:Feature Matching Based Book Detection System

## Abstract
> Finding a particular book from a large stack in a 
library is a difficult and time consuming task. Library users need 
to search the entire stack all by themselves and this is not a simple 
job. To reduce their strain and guide them in accessing the book 
they want, an autonomous system for book detection is proposed. 
This paper is all about the identification of user queried book from 
a huge collection of books in the library stack in an efficient way. 
The book to be detected is found by using image processing 
techniques like feature extraction and feature matching methods. 
It involves maintaining a separate database of book spine images 
locally and comparing the existing features of the queried book 
with the features present in the test image. DoG key point detector 
and RootSIFT feature descriptor are used to find the maximum 
likeliness between the queried and test image. The algorithm 
applied is an accurate method as it proves to be scale, affine and 
illumination invariant and can also be deployed easily in real-time 
at minimal cost.

## Evaluation Results
- **Datasets:** Around 150 images of different book spine were gathered with resized to fixed height of 720 pixels. Around 50 images of test dataset was used while evaluating the real time implementation.
- **Accuracy:** [Insert results, e.g., 92% correct matches]
- **Speed:** [Insert relevant timing or efficiency results]
- **Comparison:** Outperforms [baseline/alternative] in [specific aspect], with [quantitative results].

## Video

[Provide a link to a demonstration or explanatory video.]

- [Watch the demonstration video](https://your-video-link)

## Repository Contents

- `paper.pdf`: Full research paper
- `results/`: Evaluation results and supplementary data
- `video/`: (Optional) Video files or links
- `README.md`: This file

## Citation

If you use this work, please cite:
```bibtex
@inproceedings{FeatureMatchingBookDetection,
title={Feature Matching Based Book Detection System},
authors={Sai Mukkundan R, Melvin A, Shoban Chander E and Dr.V.Sathiesh Kumar },
booktitle={3rd International Conference on Recent Trends in Engineering and Technology(ICRTET-18)},
year={2018}
}
```
