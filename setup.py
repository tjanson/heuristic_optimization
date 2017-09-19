#!/usr/bin/env python

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


setup(
    name='heuristic_optimization',
    version='0.4.1',
    description='Heuristics for derivative-free optimization',
    long_description=readme,

    url='https://github.com/tjanson/heuristic_optimization',
    author='Tom Janson',
    author_email='tom.janson@rwth-aachen.de',

    license='MIT',

    packages=find_packages(exclude=['examples', 'tests']),

    install_requires=['numpy'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
    ],
)
