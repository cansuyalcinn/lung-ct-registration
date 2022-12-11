from pathlib import Path
import SimpleITK as sitk
import cv2 as cv
import pandas as pd
import numpy as np

notebooks_path = Path.cwd()
repo_path = notebooks_path.parent

class patient: #inherit from path_label path and seg functions
    """Class to access patient information
    """
    def __init__(self, num=1) -> None:
        self.pat_num = num #get patient number
    
    def im_path(self, type):
        """get the path of the image given the type (inhale or exhale)

        Args:
            type (char): i or e

        Returns:
            str: path of the image
        """
        return f'data/nifti/copd{self.pat_num}_{type}BHCT.nii.gz'
    
    def im_array(self, type):
        """returns the array of the image given the type (inhale or exhale)

        Args:
            type (char): i or e

        Returns:
            array: image as array
        """
        path = f'data/nifti/copd{self.pat_num}_{type}BHCT.nii.gz'
        return sitk.GetArrayFromImage(sitk.ReadImage(str(repo_path / path)))
    
    def im_sitk(self, type):
        """get sitk image given the type (inhale or exhale)

        Args:
            type (char): i or e

        Returns:
            sitk image: image as sitk image
        """
        path = f'data/nifti/copd{self.pat_num}_{type}BHCT.nii.gz'
        return sitk.ReadImage(str(repo_path / path))
    
    def points_path(self, type, format):
        """get the path of the landmarks given the type (inhale or exhale) and the format (txt or pts)

        Args:
            type (char): i or e
            format (str): txt or pts

        Returns:
            str: path of the landmarks
        """
        return f'data/keypoints/copd{self.pat_num}_300_{type}BH_xyz_r1.{format}'
    
    # Read landmarks 
    def get_landmark(self, type):
        """get the landmarks of the patient

        Args:
            type (str): inhale or exhale (i or e)

        Returns:
            _type_: np.array
        """
        im_path = str(repo_path / self.im_path(type))
        image = sitk.ReadImage(im_path)
        file_path = str(repo_path / self.points_path(type, "txt"))
        x,y,z = image.GetSpacing()
        if type == "i":
            landmark = pd.read_csv(file_path, sep="\t", header=None)
        else:
            landmark = pd.read_csv(file_path, sep="\t ", engine ='python', header=None)
        
        # Multiply spacing to get distance in mm
        landmark = landmark * np.array([x,y,z])

        return np.array(landmark)

            