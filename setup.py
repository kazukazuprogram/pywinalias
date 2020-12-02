#!/usr/bin/env python3
# coding: utf-8

from setuptools import setup, find_packages
from os import environ, mkdir
from os.path import join, isdir

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""


def setup_enviroment():
    dir = join(environ["HOMEDRIVE"], environ["HOMEPATH"], ".alias")
    if not isdir(dir):
        mkdir(dir)


setup(
    name="pywinalias",
    version="0.0.0",
    description="A pip package",
    license="MIT",
    author="kazukazuprogram",
    packages=find_packages("src"),
    package_dir={
        "pywinalias": "src\\pywinalias"
    },
    package_data={
        "pywinalias": ["src\\pywinalias\\template.bat"]
    },
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        'console_scripts': [
            'alias = pywinalias.__main__:main',
        ],
    },
    include_package_data=True,
)

setup_enviroment()
