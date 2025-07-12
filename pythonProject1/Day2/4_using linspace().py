"""
 In specified interval, linearly spaced value
 Eg: In range 0 to  1  we need 4 values 

"""

import numpy

a=numpy.linspace(1,10,num=4)
print(a)
"""
[ 1.  4.  7. 10.]
"""

a=numpy.linspace(1,100,num=5)
print(a)
"""
[  1.    25.75  50.5   75.25 100.  ]
"""