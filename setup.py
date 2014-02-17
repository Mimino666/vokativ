try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version = __import__('vokativ').__version__

with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()


setup(
    name='vokativ',
    version=version,
    description='Declension of Czech names into vocative case.',
    long_description=readme,
    author='Michal Mimino Danilak',
    author_email='michal.danilak@gmail.com',
    url='https://github.com/Mimino666/vokativ',
    keywords='czech name vocative vokativ jmena ceska',
    packages=['vokativ', 'vokativ.tests'],
    include_package_data = True,
    install_requires=['six'],
    license=license,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Czech',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities',
    ]
)
