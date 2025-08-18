"""
Dataframe Introduction
Data fream is a 2-dimensional labeled data structure with columns of potentially different types.
It is similar to a spreadsheet or SQL table, or a dictionary of Series objects.
Pandas DataFrame is generally the most commonly used pandas object.

data frame is heterogeneous, meaning that it can contain different data types in each column.
It is size-mutable, meaning that it can be resized or modified.
It is also potentially heterogeneous, meaning that it can contain different data types in each column.
DataFrame is a two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).
It is generally the most commonly used pandas object.

"""

# create a DataFrame using Python Dictionary
# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
import pandas as pd
name=['Olga','Andrew','Brain','Telulah','Nicole','Tilda']
age=[29,21,45,23,39,46]
married=[False,True,True,True,False,True]
data = {'Name': name, 'Age': age, 'Married': married}      # syntax: {'column_name': data}  we need to use a dictionary to create a DataFrame
df = pd.DataFrame(data)  # create a DataFrame from the dictionary

print("DataFrame created from dictionary:", '\n',df)
print("\nDataFrame shape:", df.shape)  # shape returns a tuple representing the dimensionality of the DataFrame
print("\nDataFrame size:", df.size)  # size returns the number of elements in the DataFrame
print("\nDataFrame dimensions:", df.ndim)  # ndim returns the number of dimensions of the DataFrame
print("\nDataFrame data types:", df.dtypes)  # dtypes returns the data types of each column in the DataFrame
print("\nDataFrame index:", df.index)  # index returns the index of the DataFrame
print("\nDataFrame columns:", df.columns)  # columns returns the column labels of the DataFrame
print("\nDataFrame values:", df.values)  # values returns the data of the DataFrame as a NumPy array
print("\nDataFrame info:", df.info())  # info() returns
