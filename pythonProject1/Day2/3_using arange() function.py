"""
arange() --> always generate 1D array. We have some other options to convert shape and lamentations

"""

import numpy as np
# example 1
a=np.arange(10)
print("Example1:",type(a),a)
a=np.arange(1,11,3,dtype=float)
print("Example1 with steps:",a)

""""
Example1: <class 'numpy.ndarray'> [0 1 2 3 4 5 6 7 8 9]
Example1 with steps: [ 1.  4.  7. 10.]
"""

