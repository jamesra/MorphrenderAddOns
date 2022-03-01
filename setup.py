'''
Created on March 1, 2022

@Author: RLPfeiffer
'''

from ez_setup import use_setuptools


if __name__=='main':
    use_setuptools()
    from setuptools import setup, find_packages

    packages = find_packages()

    install_requires= ["pymeshlab"]

    classifiers = ['Programming Language :: Python :: 3.7',
                   'Topic :: Scientific/Engineering']

    setup(name = 'morphrender_addons',
        version = '1.0',
        description= "MeshLab filters for dae files",
        author =' Rebecca Pfeiffer',
        author_email= "r.pfeiffer@utah.edu",
        url = 'https://github.com/RLPfeiffer/MorphrenderAddOns',
        install_requires=install_requires,
        packages=packages)