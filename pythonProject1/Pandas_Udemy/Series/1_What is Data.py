"""

"""
import pandas as pd
book_list=['Python for Data Analysis', 'Python Cookbook', 'Fluent Python', 'Effective Python']
book_series=pd.Series(book_list)
print("Book Series:")
print(book_series)

pd.Series(10) # Creating a Series with a single value
pd.Series([10, 20, 30]) # Creating a Series from a list of values
pd.Series({'a': 1, 'b': 2, 'c': 3}) # Creating a Series from a dictionary
pd.Series([1, 2, 3], index=['a', 'b', 'c']) # Creating a Series with custom index labels
pd.Series([1, 2, 3], dtype='float64') # Creating a Series with a specific data type
pd.Series([1, 2, 3], name='My Series') # Creating a Series with a name
pd.Series([1, 2, 3], index=[0, 1, 2], dtype='int64', name='My Series with Index') # Creating a Series with index, data type, and name
pd.Series([1, 2, 3], index=[0, 1, 2], dtype='int64', name='My Series with Index and Name') # Creating a Series with index, data type, and name
pd.Series([1, 2, 3], index=[0, 1, 2], dtype='int64', name='My Series with Index, Data Type, and Name') # Creating a Series with index, data type, and name
pd.Series([1, 2, 3], index=[0, 1, 2], dtype='int64', name='My Series with Index, Data Type, and Name') # Creating a Series with index, data type, and name
pd.Series([1, 2, 3], index=[0, 1, 2], dtype='int64', name='My Series with Index, Data Type, and Name') # Creating a Series with index, data type, and

