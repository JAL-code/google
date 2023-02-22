# Chat Openai 2_22_23
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor
cursor = conn.cursor()

# Retrieve all customers from the customers table
cursor.execute("SELECT * FROM customers")
customers = cursor.fetchall()

# Print the customers
print("Customers:")
for customer in customers:
    print("ID: {}, Name: {}, Address: {}".format(customer[0], customer[1], customer[2]))

# Retrieve all orders from the orders table
cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()

# Print the orders
print("\nOrders:")
for order in orders:
    print("ID: {}, Customer ID: {}, Order Date: {}, Total Amount: {}".format(order[0], order[1], order[2], order[3]))

# Close the connection
conn.close()
