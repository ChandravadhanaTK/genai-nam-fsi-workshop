import pandas as pd
from pathlib import Path

path = Path(__file__).parent / "dataloan.csv"
# Read the CSV data
data = pd.read_csv(path)

# Print the full data set
print(data)

# Print the total number of rows and columns
print(data.shape)

# Print number of rows only
print("Number of rows:", data.shape[0])

# Print number of columns only
print("Number of columns:", data.shape[1])

# Print the first 5 records
print(data.head(5))

# Print the last 5 records
print(data.tail(5))

# Print all non-null columns using info()
print(data.info())

# Print all column names
print(data.columns)

# Print all datatypes of respective column names
print(data.dtypes)

# Print the descriptive statistics of data frame
print(data.describe())

# Print the sum of NAN values
print(data.isnull().sum())

# Print and access only the column names like Education and Self_Employed
print(data[['Education', 'Self_Employed']])

# Print and access up to the second index position
print(data.iloc[:2])

# Rename the column gender to gender_status
data.rename(columns={'Gender': 'gender_status'}, inplace=True)
print(data.head())
