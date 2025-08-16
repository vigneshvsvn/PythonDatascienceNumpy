import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print('sum:',alcohol.sum())  # Sum of all wine servings
print(alcohol.cumsum())  # Cumulative sum of wine servings