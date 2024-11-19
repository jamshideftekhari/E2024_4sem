import pandas as pd
import matplotlib.pyplot as plt

# Creating more complex data for multiple metrics in a business
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Electronics Sales': [50000, 60000, 55000, 70000, 75000, 80000],
    'Apparel Sales': [30000, 28000, 35000, 32000, 40000, 42000],
    'Home Goods Sales': [20000, 22000, 25000, 28000, 35000, 38000],
    'Beauty Sales': [25000, 27000, 30000, 35000, 38000, 40000],
    'Sports Sales': [40000, 42000, 45000, 50000, 55000, 60000],
    'Website Traffic': [200000, 230000, 220000, 240000, 250000, 270000],
    'Customer Satisfaction': [85, 86, 84, 88, 90, 89],
    'Conversion Rate (%)': [4.5, 4.6, 4.7, 4.8, 5.0, 5.2],
    'Customer Acquisition Cost ($)': [40, 38, 37, 35, 34, 33]
}

# Converting data into a DataFrame
df = pd.DataFrame(data)
print(df)

# Plotting the data
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Sales data (stacked bar chart)
sales_columns = ['Electronics Sales', 'Apparel Sales', 'Home Goods Sales', 'Beauty Sales', 'Sports Sales']
df.plot(x='Month', y=sales_columns, kind='bar', stacked=True, ax=axes[0, 0])
axes[0, 0].set_title('Monthly Sales by Product Category')
axes[0, 0].set_ylabel('Sales (USD)')
axes[0, 0].legend(title='Product Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

# Website traffic and customer satisfaction (dual axis)
ax2 = df.plot(x='Month', y='Website Traffic', ax=axes[0, 1], color='blue', legend=False)
df.plot(x='Month', y='Customer Satisfaction', secondary_y=True, ax=ax2, color='orange', legend=False)
axes[0, 1].set_title('Website Traffic and Customer Satisfaction')
ax2.set_ylabel('Website Traffic')
ax2.right_ax.set_ylabel('Customer Satisfaction (%)')

# Conversion rate line plot
df.plot(x='Month', y='Conversion Rate (%)', kind='line', ax=axes[1, 0], color='green', marker='o')
axes[1, 0].set_title('Monthly Conversion Rate')
axes[1, 0].set_ylabel('Conversion Rate (%)')

# Customer acquisition cost line plot
df.plot(x='Month', y='Customer Acquisition Cost ($)', kind='line', ax=axes[1, 1], color='red', marker='s')
axes[1, 1].set_title('Customer Acquisition Cost Over Time')
axes[1, 1].set_ylabel('Customer Acquisition Cost ($)')

plt.tight_layout()
plt.show()

# Display the dataframe
print(df)
