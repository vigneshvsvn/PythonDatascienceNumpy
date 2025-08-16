import pandas as pd
import matplotlib
# Read a CSV file into a Series
# The 'usecols' parameter specifies which columns to read, and 'index_col' sets the index
# The resulting Series will have 'country' as the index and 'wine_servings' as the values
# The 'squeeze' function is not needed here as we are directly selecting a single column
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print(alcohol.mode())  # Mode of the series. what is mode? The mode is the value that appears most frequently in a dataset. Example: In the series [1, 2, 2, 3], the mode is 2 because it appears more frequently than the other values.
# print(alcohol.mode(dropna=False))  # Mode including NaN values
# print(alcohol.value_counts())  # Count of unique values in the series
print(alcohol.value_counts(normalize=True))  # Relative frequency of unique values what is relative frequency? Relative frequency is the ratio of the frequency of a particular value to the total number of values in the dataset. It is often expressed as a percentage or fraction. Example: If a value appears 5 times in a dataset of 100 values, its relative frequency is 5/100 = 0.05 or 5%.
# print(alcohol.value_counts(dropna=False))  # Count of unique values including NaN
# print(alcohol.value_counts(normalize=True, dropna=False))  # Relative frequency including Na