#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import setuptools
import versioneer


with open("README.md", "r") as myfile:
    long_description = myfile.read()

setuptools.setup(
    name="auto_ovpn_profiles",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Jorge Sacristan",
    author_email="j.sacris@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jsacrist/auto_ovpn_profiles",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3",
                 "License :: GPLv3 License",
                 "Operating System :: OS Independent", ],
    install_requires=["pyyaml>=3.11", "jinja2>=2.10"]
)
