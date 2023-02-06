# Lung CT Registration Challenge

The challenge was the final project of the Medical image registration course given in the University of Girona for the [MAIA programme](https://maiamaster.udg.edu/).
The final report can be found [here](MIRA_FINAL_REPORT.pdf).

## Authors of the project 
- Ricardo Montoya Del Angel [github](https://github.com/Likalto4) | [linkedin](https://www.linkedin.com/in/ricardo-montoya-del-angel)

- Cansu Yalçın [github](https://github.com/cansuyalcinn) | [linkedin](www.linkedin.com/in/cansuyalcin)

- Alex Chicano [linkedin](https://www.linkedin.com/in/%C3%A0lex-chicano-83291a148/)

**During the challenge day proposed solution ranked the 2nd place obtaining mean TRE value of  1,4223 mm across test patients**

## Challenge description 

We have performed non-rigid image registration on the Lung CT images taken from the Chronic obstructive pulmonary disease (COPD) [4DCT DIR-Lab Challenge](https://med.emory.edu/departments/radiation-oncology/research-laboratories/deformable-image-registration/index.html) dataset. The dataset contains inhale, and exhale images, as well as their landmarks corresponding to the same patient. The aim of the project is register both inhale and exhale images, and to measure the performance using the landmark point positions after registration. Target registration error (TRE) is used as a metric to determine the accuracy of the calculated landmark positions.

The pipeline inluded:
- Preprocessing step (changing the orientation of the images and convertion to NIFTI format), 
- Segmentation step (using automated U-net segmentation tool for the lung CT images reference: [lungmask](https://github.com/JoHof/lungmask), 
- Registration (Affine (rigid), B-spline (non-rigid), compositon (Affine → B-spline))





