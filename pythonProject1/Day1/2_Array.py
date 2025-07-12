"""
Array: Indexed collection of homogeneous (same datatype) data elements.

We don't have inbuilt concepts in python.

Ways:
1. By using array module not recommended to use. As many libraries don't support this.
2. By using numpy module (recommended)

Python List vs Numpy nd Array:
******************************
	Similarity:
		- Both can be used to store data.
		- Order will be preserved in Both
		- Index and slice is possible as it's ordered
		- Both are Mutable
	Difference:
		- List is inbuilt in python, but for Array we need to use external library like numpy
		- List Heterogeneous but array is only  homogeneous elements.
		- On List we can't perform Vector operations but in nd array we can.
		- Array consume less memory than list
		- arrays are fast compare to list
			

"""
import array,numpy

# using array library
a=array.array('i',[10,20,30])  # i represents int array
print(type(a))
print(a)
for x in a:
	print(type(x),':',x)

## using Numpy
a=numpy.array([10,20,30])
print(type(a))
print(a)
for each in a:
	print(each)