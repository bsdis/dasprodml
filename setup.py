'''Setup script for lasio'''

from setuptools import setup

from os import path

from dasprodml import __version__


with open(path.join(path.dirname(__file__), "requirements.txt"), "r") as f:
    requirements = f.read().splitlines()

setup(name='dasprodml',
      version=__version__,
      description="Read/write DAS data from PRODML files",
      long_description=(
          'This is a Python 3.5+ package to read and write PRODML '
          'files, used for Distributed Accoustic Sensing (DAS) data. '
          'It\'s an implementation of the energistics standard PRODML v2.0 '
          'which may be found here: http://www.energistics.org/production/prodml-standards/current-standards '
          'The standard is very new and can be complex to get up and running, so this library is meant to '
          'be a help to be able to quickly read and write PRODML data and understand how the standard may be '
          'used in a practical setting.\n\n'
          'See https://github.com/bsdis/dasprodml for more details.'),
      url="https://github.com/bsdis/dasprodml",
      author="Bjørn Dissing and Yevgheni Petkevich",
      author_email="bjorn.dissing@bitsort.io",
      license="MIT",
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Environment :: Console",
          "Environment :: Web Environment",
          "Environment :: Other Environment",
          "Intended Audience :: Customer Service",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: End Users/Desktop",
          "Intended Audience :: Other Audience",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Topic :: Scientific/Engineering",
          "Topic :: System :: Filesystems",
          "Topic :: Scientific/Engineering :: Information Analysis",
      ],
      keywords="science geophysics io",
      packages=["dasprodml", ],
      install_requires=requirements,
      entry_points={
          'console_scripts': [
          ],
      }
)
