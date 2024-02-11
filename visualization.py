import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load your dataset from CSV

df = pd.read_csv("climate_change.csv")

# Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.title('Box Plot')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, bins=20, kde=True)
plt.title('Histogram')
plt.show()

# Violin Plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=df)
plt.title('Violin Plot')
plt.show()

# Scatter Plot
plt.subplot(2, 2, 3)
sns.scatterplot(data=df, x='Temp', y='Year')
plt.title('Scatter Plot')
plt.show()