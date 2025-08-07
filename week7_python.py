# Task 1: Load and Explore the Dataset

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Enable inline plotting for Jupyter notebooks
%matplotlib inline

# Try loading the Iris dataset and converting it into a pandas DataFrame
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({i: name for i, name in enumerate(iris.target_names)})
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# Display the first few rows
print("\n📄 First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\n🔍 Dataset Info:")
print(df.info())

print("\n❓ Missing Values:")
print(df.isnull().sum())

# No missing values in the Iris dataset, so no cleaning needed here.

# Task 2: Basic Data Analysis

# Basic statistics
print("\n📊 Basic Statistics:")
print(df.describe())

# Group by species and calculate the mean
print("\n📚 Mean values per species:")
grouped = df.groupby("species").mean()
print(grouped)

# Interesting observation
print("\n🔎 Observations:")
print("- Setosa species have the shortest petals and sepals.")
print("- Virginica has the longest petals and sepals.")

# Task 3: Data Visualization

# Set the style
sns.set(style="whitegrid")

# 1. Line Chart - Mean values per species
plt.figure(figsize=(10, 5))
grouped.T.plot(kind='line', marker='o')
plt.title("Mean Feature Values by Species")
plt.xlabel("Features")
plt.ylabel("Mean Measurement (cm)")
plt.legend(title="Species")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Chart - Average Petal Length per Species
plt.figure(figsize=(6, 4))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# 3. Histogram - Sepal Length Distribution
plt.figure(figsize=(6, 4))
plt.hist(df['sepal length (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()


# Summary of Findings:
# -Setosa species are clearly separated in terms of petal length and width.

# -Virginica and Versicolor show closer values but still differ in petal and sepal sizes.

# -Distribution of sepal length is slightly right-skewed.

# -Strong positive correlation between petal and sepal lengths in the scatter plot.
