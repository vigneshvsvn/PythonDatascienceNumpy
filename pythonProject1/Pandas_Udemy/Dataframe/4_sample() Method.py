from operator import index

import pandas as pd
pd.options.display.max_columns = 10  # Show all columns in the DataFrame
nutrition=pd.read_csv('nutrition.csv',index_col=0) # index_col=0 means the first column is the index column, so we don't need to specify the index column name
# sample() method is used to get a random sample of rows from the DataFrame
# By default, it returns one random row, but we can specify the number of rows to return using the n parameter
print(nutrition.sample())  # Get a random sample of 5 rows from the DataFrame

print(nutrition.index)
print(nutrition.columns)

