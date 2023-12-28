from setuptools import find_packages, setup
from typing import List


HHPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HHPEN_E_DOT in requirements:
            requirements.remove(HHPEN_E_DOT)
    return requirements


setup(
    name = 'StudentPerformance',
    version = '0.0.1',
    author = 'Marius',
    author_email = 'hoohoo987ry@gmail.com',
    packages = find_packages(),
    install_requieres = get_requirements('requirements.txt')
)