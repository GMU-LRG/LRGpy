from setuptools import setup

setup(
  name="LRGpy",
  version = "0.0.1",
  description = "LRG Python code repsository.",
  long_description="A Python module containing various useful Python code owned by LRG.",
  py_modules=["LRGpy"],
  package_dir={"": "src"},
  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "Topic :: Scientific/Engineering"
  ]
)
