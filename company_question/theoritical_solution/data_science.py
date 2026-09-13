# ============================================================
# DATA SCIENCE INTERVIEW QUESTIONS & ANSWERS
# SQL + PYTHON + DATA QUALITY + BUSINESS ANALYTICS
# ============================================================


# ============================================================
# 1) SQL DATA EXTRACTION
# ============================================================

# Q1) How would you calculate daily revenue and compare it with
#     the previous day using SQL?
#
# Answer:
# I would calculate daily revenue using SUM() and GROUP BY date.
# Then I would use the LAG() window function to get the previous
# day's revenue and calculate the absolute or percentage change.


# ============================================================
# 2) TOP PRODUCTS
# ============================================================

# Q2) How would you find the top 5 products by revenue in each category?
#
# Answer:
# I would first calculate total revenue for each product using
# SUM() and GROUP BY. Then I would use ROW_NUMBER() or RANK()
# with PARTITION BY category to select the top 5 products.


# ============================================================
# 3) WHERE vs HAVING
# ============================================================

# Q3) What is the difference between WHERE and HAVING? Give an example.
#
# Answer:
# WHERE filters individual rows before grouping, while HAVING
# filters groups after GROUP BY.
#
# Example:
# WHERE price > 500
# HAVING SUM(sales) > 10000


# ============================================================
# 4) DUPLICATE ORDERS
# ============================================================

# Q4) How would you identify duplicate orders in a database?
#
# Answer:
# I would group the data by the order_id and use COUNT().
# If an order_id has a count greater than 1, it may be a duplicate.
#
# Example:
# SELECT order_id, COUNT(*)
# FROM orders
# GROUP BY order_id
# HAVING COUNT(*) > 1;


# ============================================================
# 5) MONTHLY ACTIVE CUSTOMERS
# ============================================================

# Q5) How would you calculate monthly active customers using SQL?
#
# Answer:
# I would group the customer activity by month and count
# DISTINCT customer_id.
#
# Example:
# COUNT(DISTINCT customer_id)
#
# This gives the number of unique customers active in each month.


# ============================================================
# 6) CUSTOMER RETENTION
# ============================================================

# Q6) How would you calculate customer retention using SQL?
#
# Answer:
# I would identify customers from the starting period and then
# check how many of them returned in the following period.
#
# Retention Rate =
# Returning Customers / Customers in Starting Period * 100


# ============================================================
# 7) JOIN DUPLICATION
# ============================================================

# Q7) What happens if a JOIN creates duplicate rows, and how would
#     you identify the problem?
#
# Answer:
# A JOIN can create duplicate rows when one record matches multiple
# records in another table. I would check row counts before and
# after the JOIN and check the join keys for duplicates.


# ============================================================
# 8) PERCENTAGE REVENUE CHANGE
# ============================================================

# Q8) How would you calculate the percentage change in revenue
#     from one month to another?
#
# Answer:
# I would compare the current month's revenue with the previous
# month's revenue.
#
# Percentage Change =
# (Current Revenue - Previous Revenue) / Previous Revenue * 100


# ============================================================
# 9) MISSING VALUES
# ============================================================

# Q9) How do you handle missing values in a dataset?
#
# Answer:
# First, I check why the values are missing. Depending on the data,
# I may remove the rows, fill the values using mean/median/mode,
# or use a business-specific value. I avoid blindly filling values.


# ============================================================
# 10) DUPLICATES IN PANDAS
# ============================================================

# Q10) How would you identify and remove duplicate records using Pandas?
#
# Answer:
# I would use duplicated() to identify duplicates and
# drop_duplicates() to remove them.
#
# Example:
# df[df.duplicated()]
# df.drop_duplicates()


# ============================================================
# 11) OUTLIERS
# ============================================================

# Q11) How would you detect outliers in a dataset?
#
# Answer:
# I can use methods such as the IQR method or Z-score.
# For example, with IQR, values below Q1 - 1.5*IQR or above
# Q3 + 1.5*IQR can be considered potential outliers.
# I would then check whether they are errors or genuine values.


# ============================================================
# 12) GROUP SALES USING PANDAS
# ============================================================

# Q12) How would you group sales by product category using Pandas?
#
# Answer:
# I would use groupby() with sum() to calculate total sales
# for each category.
#
# Example:
# df.groupby("category")["sales"].sum()


# ============================================================
# 13) COMBINING DATASETS
# ============================================================

# Q13) How would you combine two datasets using Pandas?
#
# Answer:
# If the datasets have a common key, I would use merge().
# For example, I can combine orders and customer data using
# customer_id.
#
# Example:
# pd.merge(orders, customers, on="customer_id")


# ============================================================
# 14) REPRODUCIBLE PYTHON ANALYSIS
# ============================================================

# Q14) How do you make sure your Python analysis is reproducible?
#
# Answer:
# I keep the code organized, use clear variable names, document
# important steps, fix random seeds when required, and maintain
# the required package versions. This helps others reproduce
# the same results.


