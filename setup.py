import sys
from setuptools import setup, find_packages

requires = [
    'selenium',
    'argparse',
]

setup(
    name='bizleaker',
    description=("Extracts names from phone numbers through Bizum."),
    version='1.0',
    install_requires=requires,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['bizleaker=bizleaker.app:main'],
    },
    long_description=open('README.md').read(),
    keywords=['bizum', 'phone', 'telephone']
)
