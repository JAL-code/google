# Chat Openai 2_22_23
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor
cursor = conn.cursor()

# Retrieve the number of customers in the customers table
cursor.execute("SELECT COUNT(*) FROM customers")
num_customers = cursor.fetchone()[0]

# Print the number of customers
print("Number of customers: {}".format(num_customers))

# Retrieve the number of orders in the orders table
cursor.execute("SELECT COUNT(*) FROM orders")
num_orders = cursor.fetchone()[0]

# Print the number of orders
print("Number of orders: {}".format(num_orders))

# Close the connection
conn.close()
