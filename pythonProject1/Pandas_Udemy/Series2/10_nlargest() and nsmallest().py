import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']

# Get the top 5 largest values in the Series
top_5_largest = alcohol.nlargest(5)
print("Top 5 largest values in the Series:\n", top_5_largest)

# Get the top 5 smallest values in the Series
top_5_smallest = alcohol.nsmallest(5)
print("\nTop 5 smallest values in the Series:\n", top_5_smallest)