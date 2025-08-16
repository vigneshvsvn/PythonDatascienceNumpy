from sys import prefix

import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print("Index of maximum value in series:", alcohol.idxmax())  # Index of the first occurrence of the maximum value
print("Index of minimum value in series:", alcohol.idxmin())  # Index of the first occurrence of the minimum value
# Note: If there are multiple occurrences of the maximum or minimum value, idxmax() and idxmin() will return the index of the first occurrence.
# Example:
# If the series is [1, 2, 3, 2], idxmax() will return the index of the first 3, and idxmin() will return the index of the first 1.
