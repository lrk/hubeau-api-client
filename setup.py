# https://github.com/pypa/sampleproject/blob/master/setup.py
import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='hubeau-api-client',
    version='1.0.0',
    description='Hubeau Rest API Client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lrk/hubeau-api-client',
    author='Lrk',
    author_email='sfxelrick@gmail.com',
    # classifiers=[
    #     'Development Status :: 3 - Alpha',
    #     'Intended Audience :: Developers',
    #     'Topic :: Software Development :: Build Tools',
    #     'License :: OSI Approved :: MIT License',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.5',
    #     'Programming Language :: Python :: 3.6',
    #     'Programming Language :: Python :: 3.7',
    #     'Programming Language :: Python :: 3.8',
    #     'Programming Language :: Python :: 3 :: Only',
    # ],
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
