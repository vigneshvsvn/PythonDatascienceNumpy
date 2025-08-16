from string import ascii_lowercase,ascii_uppercase
import pandas as pd
list_alphabet_lower=list(ascii_lowercase)
list_alphabet_upper=list(ascii_uppercase)
alphabet_series=pd.Series(list_alphabet_lower,name='Alphabet',index=list_alphabet_upper)
print(alphabet_series.index,alphabet_series.name,alphabet_series.dtype,alphabet_series.shape)

print(alphabet_series.A)      #accessing by attribute using dot notation
print(alphabet_series['A'])    #accessing by label using square brackets
#print(alphabet_series['Label_A'])  #accessing by label using square brackets with custom label
print(alphabet_series.get('A'))  #accessing by label using get method
#print(alphabet_series.get('Label_A'))  #accessing by label using get method with custom label