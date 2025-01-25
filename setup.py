from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]

    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

author_name =['ABHISHEK UPADHYAY','SHREYA ','NETRA']
author_email_info =['abhishekupadhyay9336@gmail.com','shreya2002pathak@gmail.com','netra01@gmail.com']


setup(
    name='MIMICPROJECT',
    version='0.0.1',
    author=author_name,
    author_email=author_email_info,
    install_require=get_requirements('requirements.txt'),
    packages=find_packages()
)
