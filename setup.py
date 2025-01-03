from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.
    Removes '-e .' if present in the requirements file.
    """
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='How small LLM makes mistakes',
    version='0.0.1',
    author='Guhan',
    author_email='cguhan03@gmail.com',
    description='To understand how small LLm makes mistakes using mechanistic interpretability',
    url='https://github.com/Guhan-C/miniproj.git',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
