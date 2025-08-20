import pandas as pd
pd.options.display.max_columns = 10  # Show all columns in the DataFrame
nutrition=pd.read_csv('nutrition.csv',index_col='name').drop(columns=['Unnamed: 0'],axis=1)

print(nutrition.iloc[:3,:1])

print(nutrition.iloc[:3,:1].replace(to_replace='100 g', value='100'))

print(nutrition.iloc[:3,:1].replace(to_replace='\sg', value='0', regex=True))  #

print(nutrition.iloc[:3,:].astype(str).replace(to_replace='[^a-zA-Z]', value='', regex=True).mode())  #  .mode() returns the most common value in each column
