from pathlib import Path
import SimpleITK as sitk

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