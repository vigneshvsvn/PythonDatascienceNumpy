"""

"""
from lib2to3.fixes.fix_tuple_params import tuple_name

##########  1. dictionary of tuples
# A dictionary of tuples is a dictionary where each key is associated with a tuple of values.
import pandas as pd
name=['Olga','Andrew','Brain','Telulah','Nicole','Tilda']
age=[29,21,45,23,39,46]
married=[False,True,True,True,False,True]
tuple_name=tuple(name)
tuple_age=tuple(age)
tuple_married=tuple(married)
data = {'Name': tuple_name, 'Age': tuple_age, 'Married': tuple_married}  # syntax: {'column_name': data}  we need to use a dictionary to create a DataFrame
df = pd.DataFrame(data)  # create a DataFrame from	the dictionary

##########  2. dictionary of series
# A dictionary of series is a dictionary where each key is associated with a pandas Series object.
name_series = pd.Series(name)
age_series = pd.Series(age)
married_series = pd.Series(married)
data_series = {'Name': name_series, 'Age': age_series, 'Married': married_series}  # syntax: {'column_name': data}  we need to use a dictionary to create a DataFrame
df_series = pd.DataFrame(data_series)  # create a DataFrame from the dictionary of series

########## 3. dictionary of dictionaries
# A dictionary of dictionaries is a dictionary where each key is associated with another dictionary.
# enumerate() is used to get the index and value of each element in the list.
# example: enumerate(['a', 'b', 'c']) returns [(0, 'a'), (1, 'b'), (2, 'c')]
# Here, we use enumerate to create a dictionary where the keys are the indices of the elements
# and the values are the elements themselves.
dict_name={k:v for k,v in enumerate(name)}
dict_age={k:v for k,v in enumerate(age)}
dict_married={k:v for k,v in enumerate(married)}
data_dict = {'Name': dict_name, 'Age': dict_age, 'Married': dict_married}  # syntax: {'column_name': data}  we need to use a dictionary to create a DataFrame
df_dict = pd.DataFrame(data_dict)  # create a DataFrame from the dictionary of dictionaries

########## 3. using a list of dictionaries
# A list of dictionaries is a list where each element is a dictionary.
# Each dictionary represents a row in the DataFrame.
data_list_of_dicts = [
	{'Name': 'Olga', 'Age': 29, 'Married': False},
	{'Name': 'Andrew', 'Age': 21, 'Married': True},
	{'Name': 'Brain', 'Age': 45, 'Married': True},
	{'Name': 'Telulah', 'Age': 23, 'Married': True},
	{'Name': 'Nicole', 'Age': 39, 'Married': False},
	{'Name': 'Tilda', 'Age': 46, 'Married': True}
]
df_list_of_dicts = pd.DataFrame(data_list_of_dicts)  # create a DataFrame from the list of dictionaries

## what is the use of zip() function?
# The zip() function is used to combine multiple iterables (like lists or tuples) into a single iterable of tuples.
# Each tuple contains one element from each of the input iterables,
# effectively pairing them together based on their positions.
# For example, zip(['a', 'b', 'c'], [1, 2, 3]) would produce an iterable of tuples: [('a', 1), ('b', 2), ('c', 3)].
# This is useful for creating DataFrames from multiple lists or tuples,
# as it allows you to pair corresponding elements together into rows.	




