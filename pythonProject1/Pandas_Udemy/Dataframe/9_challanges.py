
import pandas as pd
pd.options.display.max_columns = 10  # Show all columns in the DataFrame
nutrition=pd.read_csv('nutrition.csv',index_col='name').drop(columns=['Unnamed: 0'],axis=1)

# extraction sample 10 rows
nutrition_mini=nutrition.sample(10,axis=0)  # Get a random sample of 10 rows from the DataFrame
print(nutrition_mini.loc[:,['total_fat','cholesterol']])  # Extracting multiple columns using loc[] method

print(nutrition_mini.loc[:,['total_fat','cholesterol']])