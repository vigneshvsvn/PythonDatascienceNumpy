import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']

print(alcohol[0:5])  # Display the first 5 elements

# Iterating through the Series
# Using a for loop to iterate through the Series
print("Iterating through the Series Values:")
for i in alcohol:
	print(i)

print("Iterating through the Series Index:")
for i in alcohol.index:
	print(i)



print("Iterating through the Series both Index and Values:")
for index,value in alcohol.items():
	print(f"Index: {index} and  Value: {value}")