"""

eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, device=None, like=None)

Return a 2-D array with ones on the diagonal and zeros elsewhere.

 N --> Number of rows
 M --> Number of columns (Optional), default is m=n
 k : int, optional
      Index of the diagonal: 0 (the default) refers to the main diagonal,
      a positive value refers to an upper diagonal, and a negative value
      to a lower diagonal.

"""
import numpy
#help(numpy.eye)
a=numpy.eye(3)
"""
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""
a=numpy.eye(3,4)
"""
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]]

"""

a=numpy.eye(3,4,2,int)
"""
[[0. 0. 1. 0.]
 [0. 0. 0. 1.]
 [0. 0. 0. 0.]]
"""




print(a)
