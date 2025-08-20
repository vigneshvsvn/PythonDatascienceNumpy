import pandas as pd
import numpy as np

df=pd.DataFrame({
	'age':[3,34,29],
	'height':['2','5.6','5.3'],
		'weight':[12.5,54.5,75.3]
})
df.loc[2,'weight']=np.nan
df.loc[0,:] = np.nan  # Setting the first row to NaN
print(df)  # Accessing a specific value using loc[] method
print(df.dropna(axis=0))  # Drop rows with any NaN values
print(df.dropna(how='any',axis=0))  # Drop rows with any NaN values (equivalent to the previous line)    what is the difference between these two lines?
# replace all nan values with a specific value
print(df.fillna(0))  # Replace all NaN values with 0
# how to drop on specific column
print(df.dropna(subset=['weight'], axis=0))  # Drop rows where the 'weight' column has NaN values
# how to drop on specific row
#print(df.dropna(subset=[0], axis=1))  # Drop columns where the
print(df.shape[1])
#what is thresh= 2?
print(df.dropna(thresh=2))  # Drop rows with less than 2 non-NaN values
print(df.dropna(thresh=2, axis=1))  #