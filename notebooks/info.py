from pathlib import Path
import SimpleITK as sitk
import cv2 as cv

notebooks_path = Path.cwd()
repo_path = notebooks_path.parent

class patient: #inherit from path_label path and seg functions
    """Class to access patient information
    """
    def __init__(self, num=1) -> None:
        self.pat_num = num #get patient number
    
    def path(self, type):
        return f'data/nifti/copd{self.pat_num}_{type}BHCT.nii.gz'
    
    def im_array(self, type):
        path = f'data/nifti/copd{self.pat_num}_{type}BHCT.nii.gz'
        return sitk.GetArrayFromImage(sitk.ReadImage(str(repo_path / path)))
    def im_sitk(self, type):
        path = f'data/nifti/copd{self.pat_num}_{type}BHCT.nii.gz'
        return sitk.ReadImage(str(repo_path / path))
        