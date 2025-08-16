import pandas as pd

# Read a CSV file into a Series
# The 'usecols' parameter specifies which columns to read, and 'index_col' sets the index
# The resulting Series will have 'country' as the index and 'wine_servings' as the values
# The 'squeeze' function is not needed here as we are directly selecting a single column
wine_servings=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print(type(wine_servings))  #<class 'pandas.core.series.Series'>
print(wine_servings.shape)  # (193,) - returns a tuple with the number of elements in the Series
print(wine_servings.size)   # 193 - returns the number of elements in the Series
print(wine_servings.values) # returns the values of the Series as a NumPy array
print(wine_servings.index)  # returns the index of the Series, which is the 'country' column
print(wine_servings.values.size == wine_servings.index.size) # True - checks if the number of values matches the number of indices
print("Length of Series using len(series):",len(wine_servings))
