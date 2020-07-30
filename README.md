# LRGpy

LRGpy is a collection of Python code used by the Lattanzi Research Code at George Mason University. This package currently consists of point cloud utilities that are custom implementations of research papers, PCL functions, and CloudCompare utilities.

## Installation

Run the following to install:

```python
pip instal LRGpy
```

## Example Usage

```python
# Import entire LRGpy module:
import LRGpy

# Generate PointCloud from CloudCompare txt
LRGpy.PointCloudFromTxt("./cloud.txt")
```

```python
# Alternatively, import one function into your own namespace:
from LRGpy import PointCloudFromTxt

# Generate PointCloud from CloudCompare txt
PointCloudFromTxt("./cloud.txt")
```
