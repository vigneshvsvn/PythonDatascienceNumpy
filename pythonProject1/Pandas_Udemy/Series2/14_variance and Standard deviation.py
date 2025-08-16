import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print("Mean:",alcohol.mean())  # Calculate mean of wine servings
print("Variance:",alcohol.var())  # Calculate variance of wine servings
print("Standard Deviation:",alcohol.std())  # Calculate standard deviation of wine servings