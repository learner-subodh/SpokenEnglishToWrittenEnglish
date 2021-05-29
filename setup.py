import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name='SpokenEnglishToWrittenEnglish',
      packages=['ConvertSpokenToWritten'],
      version='1.0.0',
      description='Convert Spoken English using the given text to equivalent Written English ',
      long_description=open_file('README.md').read()
      author='Subodh Lonkar',
      author_email='learner.subodh@gmail.com',
      url='https://github.com/learner-subodh/SpokenEnglishToWrittenEnglish',
      classifiers=[
                    License :: GNU General Public License v3.0,
                    Programming Language :: Python :: 3,
                    Operating System :: OS Independent
  	  ],
)