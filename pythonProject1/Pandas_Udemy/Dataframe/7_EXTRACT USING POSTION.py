import pandas as pd
pd.options.display.max_columns = 10  # Show all columns in the DataFrame
nutrition=pd.read_csv('nutrition.csv',index_col='name').head(20).drop(columns=['Unnamed: 0'],axis=1)  # Read the CSV file and drop the Unnamed: 0 column
print(nutrition.iloc[0:3,0:5])  # Extracting rows using position

## using Boolean mask
print(nutrition.iloc[[True if i%2==0 else False for i in range(len(nutrition))] ,
						[0,1,2,3,4]])  # Extracting rows using position with a boolean mask


