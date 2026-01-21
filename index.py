python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data_url = 'https://data.abudhabi.ae/dataset/traffic-accident-reports-2025.csv'
data = pd.read_csv(data_url)

# Display the first few rows of the dataset
print(data.head())

# Example: Generate a heatmap of accident hotspots
heatmap_data = data.groupby(['city', 'street']).size().reset_index(name='accident_count')
heatmap_data = heatmap_data.pivot('city', 'street', 'accident_count')

plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True)
plt.title('Accident Hotspots in Abu Dhabi 2025')
plt.show()

# Example: Analyze accident trends over time
data['date'] = pd.to_datetime(data['date'])
accident_trends = data.groupby(data['date'].dt.month).size()

plt.figure(figsize=(10, 5))
plt.plot(accident_trends.index, accident_trends.values, marker='o')
plt.title('Monthly Traffic Accident Trends in 2025')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.show()
