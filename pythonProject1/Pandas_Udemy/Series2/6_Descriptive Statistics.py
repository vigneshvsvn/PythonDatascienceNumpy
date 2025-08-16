import pandas as pd
import matplotlib
# Read a CSV file into a Series
# The 'usecols' parameter specifies which columns to read, and 'index_col' sets the index
# The resulting Series will have 'country' as the index and 'wine_servings' as the values
# The 'squeeze' function is not needed here as we are directly selecting a single column
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print("Summary statistics of the Series:", alcohol.describe())
print("Sum of series:", alcohol.sum())
print("Mean of series:", alcohol.mean())
print("Median of series:", alcohol.median())
print("Standard deviation of series:", alcohol.std())
print("Variance of series:", alcohol.var())
print("Minimum value in series:", alcohol.min())
print("Maximum value in series:", alcohol.max())
print("Count of non-null values in series:", alcohol.count())
print("Unique values in series:", alcohol.unique())
print("Value counts in series:\n", alcohol.value_counts())
print("Quantiles of series:\n", alcohol.quantile([0.25, 0.5, 0.75]))
