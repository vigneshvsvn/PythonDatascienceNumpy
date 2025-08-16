import pandas as pd

# Read a CSV file into a Series
# The 'usecols' parameter specifies which columns to read, and 'index_col' sets the index
# The resulting Series will have 'country' as the index and 'wine_servings' as the values
# The 'squeeze' function is not needed here as we are directly selecting a single column
wine_servings=pd.read_csv('drinks.csv',usecols=['country','wine_servings'],index_col='country')['wine_servings']
print("Check if all values in the Series are unique:",wine_servings.is_unique)  # Check if all values in the Series are unique
print("Unique values in the Series:",wine_servings.unique())  # Get unique values in the Series
print("Number of unique values in the Series:",wine_servings.nunique(dropna=False))# Get the number of unique values in the Series, including NaN
print("Number of unique values in the Series:",wine_servings.nunique())  # Get the number of unique values in the Series, excluding NaN
print("Value counts in the Series:\n",wine_servings.count())  # Get the count of unique values in the Series

         


print("Check if the Series is empty:",wine_servings.empty)  # Check if the Series is empty
print("Check if the Series has any null values:",wine_servings.isnull().any())  # Check if the Series has any null values
print("is_monotonic_increasing",wine_servings.is_monotonic_increasing)      	# Check if the Series is monotonically increasing
print("is_monotonic_decreasing",wine_servings.is_monotonic_decreasing)      	# Check if the Series is monotonically decreasing
#print("",wine_servings.is_monotonic)      	# Check if the Series is monotonic (either increasing or decreasing)
print("Check if the Series has any NaN values:",wine_servings.hasnans)  # Check if the Series has any NaN values
print("Check if the Series has any null values:",wine_servings.isna().any())  # Check if the Series has any null values
print("Check if the Series has any NaN values:",wine_servings.isnull().any())  # Check if the Series has any NaN values   why .any ?
print("Check if the Series has any NaN values:",wine_servings.isna().any())  # Check if the Series has any NaN values
print("Check if the Series has any null values:",wine_servings.isnull().any())  # Check if the Series has any null values

print("Check if the Series has any non-null values:",wine_servings.notnull)  # Check if the Series has any non-null values
print("Check if the Series has any non-null values:",wine_servings.notnull().any())  # Check if the Series has any non-null values
print("Check if the Series has any non-null values:",wine_servings.notna().any())  # Check if the Series has any non-null values
