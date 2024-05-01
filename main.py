import pandas as pd
import matplotlib.pyplot as plt

# reading the walmart dataset
walmart_data = pd.read_excel("walmart_sales.xlsx")

# PART A OF THE TASK

# calculating the sales according to each product line
walmart_data['Total Sales'] = walmart_data['Unit price'] * walmart_data['Quantity']
branch_sales_by_product = walmart_data.groupby(['City', 'Branch', 'Product line'])['Total Sales'].sum().reset_index()

# calculating the total sales of each branch
total_branch_sales = branch_sales_by_product.groupby(['City', 'Branch'])['Total Sales'].sum().reset_index()

# calculatng the total sales of each city
total_city_sales = total_branch_sales.groupby('City')['Total Sales'].sum().reset_index()

print("\nTotal sales of each branch according to Product line :  ")
print(branch_sales_by_product)

print("\nTotal sales for each branch : ")
print(total_branch_sales)

print("\nTotal sales of each city : ")
print(total_city_sales)

# PART B OF THE TASK

average_price_of_each_product = walmart_data.groupby(['City','Branch','Product line'])['Unit price'].mean().reset_index()

average_price_of_each_product_by_branch = average_price_of_each_product.groupby(['City', 'Branch'])['Unit price'].mean().reset_index()

average_price_of_each_product_by_city = average_price_of_each_product_by_branch.groupby(['City'])['Unit price'].mean().reset_index()

print("\n Average price of each product in each branch : ")
print(average_price_of_each_product)

print('\n Average price of each product by branch : ')
print(average_price_of_each_product_by_branch)

print('\n Average price of each product by each City : ')
print(average_price_of_each_product_by_city)

# PART C OF THE TASK

walmart_data['Date'] = pd.to_datetime(walmart_data['Date'])

walmart_data['Month'] = walmart_data['Date'].dt.month

data_of_previous_months = walmart_data[(walmart_data['Date'].dt.year == 2019) & (walmart_data['Date'].dt.month < 4)]

data_groupedby = data_of_previous_months.groupby(['Product line', 'Gender', 'Payment', 'Month'])

previous_month_sales = data_groupedby.apply(lambda x : (x['Unit price'] * x['Quantity']).sum()).unstack()

print(previous_month_sales)

# VISUALISING THE SALES FOR BETTER UNDERSTANDING OF SALES FORECAST OF NEXT MONTH

sales = previous_month_sales.stack().unstack('Month')

sales.plot(kind='bar', figsize=(14,8))
plt.title('Total sales by Product line, Gender, Payment method')
plt.xlabel('Product line, Gender, Payment method')
plt.ylabel('Total sales')
plt.xticks(rotation=45)
plt.legend(title='Month')
plt.tight_layout()
plt.show()