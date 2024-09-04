import pandas as pd

# Load the dataset
file_path = "coffee.csv"  # Ensure this path is correct for your local setup
data = pd.read_csv(file_path)

# Basic Data Inspection

# Display the first 10 rows
print("First 10 rows of the dataset:")
print(data.head(10))
print("\n")

# Number of rows and columns
print(f"Number of rows and columns: {data.shape}")
print("\n")

# Data types of each column
print("Data types of each column:")
print(data.dtypes)
print("\n")

# Handling Missing Data

# Identify columns with missing data and their counts
missing_data = data.isnull().sum()
print("Columns with missing data and their counts:")
print(missing_data[missing_data > 0])
print("\n")

# Calculate the percentage of missing data for each column
missing_percentage = (missing_data / len(data)) * 100

# Identify columns with more than 20% missing data
columns_to_handle = missing_percentage[missing_percentage > 20].index
print("Columns with more than 20% missing data:")
print(columns_to_handle)
print("\n")

# Example of handling missing data: Drop columns with more than 20% missing values
data_cleaned = data.drop(columns=columns_to_handle)
print("Dataset after dropping columns with more than 20% missing values:")
print(data_cleaned.head(10))
print("\n")

# Summary Statistics

# Generate summary statistics for numerical columns
print("Summary statistics for numerical columns:")
print(data.describe())
print("\n")

# Analysis of Bitterness Preference Across Age Groups
# Ensure 'coffee_a_bitterness' and 'age' columns are present
if 'coffee_a_bitterness' in data.columns and 'age' in data.columns:
    # Group by age and get mean bitterness preference
    bitterness_by_age = data.groupby('age')['coffee_a_bitterness'].mean()
    print("Bitterness preference by age group:")
    print(bitterness_by_age)
else:
    print("Columns 'coffee_a_bitterness' or 'age' not found in the dataset.")
