import pandas as pd

list_actrors=['Tom Cruise', 'Brad Pitt', 'Leonardo DiCaprio', 'Robert Downey Jr.']
list_ages=[60, 59, 48, 56]

actor_series=pd.Series(data=list_ages,index=list_actrors,name='Actors',dtype='int64')
print("Actor Series with name:")
#print(actor_series.size, '\n', actor_series.name)
print(actor_series)
