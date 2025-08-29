from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    this functionn will return requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()
            if req and req != HYPEN_E_DOT:
                requirements.append(req)
    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    author='krishnav',
    author_email='talukdarkrishnav9@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
