import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce-behavior-data.csv")

# Preview
print(df.head())

# Basic info
print(df.info())

# --- Data Cleaning ---
# Drop missing values
df = df.dropna()

# Convert time column
df["event_time"] = pd.to_datetime(df["event_time"])

# --- Analysis ---

# 1. Top product categories
top_categories = df["category_code"].value_counts().head(10)
print(top_categories)

# 2. Revenue by category (only purchases)
purchases = df[df["event_type"] == "purchase"]

revenue_by_category = purchases.groupby("category_code")["price"].sum().sort_values(ascending=False)
print(revenue_by_category.head())

# 3. Events distribution
event_counts = df["event_type"].value_counts()
print(event_counts)

# --- Visualization ---

# Top categories plot
top_categories.plot(kind="bar")
plt.title("Top Product Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Revenue plot
revenue_by_category.head(10).plot(kind="bar")
plt.title("Top Revenue Generating Categories")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()
