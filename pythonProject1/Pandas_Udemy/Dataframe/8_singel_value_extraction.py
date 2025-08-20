import timeit 

import pandas as pd
pd.options.display.max_columns = 10  # Show all columns in the DataFrame
nutrition=pd.read_csv('nutrition.csv',index_col='name').head(20).drop(columns=['Unnamed: 0'],axis=1)

print(nutrition.at['Cornstarch','calories'])  # Extracting a single value using label it will be faster than loc[]
# The at[] method is used to access a single value for a row/column label pair
# It is similar to loc[] but is faster for accessing a single value
# It is used to access a single value for a row/column label pair

print(nutrition.iat[0,0])  # Extracting a single value using position it will be faster than iloc[]

print(timeit.timeit(lambda: nutrition.at['Cornstarch', 'calories'], number=1000))# Measure the time taken to extract a single value using at[]
#number =1000 means we are running the code 1000 times to get the average time taken