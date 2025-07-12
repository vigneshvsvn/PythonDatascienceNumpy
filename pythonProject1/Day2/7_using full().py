import numpy

a=numpy.full((1,1,2,4),fill_value=10,dtype=int)
print(a)
"""
[[[[10 10 10 10]
   [10 10 10 10]]]]
"""

a=numpy.full((2,4),fill_value=10,dtype=int)
print(a)

"""
[[10 10 10 10]
 [10 10 10 10]]
"""