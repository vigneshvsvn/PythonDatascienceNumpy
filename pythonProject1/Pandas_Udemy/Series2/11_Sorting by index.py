import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print(alcohol.sort_index(ascending=False))  # Sort by index in descending order
print(alcohol.sort_index(ascending=True))   # Sort by index in ascending order
print(alcohol.sort_index())  # Default is ascending order
#print(alcohol.sort_index(ascending=False, inplace=True)) # This will raise an error because inplace=True is not allowed with chained operations