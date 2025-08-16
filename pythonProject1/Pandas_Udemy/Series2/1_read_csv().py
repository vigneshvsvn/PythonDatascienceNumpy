import pandas as pd
from numpy.ma.core import squeeze

# Read a CSV file into a DataFrame
wine_servings=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print(type(wine_servings))  #<class 'pandas.core.series.Series'>