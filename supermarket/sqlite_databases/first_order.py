# Chat Openai 2_22_23

import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor
cursor = conn.cursor()

# Add customer to the customers table
customer_data = ('John Smith', '1 Apple Rd, Beverly MA 01915-5300')
cursor.execute("INSERT INTO customers (name, address) VALUES (?, ?)", customer_data)
customer_id = cursor.lastrowid

# Add order to the orders table
order_data = ('000000001', customer_id, '2023-02-21', 2313.90)
cursor.execute("INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES (?, ?, ?, ?)", order_data)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
