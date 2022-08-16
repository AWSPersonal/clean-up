"""
    Setup
"""

from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup_info = {
    "name": "AWS Clean Up Tool",
    "version": "1.0",
    "packages": ["utils", "services"],
    "url": "https://github.com/AWSPersonal/clean-up/",
    "license": "",
    "author": "Manjunath PV",
    "author_email": "manjunathpv@outlook.com",
    "description": "",
    "install_requires": required,
}

if __name__ == "__main__":
    setup(**setup_info)
