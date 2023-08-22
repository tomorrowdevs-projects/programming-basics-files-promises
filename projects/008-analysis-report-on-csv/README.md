# Analysis Report on CSV

Reading data from a CSV file and performing analysis to generate a report summarizing the data.


### Features

**Clean Data**.
Remove any duplicate lines.

**OrderID Analysis**.   
Count the total number of unique OrderIDs to determine the total number of orders.

**Product Analysis**.  
Count the occurrences of each unique product to identify the most popular products.
Calculate the average price of products to understand the pricing distribution.

**Category Analysis**.   
Count the occurrences of products in each category to determine the distribution of products across categories.
Calculate the total sales revenue for each category by summing the (Price * Quantity) for each product.

**Price Analysis**.   
Calculate the average, minimum, and maximum prices to understand the price range of products.

**Quantity Analysis**.   
Calculate the total quantity sold for each product and category to identify high-demand items.

**Customer Analysis**.   
Count the number of orders placed by each customer to identify the most active customers.
Calculate the total amount spent by each customer to identify high-value customers.

**Generate report**
Generates and prints a summary report based on the analysis. 
The report may include calculated statistics, patterns observed, and any other relevant insights

### Define functions
- read csv, accepts a filename as input and return the data.
- order id analysis,
- product analysis,
- category analysis,
- price analysis,
- quantity analysis,
- customer analysis,
- generate report, accepts the analysis results. 

Feel free to create as many functions as you see fit.


Implement error handling to handle cases where the CSV file is not found or there is an issue with the data format.


# Documentation

For this project solution you may use:

- Files and Exceptions

# Deadline

This project requires to be completed in a maximum of **4 hours**
