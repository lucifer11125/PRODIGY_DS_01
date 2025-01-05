import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
# Replace 'your_file_path.csv' with the path to your dataset file
file_path = 'API_SP.POP.1564.TO.ZS_DS2_en_csv_v2_145.csv'
data = pd.read_csv(file_path, skiprows=4)  # Skip metadata rows

# Step 2: Filter data for India
india_data = data[data['Country Name'] == 'India']

# Step 3: Select columns for years (e.g., 2000 to 2023)
india_age_group = india_data.loc[:, '1960':'2023']

# Transpose the data for easier plotting
india_age_group = india_age_group.T
india_age_group.columns = ['Population Age 15-64 (%)']
india_age_group.index.name = 'Year'
india_age_group.reset_index(inplace=True)

# Filter data from 2000 to 2023
india_age_group = india_age_group[india_age_group['Year'].astype(int) >= 2000]

# Step 4: Visualization
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# Create a line plot for population distribution
sns.lineplot(data=india_age_group, x='Year', y='Population Age 15-64 (%)', marker='o', color='b', linewidth=2.5)

# Add titles and labels
plt.title('Trend of Population Aged 15-64 (%) in India (2000-2023)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population Aged 15-64 (%)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
