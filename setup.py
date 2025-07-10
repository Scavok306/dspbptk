#!/usr/bin/env python
from setuptools import setup, find_packages

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dspbptk",
    version="0.1.0",
    author="John Doe",
    author_email="john.doe@example.com",
    description="Dyson Sphere Program Blueprint Parsing Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johndoe31415/dspbptk",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here if needed
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)