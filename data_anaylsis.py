import pandas as pd
import matplotlib.pyplot as plt
# Load a sample dataset (replace with your own file if needed)
df = pd.read_csv("sales_data.cvs")  # Make sure this file is in your folder
# View first few rows
print(df.head())

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())
# Total sales by product
sales_by_product = df.groupby("Product")["Revenue"].sum()
print(sales_by_product)

# Monthly sales trend
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()
print(monthly_sales)
# Bar chart: Sales by product
sales_by_product.plot(kind="bar", title="Total Sales by Product", color="skyblue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Line chart: Monthly sales trend
monthly_sales.plot(kind="line", title="Monthly Sales Trend", marker="o", color="green")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()