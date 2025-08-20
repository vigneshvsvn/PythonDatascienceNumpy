import pandas as pd
df=pd.DataFrame({
	'age':[3,34,29],
	'height':['2','5.6','5.3'],
	'weight':[12.5,54.5,75.3]
})

print(df)
print(df.rename(index={0:'first',1:'second',2:'third'}, columns={'age':'Age','height':'Height','weight':'Weight'}))  # Rename index and columns using rename() method
print(df.rename(mapper=str.upper, axis=1))  # Rename all columns to uppercase using a mapper function , need to use axis parameter to specify that we are renaming columns
print(df.axes[0])
print(df.index)
print(df.columns)