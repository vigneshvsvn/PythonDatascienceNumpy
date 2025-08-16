import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']

"""
spot vs global transformations
- spot transformation: applies to each element individually, e.g., using `map(),update(), using assignment`
- global transformation: applies to the entire Series, e.g., using `apply()`
"""

print(alcohol.head())
alcohol['Algeria']=19 # Adding a new value to the Series
print(alcohol.head())

# using update() to modify values in the Series  using another Series or a dictionary
#alcohol.update(pd.Series({'Algeria': 20, 'Angola': 10}))
alcohol.update(pd.Series(data=[20,10],index=['Algeria', 'Angola']))
print(alcohol.head())


print(alcohol.apply(lambda x: x + 10).head())  # Applying a function to each element in the Series    will return a new Series with the transformed values
print(alcohol.head())


# using map() to transform values in the Series
print(alcohol.map(lambda x: x + 10).head())  # Applying a function to each element in the Series will return a new Series with the transformed values
print(alcohol.head())