# LRGpy

LRGpy is a collection of Python code used by the Lattanzi Research Code at George Mason University. This package currently consists of point cloud utilities derived from research papers, CloudCompare utilities, and PCL functions.

## Installation

Run the following to install:

```python
pip install LRGpy
```

## Usage

Example usage

Generate a point cloud from a CloudCompare generated text file:

```python
# Import the entire LRGpy module:
import LRGpy

cloud = LRGpy.PointCloudFromTxt("./cloud.txt")
```

```python
# Alternatively, import just one function into your own namespace:
from LRGpy import PointCloudFromTxt

cloud = PointCloudFromTxt("./cloud.txt")
```
