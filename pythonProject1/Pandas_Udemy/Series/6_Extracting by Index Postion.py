from string import ascii_lowercase
import pandas as pd
list_alphabet=list(ascii_lowercase)
alphabet_series=pd.Series(list_alphabet,name='Alphabet',index=range(1,len(list_alphabet)+1))
print("Alphabet Series with name:")
print(alphabet_series[1])  # Extracting by index position
print(alphabet_series[1:5])  # Extracting by index position range
print(alphabet_series[1:])  # Extracting by index position range from 1


