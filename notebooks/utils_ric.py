from pathlib import Path
import SimpleITK as sitk
import pickle
import numpy as np

notebooks_path = Path.cwd()
repo_path = notebooks_path.parent

def getArrayfromPath(image_path):
    """Simply get array of image

    Args:
        image_path (str): image path

    Returns:
        array: array of the image
    """
    return sitk.GetArrayFromImage(sitk.ReadImage(image_path))

def save_pickle(obj, path):
    """Save object as pickle

    Args:
        obj (object): object to save
        path (str): path to save object
    """
    with open(path, 'wb') as handle:
        pickle.dump(obj, handle, pickle.HIGHEST_PROTOCOL)

def open_pickle(path):
    """Open pickle

    Args:
        path (str): path to pickle

    Returns:
        object: object in pickle
    """
    with open(path, 'rb') as handle:
        return pickle.load(handle)
    
# Calculate TRE
def calculate_tre(fixed_points, moving_points):
    """Compute TRE
    
    args:
        fixed_points (np.array): fixed points
        moving_points (np.array): moving points
    returns:
        tre (np.array): TRE
    
    """
    tre = np.sqrt(np.sum((fixed_points - moving_points) ** 2, axis=1))
    return tre

# save the array as a new nifti image
def save_as_nifti(array, filename, reference_image):
    """Save array as nifti image

    Args:
        array (array): array to be saved
        filename (str): path to save
        reference_image (str): path of reference image
    """
    reference_image = sitk.ReadImage(reference_image)
    image = sitk.GetImageFromArray(array)
    image.SetOrigin(reference_image.GetOrigin())
    image.SetSpacing(reference_image.GetSpacing())
    image.SetDirection(reference_image.GetDirection())
    sitk.WriteImage(image, filename)