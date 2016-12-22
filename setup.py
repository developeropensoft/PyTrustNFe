# coding=utf-8
from setuptools import setup, find_packages

VERSION = "0.1.14"

setup(
    name="PyTrustNFe",
    version=VERSION,
    author="Danimar Ribeiro",
    author_email='danimaribeiro@gmail.com',
    keywords=['nfe', 'mdf-e'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or \
later (LGPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=['*test*']),
    package_data={'pytrustnfe': ['nfe/templates/*xml',
                                 'nfse/paulistana/templates/*xml']},
    url='https://github.com/danimaribeiro/PyTrustNFe',
    license='LGPL-v2.1+',
    description='PyTrustNFe é uma biblioteca para envio de NF-e',
    long_description=open('README.md', 'r').read(),
    install_requires=[
        'Jinja2 >= 2.8',
        'signxml >= 2.0.0',
        'lxml >= 3.6.0, < 3.7',
        'suds >= 0.4',
        'suds_requests >= 0.3',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock',
    ],
)
