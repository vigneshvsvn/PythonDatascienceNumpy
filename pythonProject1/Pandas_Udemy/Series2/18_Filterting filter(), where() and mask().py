import pandas as pd
alcohol=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']

## Filter on index using filter()
print(alcohol.filter(regex='^V'))  # Filter the Series to include only those with index starting with 'V'
print(alcohol.filter(like='dia'))  # Filter the Series to include only those with index containing 'a'
#print(alcohol.filter(items=['Afghanistan', 'Venezuela']))

## Filter on Values using filter()
alcohol_filter=alcohol.loc[alcohol > 300]  # Filter the Series to include only those with values greater than 100
print(alcohol_filter)

## using callable function with filter()
def filter_300(x):
	return x > 300

print(alcohol[filter_300])  # Filter the Series using a callable function to include only those with values greater than 300

## Using where() to filter values
print(alcohol.where(alcohol > 300))  # Replace values not meeting the condition with NaN
print(alcohol.where(alcohol > 300, other='to small'))  # Replace values not meeting the condition with 0

###########################################using mask() to filter values#########################
print(alcohol.mask(alcohol > 300))  # Replace values meeting the condition with NaN
print(alcohol.mask(alcohol > 300, other='to small'))  # Replace values