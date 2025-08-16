import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print(alcohol.head())
print(alcohol.diff().head())
