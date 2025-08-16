"""
Both dropping NaN values and filling NaN values are common operations in data preprocessing.
Dropping NaN values removes any rows that contain NaN values, which can be useful when
you want to ensure that your data is clean and complete for analysis.
Filling NaN values replaces them with a specified value, such as 0, which can be useful when
you want to retain all rows in your dataset but need to handle missing values in a specific way.

It will be a copy of the Series with NaN values removed.
"""

import pandas as pd

# Read a CSV file into a Series
# The 'usecols' parameter specifies which columns to read, and 'index_col' sets the index
# The resulting Series will have 'country' as the index and 'wine_servings' as the values
# The 'squeeze' function is not needed here as we are directly selecting a single column
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print(alcohol.dropna())  # Drop all rows with NaN values in the Series

print(alcohol.fillna(0))  # Fill NaN values with 0 in the Series