from string import ascii_lowercase,ascii_uppercase
import pandas as pd
list_alphabet_lower=list(ascii_lowercase)
list_alphabet_upper=list(ascii_uppercase)
alphabet_series=pd.Series(list_alphabet_lower,name='Alphabet',index=list_alphabet_upper)
print("Alphabet Series:",alphabet_series)

print("Alphabet Series with prefix and suffix:")
print(alphabet_series.add_prefix('prefix_').add_suffix('_suffix'))