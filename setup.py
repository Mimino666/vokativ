# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import io

with io.open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='vokativ',
    version='1.2.1',
    description='Declension of Czech names into vocative case.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Michal Mimino Danilak',
    author_email='michal.danilak@gmail.com',
    url='https://github.com/Mimino666/vokativ',
    keywords='czech name vocative vokativ jmena ceska',
    packages=['vokativ', 'vokativ.tests'],
    include_package_data=True,
    install_requires=['six'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Czech',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ]
)
