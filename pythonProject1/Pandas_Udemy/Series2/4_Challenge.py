import pandas as pd

# Read a CSV file into a Series
# The 'usecols' parameter specifies which columns to read, and 'index_col' sets the index
# The resulting Series will have 'country' as the index and 'wine_servings' as the values
# The 'squeeze' function is not needed here as we are directly selecting a single column
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
wineservings=alcohol.loc[alcohol.notnull() & (alcohol < 100)]  # Filter the Series to include only countries with wine servings less than 100
print("Total Wine Consuming: ",wineservings.sum())  #	Calculate the total wine servings for countries	 with less than 100 servings