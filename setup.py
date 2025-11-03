from __future__ import annotations

from pathlib import Path

from setuptools import find_packages
from setuptools import setup

from version import __version__ as package_version


project_root = Path(__file__).parent
install_requires = (project_root / 'requirements.txt').read_text().splitlines()

setup(
    name='project_poki',
    version=package_version,
    description='Collection of tools for analysis and processing of Toki Pona language.',
    author='BaronVladziu',
    url='https://github.com/BaronVladziu/Project-Toki',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    long_description=(project_root / 'README.md').read_text(),
    long_description_content_type='text/markdown',
)
