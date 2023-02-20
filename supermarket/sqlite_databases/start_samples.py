# Chat Openai 2_22_23
import sqlite3

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect('database.db')

# Create a cursor
cursor = conn.cursor()

# Create the customers table
cursor.execute('''
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL
)
''')

# Create the orders table
cursor.execute('''
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    total_amount REAL NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

