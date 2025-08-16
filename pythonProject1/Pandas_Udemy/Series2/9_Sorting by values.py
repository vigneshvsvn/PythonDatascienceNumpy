"""
Sort by values and sort by index in a Series.
This code demonstrates how to sort a Pandas Series by its values and by its index.
It uses the `sort_values()` method to sort by values and the `sort_index()` method
"""
import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
# Sort the Series by values in ascending order
sorted_by_values = alcohol.sort_values()
print("Series sorted by values (ascending):\n", sorted_by_values)
# Sort the Series by values in descending order
sorted_by_values_desc = alcohol.sort_values(ascending=False)
print("\nSeries sorted by values (descending):\n", sorted_by_values_desc)