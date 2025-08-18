import pandas as pd
pd.options.display.max_columns = 10  # Show all columns in the DataFrame
nutrition=pd.read_csv('nutrition.csv',index_col=0)

# Using the set_index() method to change the index of the DataFrame
# The set_index() method is used to set the DataFrame index using existing columns.
# It returns a new DataFrame with the specified column as the index.
# The original DataFrame remains unchanged unless you set the inplace parameter to True.
print(nutrition.set_index('name',drop=False).head(1))       # drop=False means we are not dropping the index column, so it will be included in the DataFrame
# If we don't specify drop=False, the index column will be dropped from the DataFrame

print(nutrition.set_index('calories',drop=False,append=True,verify_integrity= True).head(1))      # add Index to the existing index, so we can have multiple index columns
# append=True means we are adding the index column to the existing index, so we can have multiple index columns
# If we don't specify append=True, the index column will replace the existing index

# verify_integrity=True means we are checking the integrity of the index, so we can have unique index values
# If we don't specify verify_integrity=True, the index values can be duplicated
# If we have duplicate index values, it will raise an error
# If we don't specify verify_integrity=True, the index values can be duplicated and it will not raise an error
# If we have duplicate index values, it will not raise an error and


