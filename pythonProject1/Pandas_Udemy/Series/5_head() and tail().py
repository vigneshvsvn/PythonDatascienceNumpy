import pandas as pd
int_series = pd.Series(range(1,101), name='Integers')
print("Integer Series with name:", int_series)
print("First  elements using head():")
pd.options.display.max_rows = 100  # Set maximum rows to display
print(int_series.head(30))  # Display the first 5 elements

print("Last  elements using tail():")
print(int_series.tail(30))  # Display the last 5 elements

