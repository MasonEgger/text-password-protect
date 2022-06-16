#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["cryptography"]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Mason Egger",
    author_email="mason@masonegger.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="Protect any text with your own password",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="text_password_protect",
    name="text_password_protect",
    packages=find_packages(
        include=["text_password_protect", "text_password_protect.*"]
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/masonegger/text_password_protect",
    version="0.1.0",
    zip_safe=False,
)