# ============================================================
# 15) DATA QUALITY CHECKS
# ============================================================

# Q15) What data-quality checks would you perform before using
#     a dataset for analysis?
#
# Answer:
# I would check for missing values, duplicates, incorrect data
# types, invalid or out-of-range values, and inconsistent records.
# I would also check whether important totals match the source data.


# ============================================================
# 16) SUDDEN 40% REVENUE DROP
# ============================================================

# Q16) How would you investigate a sudden 40% drop in reported revenue?
#
# Answer:
# First, I would check whether the data pipeline or SQL query has
# an issue. Then I would check orders, cancellations, refunds,
# missing data, and compare revenue by day, product, and region.
# This helps determine whether it is a data problem or a real business change.


# ============================================================
# 17) BUSINESS-CRITICAL MISSING DATA
# ============================================================

# Q17) How would you handle missing data when the missing values
#     are business-critical?
#
# Answer:
# I would first understand why the data is missing and whether it
# can be recovered from another source. If not, I would use a suitable
# imputation method or flag the records instead of making assumptions.


# ============================================================
# 18) VALIDATING A DASHBOARD KPI
# ============================================================

# Q18) How would you validate that a dashboard KPI is calculated correctly?
#
# Answer:
# I would independently calculate the KPI from the source data
# and compare it with the dashboard value. I would also check the
# filters, joins, date range, and calculation logic used in the dashboard.


# ============================================================
# 19) DIFFERENT REVENUE FROM TWO SOURCES
# ============================================================

# Q19) What would you do if two different data sources show
#     different revenue numbers?
#
# Answer:
# I would compare their definitions, filters, date ranges, and
# calculation methods. Then I would trace the data back to the
# source records to find where the difference is coming from.


# ============================================================
# 20) SALES DECREASE
# ============================================================

# Q20) How would you identify why sales have decreased this month?
#
# Answer:
# I would compare this month with previous months and break sales
# down by product, category, location, customer type, and channel.
# This helps identify where the biggest decrease happened and why.


# ============================================================
# 21) E-COMMERCE KPIs
# ============================================================

# Q21) Which KPIs would you track for an e-commerce company?
#
# Answer:
# Important KPIs include:
# - Revenue
# - Number of orders
# - Average Order Value (AOV)
# - Conversion rate
# - Customer retention
# - Customer acquisition cost (CAC)
# - Cancellation/return rate
# - Customer lifetime value (CLV)


# ============================================================
# 22) MOST VALUABLE CUSTOMERS
# ============================================================

# Q22) How would you identify the most valuable customers?
#
# Answer:
# I would look at metrics such as total spending, purchase frequency,
# and customer lifetime value. I could then rank customers based on
# these metrics and identify the highest-value customer groups.


# ============================================================
# 23) MARKETING CAMPAIGN SUCCESS
# ============================================================

# Q23) How would you determine whether a marketing campaign was successful?
#
# Answer:
# I would compare important metrics before and after the campaign,
# such as sales, conversion rate, new customers, and revenue.
# If possible, I would also compare the campaign group with a control
# group to measure the actual impact.


# ============================================================
# 24) INCREASE IN CUSTOMER CANCELLATIONS
# ============================================================

# Q24) How would you investigate a sudden increase in customer cancellations?
#
# Answer:
# I would compare cancellation rates over time and break them down
# by product, location, customer type, and reason for cancellation.
# I would also check for delivery delays, stock issues, or changes
# in business rules that could explain the increase.


# ============================================================
# 25) FROM ANALYSIS TO BUSINESS RECOMMENDATION
# ============================================================

# Q25) How would you convert your analysis into a recommendation
#     for a business stakeholder?
#
# Answer:
# I would first explain the main finding using clear numbers,
# then explain what caused it and its possible business impact.
# Finally, I would give a practical recommendation based on the data.
#
# Example:
# "Electronics sales increased by 20%, mainly because of headphones.
# We could increase stock and run targeted promotions for this category."


# ============================================================
# ⭐ INTERVIEW ANSWERING FORMULA
# ============================================================

# For most Data Science interview questions, remember:
#
#     DATA
#       ↓
#     ANALYSIS
#       ↓
#     VALIDATION
#       ↓
#     INSIGHT
#       ↓
#     BUSINESS ACTION
#
# Try to explain not only WHAT you would do,
# but also WHY you would do it.
#
# A strong answer usually contains:
#     1. Method / Tool
#     2. Short explanation
#     3. Validation
#     4. Business purpose
#
# Example:
# "I would use SQL to aggregate daily revenue, compare it with the
# previous day using LAG(), validate the numbers against the source,
# and then investigate large changes to understand the business reason."
#
# This sounds much more practical than simply saying:
# "I will use SQL to analyze the data."
# ============================================================