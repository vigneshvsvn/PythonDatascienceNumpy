import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
fifty_plus=alcohol[alcohol>=50]
print(fifty_plus.count())  # Count the number of countries with wine servings >= 50
print(fifty_plus.nsmallest(3))  # Get the 3 countries with the least wine servings among those with >= 50 servings