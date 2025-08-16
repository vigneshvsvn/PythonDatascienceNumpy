""""
Series is a one-dimensional labeled array capable of holding any data type.
It is similar to a list or a dictionary, but with additional features like indexing and data alignment.
You can create a Series from various data structures such as lists, dictionaries, or NumPy arrays.

"""
import pandas as pd
# Creating a Series from a list
data = [10, 20, 30, 40]
series_from_list = pd.Series(data)
print("Series from list:",type(series_from_list))
print(series_from_list)

# Creating a Series from a dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
series_from_dict = pd.Series(data_dict)
print("\nSeries from dictionary:",type(series_from_dict))
print(series_from_dict)

# Creating a Series from a NumPy array
import numpy as np
data_array = np.array([1, 2, 3, 4])
series_from_array = pd.Series(data_array)
print("\nSeries from NumPy array:",type(series_from_array))
print(series_from_array)
