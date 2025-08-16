import pandas as pd
list_book=['Python for Data Analysis', 'Python Cookbook', 'Fluent Python', 'Effective Python']
book_series=pd.Series(list_book,name='Books')
print("Book Series with name:")

print(book_series.size,'\n',book_series.name)
print(book_series)