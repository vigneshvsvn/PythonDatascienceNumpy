"""
when to go for array()
For a given list or tuple if we want to create an array, we need to go for array()

"""

import numpy as np
#help(np.array)

## 1D array
l1=[10,20,30]
a=np.array(l1)        ## 1D is only row
print(type(a))
print(a)
print(a.ndim)    ## To check what dimensional array it is. like one  dimensional, two dimensional..
print(a.dtype)   ## To check data type for array elements
print(a.shape)

## 2D array
l2=[[10,20,30,4],[30,40,50,4],[30,40,60,4]]
b=np.array(l2)
print(b.ndim) # 2D, only rows and columns
print(b.shape)  # shape of array  3 row and 3 columns   (3,3) (rows,column)
print(b.size)   # 9 elements in the array


print(np.array([10,30,30.5],dtype=str))  ## dtype is to convert to required type when heterogeneous elements.




