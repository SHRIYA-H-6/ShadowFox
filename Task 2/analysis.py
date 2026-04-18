import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("Superstore.csv", encoding='latin-1')

# Clean column names (important!)
df.columns = df.columns.str.strip()

# Convert to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', errors='coerce')

# Drop missing values
df = df.dropna()

# Create Month column
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)

# -----------------------
# Monthly Sales Trend
# -----------------------
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

fig1 = px.line(monthly_sales, x='Month', y='Sales',
               title='Monthly Sales Trend')
fig1.write_html("monthly_sales.html")

# -----------------------
# Category Sales
# -----------------------
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

fig2 = px.bar(category_sales, x='Category', y='Sales',
              title='Sales by Category', color='Category')
fig2.write_html("category_sales.html")

# -----------------------
# Profit by Category
# -----------------------
category_profit = df.groupby('Category')['Profit'].sum().reset_index()

fig3 = px.pie(category_profit, names='Category',
              values='Profit',
              title='Profit Distribution')
fig3.write_html("profit_distribution.html")

# -----------------------
# Segment Profit
# -----------------------
segment_profit = df.groupby('Segment')['Profit'].sum().reset_index()

fig4 = px.bar(segment_profit, x='Segment', y='Profit',
              title='Profit by Segment', color='Segment')
fig4.write_html("segment_profit.html")

# -----------------------
# Sales to Profit Ratio (fixed)
# -----------------------

# Avoid division by zero
df = df[df['Profit'] != 0]

df['Sales_to_Profit'] = df['Sales'] / df['Profit']

ratio = df.groupby('Category')['Sales_to_Profit'].mean().reset_index()

fig5 = px.bar(ratio, x='Category', y='Sales_to_Profit',
              title='Sales to Profit Ratio')
fig5.write_html("sales_profit_ratio.html")

print("✅ Analysis complete! Open the HTML files to view charts.")