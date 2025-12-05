# customer-orders-analysis
#  Customer Orders Analysis Pipeline

A Python-based data analysis tool that extracts, cleans, and visualizes customer transaction data. This project demonstrates a full **ETL (Extract, Transform, Load)** pipeline using the Pandas library.

##  Project Overview
The goal of this project was to move away from manual Excel analysis and build an automated script that can process thousands of orders in seconds.

**Key Features:**
* **ETL Pipeline:** Reads raw CSV files with complex formatting (e.g., pipe-separated values like `Laptop|Mouse`).
* **Data Cleaning:** uses Pandas to split strings and clean unstructured data.
* **Business Insights:** Automatically calculates:
    * Top 5 Customers by spending.
    * Most Popular Product Categories.
* **Visualization:** Generates a Bar Chart using Matplotlib to visualize high-value customers.

##  Tools & Technologies
* **Language:** Python 3.x
* **Libraries:** Pandas, Matplotlib
* **Editor:** VS Code

##  File Structure
```text
DataProjectz/
├── analysis.py           # The main Python script
├── orders.csv            # Raw data file (Input)
├── README.md             # Project documentation
├── top_customers.csv     # Generated Report (Output)
└── popular_products.csv  # Generated Report (Output)
