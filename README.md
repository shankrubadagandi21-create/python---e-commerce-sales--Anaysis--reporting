Python E-commerce Data Processing and Sales Reporting and power Bi dashborad

1. Project Overview

The Python E-commerce Data Processing and Sales Reporting project focuses on developing a reusable data-processing workflow to automate sales reporting for an e-commerce business.

The project uses multiple datasets, including customer, order, product, and payment information. These datasets are processed using Python to perform data validation, cleaning, transformation, integration, and business analysis.

The workflow generates meaningful business insights through sales and revenue calculations, product performance analysis, city-wise sales analysis, and monthly revenue trends.

The final results are presented through analytical reports, CSV files, and visualisations to support data-driven business decisions.

2. Business Problem

The e-commerce company receives business data from different systems.

The operations team manually combines customer, product, order, and payment files to prepare sales reports.

This manual process:

- Consumes time.
- Creates data inconsistencies.
- Increases the possibility of errors.
- Makes regular reporting difficult.

Solution: Developed a reusable Python workflow to automate data processing, validation, cleaning, analysis, and reporting.

3. Project Objectives

- Load multiple CSV datasets using Pandas.
- Inspect and understand the datasets.
- Identify missing values and duplicate records.
- Clean inconsistent data.
- Validate customer and product relationships.
- Combine multiple datasets using merge operations.
- Calculate sales and revenue metrics.
- Analyse monthly revenue trends.
- Identify top-performing products.
- Generate visualisations and export analytical results.

4. Tools and Technologies

Technology| Purpose
Python 3| Programming
Pandas| Data manipulation and analysis
NumPy| Numerical operations
Matplotlib| Data visualisation
Seaborn| Statistical visualisation
Google Colab| Development environment
CSV| Dataset storage
GitHub| Version control and project portfolio

5. Dataset Description

The project uses four datasets:

1. customers.csv

- Customer ID
- Customer Name
- City

2. products.csv

- Product ID
- Product Name
- Category
- Unit Price

3. orders.csv

- Order ID
- Customer ID
- Product ID
- Order Date
- Quantity
- Order Status

4. payments.csv

- Payment ID
- Order ID
- Payment Method
- Payment Status

6. Data Processing Workflow

Step 1: Data Loading

Imported customer, order, product, and payment CSV files using Pandas.

Step 2: Data Inspection

Used shape, head(), info(), and isnull() to understand the datasets, data types, and missing values.

Step 3: Data Cleaning

- Standardised column names.
- Removed duplicate records.
- Converted date columns into datetime format.
- Converted numerical columns into appropriate data types.
- Identified invalid quantities and product prices.

Step 4: Data Validation

- Checked missing customer references.
- Checked missing product references.
- Identified invalid records and inconsistent data.

Step 5: Data Integration

Combined customer, order, product, and payment datasets using Pandas merge() with common keys.

Step 6: Business Analysis

Calculated revenue and analysed sales performance using filtering, grouping, aggregation, and sorting.

Step 7: Data Visualisation

Created monthly revenue trend charts and top 10 product revenue charts using Matplotlib and Pandas.

Step 8: Report Generation

Saved processed datasets and analytical reports in CSV format and generated visualisation files in the outputs folder.

Step 9: Reusable Workflow

Developed reusable Python functions for revenue calculations and city-wise sales analysis.

7. Key Business Metrics and power Bi dashbords
   outputs/Power BI Dashbord

- Total Revenue
- Total Completed Orders
- Average Order Value (AOV)
- City-wise Revenue
- Product-wise Revenue
- Monthly Revenue Trends
- Top 10 Products by Revenue

8. Project Visualisations

The project includes the following visual outputs:

1. Monthly Revenue Trend
2. Top 10 Products by Revenue
3. Power BI Dashboard Screenshot

These visualisations help understand revenue performance and identify top-performing products.

9. Project Folder Structure

python-ecommerce-reporting/
│
├── data/
│   ├── customers.csv
│   ├── orders.csv
│   ├── products.csv
│   └── payments.csv
│
├── outputs/
│   ├── monthly_revenue_trnd.png
│   ├── top_10_products_by_revenue.png
│   └── power_bi_dashboard.png
│
├── notebooks/
│   └── E-commerce_analysis.ipynb
│
├── src/
│   └── E-commerce_pipeline.py
│
├── README.md
└── requirements.txt

10. Key Learnings

Through this project, I gained practical experience in:

- Python programming for data analytics.
- Data cleaning and preprocessing.
- Handling missing and duplicate records.
- Data validation and integration.
- Pandas DataFrame operations.
- GroupBy, aggregation, and merge operations.
- Business metric calculations.
- Data visualisation.
- Creating reusable data-processing functions.
- Managing projects using GitHub.

