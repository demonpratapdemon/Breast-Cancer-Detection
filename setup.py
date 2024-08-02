from setuptools import setup, find_packages
from typing import List

hyphen_e_dot = '-e .'

def read_requirements(filepath : str)->List[str]:
    requirements = []
    
    with open(filepath) as f:
        requirements = f.readlines()
        
    requirements = [req.replace('\n', '')  for req in requirements]
    
    if hyphen_e_dot in requirements:
        requirements.remove(hyphen_e_dot)

    return requirements


setup(
    name='Breast Cancer Prediction',
    version='0.1',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    author='Pratap Kumar Chandra',
    author_email='pratapkumar.chandra@yahoo.com',
    description='Prediction of Tumour being Malignant or Benign',
    url='https://github.com/demonpratapdemon/Breast-Cancer-Detection',
)