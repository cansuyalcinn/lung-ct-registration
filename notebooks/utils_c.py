# Import Libraries
import os
from pathlib import Path
import numpy as np
import pandas as pd
import SimpleITK as sitk
import matplotlib.pyplot as plt
from tqdm import tqdm
import pickle


def get_landmark(p, i):
    """get the landmarks of the patient

    Args:
        p (str): inhale or exhale (i or e)
        i (int): patient number

    Returns:
        _type_: pandas dataframe
    """
    image = sitk.ReadImage(f"../data/nifti/copd{i}_{p}BHCT.nii.gz")
    file= f"../data/keypoints/copd{i}_300_{p}BH_xyz_r1.txt"
    x,y,z = image.GetSpacing()
    if p == "i":
        landmark = pd.read_csv(file, sep="\t", header=None)
    else:
        landmark = pd.read_csv(file, sep="\t ", header=None)
    
    # Multiply spacing to get distance in mm
    landmark = landmark * np.array([x,y,z])

    return np.array(landmark)

get_landmark(p="i", i=1)


def get_data(p,i):
    """ Args:
        p (str): inhale or exhale (i or e)
        i (int): patient number
    """
    image = sitk.ReadImage(f"../data/nifti/copd{i}_{p}BHCT.nii.gz")
    landmark = f"../data/keypoints/copd{i}_300_{p}BH_xyz_r1.txt"
    return image, landmark

def get_data_paths(p,i):
    """ Args:
        p (str): inhale or exhale (i or e)
        i (int): patient number
    """
    image_p = f"../data/nifti/copd{i}_{p}BHCT.nii.gz"
    landmark_p = f"../data/keypoints/copd{i}_300_{p}BH_xyz_r1.txt"
    return image_p, landmark_p