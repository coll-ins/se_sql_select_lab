# STEP 1A
# Import SQL Library and Pandas
import sqlite3 
import pandas as pd
# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("Select employeeNumber, lastName From employees", conn)

print(df_first_five)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("Select lastName, employeeNumber From employees", conn)

print(df_five_reverse)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("Select lastName, employeeNumber AS ID From employees", conn)

print(df_alias)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql(
    "Select *,Case   When jobtitle = 'President' or jobtitle = 'VP Sales' or jobtitle = 'VP Marketing' Then 'Executive' Else 'Not Executive' END AS role From employees", conn)

print(df_executive)
# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("Select LENGTH(lastName) AS name_length From employees", conn)

print(df_name_length)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""Select  Substr(jobtitle, 1,2) AS short_title From employees""", conn)

print(df_short_title)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql(""" 
Select SUM(ROUND(priceEach * quantityOrdered, 0)) AS totalPrice 
From orderDetails""", conn).iloc[:, 0]

print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year =pd.read_sql("""
Select orderDate,
    Substr(orderDate, 9, 2) AS day,
    Substr(orderDate, 6, 2) AS month,
    Substr(orderDate, 1, 4) AS year
From orders
""", conn)

print(df_day_month_year)
