import pandas as pd
df=pd.DataFrame({
	'age':[3,34,29],
	'height':['2','5.6','5.3'],
	'weight':[12.5,54.5,75.3]
})
print("Before Cast",df.info())
# Using astype() method to cast one type to another
# astype() method is used to cast a pandas object to a specified dtype
# It returns a new object with the specified dtype
# The original object remains unchanged unless you set the inplace parameter to True
df['height']=df['height'].astype(float)  # Cast height column to float
df['weight']=df['weight'].astype(int)    # Cast weight column to int
df['age']=df['age'].astype(str)           # Cast age column to str
print("After Cast",df.info())