"""
info() method in Pandas DataFrame
The info() method in Pandas DataFrame provides a concise summary of the DataFrame, including
the index dtype and columns, non-null values, and memory usage. It is useful for quickly
understanding the structure and contents of a DataFrame, especially when dealing with large datasets.
It displays the following information:
- The class type of the DataFrame
- The range of the index
- The number of columns and their names
- The data type of each column
"""

import pandas as pd
name=['Olga','Andrew','Brain','Telulah','Nicole','Tilda']
age=[29,21,45,23,39,46]
married=[False,True,True,True,False,True]
tuple_name=tuple(name)
tuple_age=tuple(age)
tuple_married=tuple(married)
data = {'Name': tuple_name, 'Age': tuple_age, 'Married': tuple_married}  # syntax: {'column_name': data}  we need to use a dictionary to create a DataFrame
df = pd.DataFrame(data)  # create a DataFrame from	the dictionary
print("DataFrame created from dictionary of tuples:", '\n', df)
print("\nDataFrame info:")
df.info()  # info() provides a concise summary of the DataFrame, including index dtype


# In general, what is meant by verbose?
# Verbose means providing more detailed or extensive information. In the context of the info() method
# in Pandas, setting verbose=True means that the method will display more detailed information about the
# DataFrame, such as the number of non-null values in each column, the data types of each column, and the memory usage.
# Setting verbose=False will provide a more concise summary,
# showing only the basic information about the DataFrame, such as the index dtype and columns.
df.info(verbose=True)  # verbose=True provides more detailed information about the DataFrame
df.info(verbose=False)  # verbose=False provides less detailed information about the DataFrame

print("###########Memery Usage###########")
## memory_usage # The memory_usage parameter in the info() method specifies whether to display the memory usage of each column in the DataFrame.
# If memory_usage=True, it will show the memory usage of each column in bytes.
# If memory_usage=False, it will not display the memory usage.
df.info(memory_usage=True)  # memory_usage=True displays the memory usage of each column in the DataFrame
df.info(memory_usage=False)  # memory_usage=False does not display the memory
# usage of each column in the DataFrame
df.info(memory_usage='deep')  # memory_usage='deep' provides a more detailed memory usage report, including the memory usage of object dtype columns	