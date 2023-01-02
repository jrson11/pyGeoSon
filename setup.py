# Copyright 2023 pyGeoSon Developers
#
# Licensed under the ???

import os
from setuptools import setup, find_packages

# Info
VERSION='0.0.1'
AUTHORS='Jungrak Son, Yichuan Zhu'
DESCRIPTION='A Python Library for Geotechnical Engineering'

# Version

# Long description

# Setting up
setup(
    name="pyGeoSon",
    version=VERSION,
    authour=AUTHORS,
    author_email="jon.jungrak.son@gmail.com",
    description=DESCRIPTION,
    license="GPL, Version 2.0 ???",
    url="https://github.com/jrson11/pyGeoSon.git ???"
    #
    packages=find_packages()
    install_requires=[]
    keywords=['python','civil','geotechnical','engineering','geotechnics','foundation','design','settlement','API','FHWA']
    include_package_data=True,
    python_requires='>=3.6',
)
