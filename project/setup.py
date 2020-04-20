import os

from setuptools import setup, find_packages

setup(
    name='weasyprint-server',
    version=os.environ.get('GIT_BUILD_VERSION', 'unkown'),
    description='Weasyprint Server',
    author='mecodia GmbH',
    author_email='it@mecodia.de',
    packages=find_packages(),
    install_requires=[
        'WeasyPrint(==51)',
        'flask(~=1.0)',
    ],
)
