from string import ascii_lowercase,ascii_uppercase
import pandas as pd
list_alphabet_lower=list(ascii_lowercase)
list_alphabet_upper=list(ascii_uppercase)
alphabet_series=pd.Series(list_alphabet_lower,name='Alphabet',index=map(lambda x:'label_'+x,list_alphabet_upper))
print("Alphabet Series with name:")
print(alphabet_series['label_A'])  # Accessing by label