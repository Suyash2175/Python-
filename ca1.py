import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('dataset_15.csv')

# Drop unnecessary columns
data = df.drop(['infraspecificEpithet', 'verbatimScientificNameAuthorship', 'locality',
                'individualCount', 'coordinatePrecision', 'elevation', 'elevationAccuracy',
                'depth', 'depthAccuracy', 'recordNumber', 'typeStatus', 'establishmentMeans'], 
               axis=1, errors='ignore')

# Convert all possible numeric columns
data_numeric = data.apply(pd.to_numeric, errors='coerce')

# Filter only numeric columns
numeric_cols = data_numeric.select_dtypes(include=['float64', 'int64'])

# Set style for more professional plots
sns.set(style="white", palette="muted")

# 1. **Pairplot of Decimal Latitude and Longitude**
# A pairplot shows relationships between the numeric variables
plt.figure(figsize=(14, 10))
sns.pairplot(data=numeric_cols[['decimalLatitude', 'decimalLongitude']], 
             height=3, aspect=1.5, plot_kws={'edgecolor':'black', 'linewidth':1})
plt.suptitle('Professional Pairplot of Decimal Latitude vs Longitude', fontsize=20, weight='bold')
plt.tight_layout()
plt.show()

# 2. **Correlation Heatmap**: 
# A heatmap to show correlations between the numeric variables, enhanced with a cool color palette
plt.figure(figsize=(12, 8))
correlation = numeric_cols.corr()
sns.heatmap(correlation, annot=True, cmap='Blues', linewidths=1, annot_kws={"size": 12}, 
            cbar_kws={"shrink": .75}, linecolor='black')
plt.title('Correlation Heatmap', fontsize=18, weight='bold')
plt.xticks(fontsize=12, rotation=45, weight='bold')
plt.yticks(fontsize=12, weight='bold')
plt.tight_layout()
plt.show()

# 3. **Scatter Plot Between Decimal Latitude and Longitude**
# Use professional color palette with large, clear markers
plt.figure(figsize=(12, 8))
sns.scatterplot(x=data['decimalLongitude'], y=data['decimalLatitude'], 
                hue=data['kingdom'] if 'kingdom' in data.columns else None, 
                palette='Set2', edgecolor='black', s=150, alpha=0.7)
plt.title('Professional Scatter Plot: Latitude vs Longitude', fontsize=18, weight='bold')
plt.xlabel('Decimal Longitude', fontsize=14, weight='bold')
plt.ylabel('Decimal Latitude', fontsize=14, weight='bold')
plt.xticks(fontsize=12, weight='bold')
plt.yticks(fontsize=12, weight='bold')
plt.grid(True, linestyle='--', alpha=0.5)
if 'kingdom' in data.columns:
    plt.legend(loc='best', title='Kingdom', fontsize=12, title_fontsize='13', fancybox=True, shadow=True)
plt.tight_layout()
plt.show()

# 4. **Countplot of Kingdom** (if exists in dataset)
# Professional and clean count plot
if 'kingdom' in data.columns:
    plt.figure(figsize=(14, 8))
    sns.countplot(x=data['kingdom'], palette='muted', edgecolor='black')
    plt.title('Distribution of Kingdom', fontsize=18, weight='bold')
    plt.xlabel('Kingdom', fontsize=14, weight='bold')
    plt.ylabel('Count', fontsize=14, weight='bold')
    plt.xticks(fontsize=12, weight='bold', rotation=45)
    plt.yticks(fontsize=12, weight='bold')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# 5. **Advanced KDE Plot (Density Plot) for Latitude and Longitude**
plt.figure(figsize=(12, 8))
sns.kdeplot(data=data['decimalLatitude'], shade=True, color="blue", label="Latitude", linewidth=3)
sns.kdeplot(data=data['decimalLongitude'], shade=True, color="green", label="Longitude", linewidth=3)
plt.title('KDE Plot of Latitude and Longitude', fontsize=18, weight='bold')
plt.xlabel('Value', fontsize=14, weight='bold')
plt.ylabel('Density', fontsize=14, weight='bold')
plt.xticks(fontsize=12, weight='bold')
plt.yticks(fontsize=12, weight='bold')
plt.legend(loc='best', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
