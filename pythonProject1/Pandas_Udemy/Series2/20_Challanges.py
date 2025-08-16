import pandas as pd
beer=pd.read_csv('drinks.csv',usecols=['country','beer_servings'],index_col='country')['beer_servings']
print("Mean:",beer.mean())
print("Median:",beer.median())
print("Mode:",beer.mode()[0])
print("Variance:",beer.var())
print("Standard Deviation:",beer.std())
print("Minimum:",beer.min())
print("Maximum:",beer.max())

beer[:10]