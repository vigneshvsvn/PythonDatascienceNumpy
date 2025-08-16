"""
iloc is used to access a group of rows and columns by integer position(s).
It is primarily used for integer-location based indexing, allowing you to select rows and columns by their integer index positions rather than labels.
This is particularly useful when you want to access specific rows or columns based on their numerical index rather than their labels.
It is commonly used in data manipulation and analysis tasks
where you need to work with specific rows or columns in a DataFrame or Series based on their integer positions.

"""
from string import ascii_lowercase,ascii_uppercase
import pandas as pd
list_alphabet_lower=list(ascii_lowercase)
list_alphabet_upper=list(ascii_uppercase)
alphabet_series=pd.Series(list_alphabet_lower,name='Alphabet',index=list_alphabet_upper).add_prefix('Lable_')

print(alphabet_series.iloc[0])  # Accessing the first element by integer position
print(alphabet_series.iloc[1:3])  # Accessing a range of elements by integer positions
print(alphabet_series.iloc[[0, 2, 4]])  # Accessing specific elements by integer positions
print(alphabet_series.iloc[-1])  # Accessing the last element
print(alphabet_series.iloc[-3:])  # Accessing the last three elements
