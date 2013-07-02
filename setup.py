from setuptools import setup
import os
from turnapi import __version__

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

packages = ['turnapi']

setup(
    name='django-turnapi',
    version=__version__,
    description= "TURN Server API for Django",
    long_description=read("README.rst"),
    keywords='django, turn, rfc5766,',
    author='Patrick Marques',
    author_email='patrickfmarques@gmail.com',
    url='http://github.com/pmarques/django-turnapi',
    license='MIT',
    packages=packages,
    zip_safe=False,
    install_requires=['redis>=2.4.10'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
