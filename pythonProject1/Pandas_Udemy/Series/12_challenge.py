import pandas as pd

square_series=pd.Series(data =[i**2 for i in range(100)], name='Square Numbers')
print(square_series.head())
print(square_series.tail())
print(square_series.iloc[10])  # Accessing the first element by integer position
print(square_series.iloc[10:21])  # Accessing a range of elements by integer positions