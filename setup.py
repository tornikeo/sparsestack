#!/usr/bin/env python
import os
from setuptools import find_packages, setup


here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(here, "stacked-sparse-array", "__version__.py")) as f:
    exec(f.read(), version)

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name="matchms",
    version=version["__version__"],
    description="Python library for to build and handle stacks of sparse COO arrays efficiently",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Florian Huber",
    author_email="florian.huber@hs-duesseldorf.de",
    url="https://github.com/florian-huber/stacked-sparse-array",
    packages=find_packages(exclude=['*tests*']),
    package_data={"stacked-sparse-array": ["data/*.csv"]},
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    python_requires='>=3.7',
    install_requires=[
        "numpy",
        "scipy",
    ],
    extras_require={"dev": ["bump2version",
                            "decorator",
                            "isort>=5.1.0",
                            "pylint<2.12",
                            "prospector[with_pyroma]",
                            "pytest",
                            "pytest-cov",
                            "sphinx>=4.0.0",
                            "sphinx_rtd_theme",
                            "sphinxcontrib-apidoc",
                            "testfixtures",
                            "yapf",]},
)
