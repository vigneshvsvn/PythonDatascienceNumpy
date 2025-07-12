"""
Need of Numpy:
- Numpy Developed based on Numeric Libraray
Numeric Library --> by Jim Huguin
Numpy --> developed by Trvis Oliphant and other contributors in 2005.  Using c and Python

- To Perform complex sevaral mathematical Operations.
	Eg: Linear algebra, integral, stati
- To fullFill performance gaps in python
	Most of the numpy implemented in c Language
	superfast
- nd array is a data structure.
	N dimensional array or numpy array
	numpy acts a backbone for remaining libraries as well (Pandas, matplotlib...) as it's developed on top of numpy


Array:
- arrays are Object of ndarray class present in numpy Module.
- An indexed collection of homogeneous elements
one dimensional arrays are Vector
tow dimensional arrays are Matrix

Installing numpy
Way 1 by Anaconda: is the flavor of python specifically for datascience.
Way 2 : pip install numpy

"""
from datetime import datetime

import numpy as np

a=[10,20,30]
b=[1,2,3,4]

## Traditional Python
def dot_product(a,b):
	result=0
	for i,j in zip(a,b):
		#print(i,j)
		result=result + i*j
	return result

before=datetime.now()
for i in range(10000000):
	dot_product(a,b)
after=datetime.now()

print("Time taken by traditional python", after-before)

### using numpy library
a=np.array([10,20,30])
b=np.array([1,2,3])

before=datetime.now()
for i in range(10000000):
	np.dot(a,b)
after=datetime.now()
print("Time taken by numpy", after-before)

