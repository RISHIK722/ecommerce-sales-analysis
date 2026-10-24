import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv('sales_data.csv')

# 2. Calculate Key Performance Indicators (KPIs)
total_revenue = df['Total_Sales'].sum()
total_orders = df['Order_ID'].nunique()
avg_order_value = total_revenue / total_orders

print("--- E-COMMERCE SALES SUMMARY ---")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ${avg_order_value:,.2f}\n")

# 3. Revenue by Category
category_sales = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
print("--- REVENUE BY CATEGORY ---")
print(category_sales)
print("\n")

# 4. Revenue by Region
region_sales = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print("--- REVENUE BY REGION ---")
print(region_sales)
print("\n")

# 5. Most Popular Payment Methods
payment_counts = df['Payment_Method'].value_counts()
print("--- ORDERS BY PAYMENT METHOD ---")
print(payment_counts)

# 6. Generate and Save a Bar Chart
plt.figure(figsize=(8, 5))
category_sales.plot(kind='bar', color=['#2563eb', '#3b82f6', '#60a5fa'])
plt.title('Total Revenue by Product Category', fontsize=14, fontweight='bold')
plt.xlabel('Category', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save chart as an image file
plt.savefig('category_revenue_chart.png')
print("\nChart saved successfully as 'category_revenue_chart.png'!")
