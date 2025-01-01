import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load the dataset
file_path = 'lagos_rooftop_solar_potential.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data
print(data.head())

# Get an overview of the data, including column types and missing values
print(data.info())
# Drop irrelevant columns
data_cleaned = data.drop(columns=['Unit_installation_price', 'Comment'])

# Handle missing values
# Fill missing values in `Estimated_building_height` and `Estimated_capacity_factor` with the mean value of the column
data_cleaned['Estimated_building_height'].fillna(data_cleaned['Estimated_building_height'].mean(), inplace=True)
data_cleaned['Estimated_capacity_factor'].fillna(data_cleaned['Estimated_capacity_factor'].mean(), inplace=True)

# Verify missing values are handled
print(data_cleaned.isnull().sum())

# Summary statistics for numerical columns
summary_stats = data_cleaned.describe()

print(summary_stats)

# Calculate the correlation matrix
correlation_matrix = data_cleaned.corr()

# Plot correlation matrix using matplotlib
plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Correlation Matrix of Solar Data')
plt.show()

# Group by building type and calculate the mean
energy_by_building_type = data_cleaned.groupby('Assumed_building_type')['Energy_potential_per_year'].mean()

# Bar chart using matplotlib
plt.figure(figsize=(10, 6))
plt.barh(energy_by_building_type.index, energy_by_building_type.values, color='skyblue')
plt.title('Average Energy Potential per Year by Building Type')
plt.xlabel('Energy Potential per Year (kWh)')
plt.ylabel('Building Type')
plt.show()

# Scatter plot using matplotlib
plt.figure(figsize=(10, 6))
for building_type in data_cleaned['Assumed_building_type'].unique():
    subset = data_cleaned[data_cleaned['Assumed_building_type'] == building_type]
    plt.scatter(subset['Surface_area'], subset['Energy_potential_per_year'], label=building_type)

plt.title('Energy Potential per Year vs. Surface Area')
plt.xlabel('Surface Area (m²)')
plt.ylabel('Energy Potential per Year (kWh)')
plt.legend(title='Building Type')
plt.show()

# Histogram using matplotlib
plt.figure(figsize=(10, 6))
plt.hist(data_cleaned['Energy_potential_per_year'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of Energy Potential per Year')
plt.xlabel('Energy Potential per Year (kWh)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot for Tilt vs. Energy Potential
plt.figure(figsize=(10, 6))
for building_type in data_cleaned['Assumed_building_type'].unique():
    subset = data_cleaned[data_cleaned['Assumed_building_type'] == building_type]
    plt.scatter(subset['Estimated_tilt'], subset['Energy_potential_per_year'], label=building_type)

plt.title('Energy Potential per Year vs. Estimated Tilt')
plt.xlabel('Estimated Tilt (Degrees)')
plt.ylabel('Energy Potential per Year (kWh)')
plt.legend(title='Building Type')
plt.show()


___________________
