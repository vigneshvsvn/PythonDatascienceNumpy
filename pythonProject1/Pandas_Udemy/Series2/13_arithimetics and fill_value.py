from unittest.mock import inplace

import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
#print(alcohol+2)  # Add 2 to each value in the Series
print(alcohol)

more_drinks = pd.Series({ 'Albania': 5, 'Algeria': 10,'Afghanistan':1}, name='more_drinks')

print(alcohol + more_drinks)  # Add values from another Series, aligning by index

print(alcohol.add(more_drinks, fill_value=0))  # Add with fill_value for missing indices