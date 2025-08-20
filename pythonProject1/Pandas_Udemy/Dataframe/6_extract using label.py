import pandas as pd
pd.options.display.max_columns = 10  # Show all columns in the DataFrame
nutrition=pd.read_csv('nutrition.csv',index_col='name')
# Extracting rows using label
# We can use the loc[] method to extract rows using labels
# loc[] method is used to access a group of rows and columns by labels or a boolean array
#print(nutrition.loc['Cornstarch'])  # Extracting the calories of Cornstarch returns a Series object
#print(nutrition.loc['Cornstarch','calories'])  # [label,column_name]
print(nutrition.loc[['Cornstarch','Honey'],['calories','sodium']])  # Extracting multiple rows using labels returns a DataFrame object
print(nutrition.loc[
	['Raspberries, raw','Cornstarch'],
	['calories','sodium']
	  ])
