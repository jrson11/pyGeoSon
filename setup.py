# Copyright 2023 pyGeoSon Developers
#
# Licensed under the ???

from setuptools import setup, find_packages


setup(
    name="pyGeoSon",
    version='0.0.1',
    authour="Jungrak Son, Yichuan Zhu"
    author_email="jon.jungrak.son@gmail.com",
    description="A Python Library for Geotechnical Engineering",
    license="GPL, Version 2.0 ???",
    url="https://github.com/jrson11/pyGeoSon.git ???"
    #
    packages=find_packages()
    include_package_data=True,
    python_requires='>=3.6',
)
