from setuptools import find_packages, setup
from typing import List

# Getting list from requirements.txt

HYPEN_E_DOTT = "-e ."


def get_requrements(file_path: str) -> List[str]:
    """The functions returns List of Requirements

    Args:
        arg_1 (str): Takes File path of text file as string

    Returns:
        List : List containg libraries for installation
    """
    requirements = []

    with open(file_path, "r") as f:
        lines = f.readlines()
        requirements = [line.replace("\n", "") for line in lines]

        if HYPEN_E_DOTT in requirements:
            requirements.remove(HYPEN_E_DOTT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Vikram_Reddy",
    author_email="vikram_viky2001@yahoo.com",
    packages=find_packages(),
    install_requires=get_requrements("requirements.txt")
)
