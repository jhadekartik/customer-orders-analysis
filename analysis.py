import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Load Data from CSV ---
# instead of data = [...], we read the file
print("Loading data from file...")
df = pd.read_csv('orders.csv')

# Custom Step: We need to handle the '|' separator in the items column
# In the CSV, items look like "Laptop|Mouse". We need to turn that into a list ['Laptop', 'Mouse']
df['items'] = df['items'].str.split('|')

# --- 2. Run Analysis ---
# (The rest of your code stays exactly the same!)
top_customers = df.groupby('customer')['total'].sum().sort_values(ascending=False)

print("Analysis running...")

# --- 3. Generate Chart ---
top_customers.plot(kind='bar', color='green', edgecolor='black') # Changed color to green
plt.title('Top Customers (Loaded from CSV)', fontsize=14)
plt.ylabel('Amount Spent ($)', fontsize=12)
plt.xlabel('Customer Name', fontsize=12)
plt.xticks(rotation=0)
plt.show()