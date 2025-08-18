import pandas as pd
nutrition = pd.read_csv('nutrition.csv')
#nutrition.info(memory_usage='deep')
#print(nutrition['Unnamed: 0'])      # if we don't have a column name then unamed: 0 is the default column name, example of index column

# remove the unnamed column
nutrition = nutrition.drop(columns=['Unnamed: 0'],axis=1)  # what is the axis? 0 is row and 1 is column, so we are removing the column,
# As we already specified columns=['Unnamed: 0'] why we are using axis=1?
# Because we can use the same code to remove rows as well, so we need to specify the axis
print(nutrition.head())