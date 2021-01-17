# https://github.com/pypa/sampleproject/blob/master/setup.py
import pathlib
import os.path

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='hubeau-api-client',
    version=get_version('src/api/__init__.py'),
    description='Hubeau Rest API Client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lrk/hubeau-api-client',
    author='Lrk',
    author_email='sfxelrick@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Natural Language :: French',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='hubeau, api, rest',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=['requests'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/lrk/hubeau-api-client/issues',
        'Source': 'https://github.com/lrk/hubeau-api-client'
    }
)
