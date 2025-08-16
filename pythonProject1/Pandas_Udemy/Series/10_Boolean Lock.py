"""
boolean mask is a series of boolean values that can be used to filter data in a DataFrame or Series.
It is created by applying a condition to a Series or DataFrame, resulting in a Series of boolean values (True or False).
This boolean mask can then be used to select rows or elements that meet the specified condition.

"""

import pandas as pd


book_series = pd.Series(['The Great Gatsby', 'To Kill a Mockingbird', 'Pride and Prejudice'])
print( book_series.loc[[True, False, True]])  # All values are True