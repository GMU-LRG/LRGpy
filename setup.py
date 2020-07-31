from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
  name='LRGpy',
  version = '0.0.1',
  description = 'LRG Python code repsository.',
  url='https://github.com/GMU-LRG/LRGpy',
  author='Lattanzi Research Group',
  author_email='dlattanz@gmu.edu',
  long_description=long_description,
  long_description_content_type='text/markdown',
  package_dir={'': 'src'},
  classifiers=[
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Topic :: Scientific/Engineering'
  ],
  #dependencies
  install_requires = [
    'scikit-learn',
    'matplotlib'
  ]
)

