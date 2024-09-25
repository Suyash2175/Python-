import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt    
# Load the data
df = pd.read_csv('dataset_15.csv')     
print(df.info())  # Get an overview of column types     
print(df.isnull().sum())    
print(df.columns)
# Get the number of columns
num_columns = len(df.columns)
print(f'The dataset has {num_columns} columns.')

data = df.drop(['infraspecificEpithet', 'verbatimScientificNameAuthorship', 'locality',
                'individualCount', 'coordinatePrecision', 'elevation', 'elevationAccuracy',
                'depth', 'depthAccuracy', 'recordNumber', 'typeStatus', 'establishmentMeans'], 
               axis=1, errors='ignore')

data.columns
print(df.describe())
sns.boxplot(x=df['decimalLatitude'])
plt.show()

sns.boxplot(x=df['decimalLongitude'])
plt.show()
