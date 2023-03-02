# Chat Openai 2_22_23
import sqlite3

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect('database2.db')

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
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
''')

cursor.execute('''
    ALTER TABLE orders
    ADD CONSTRAINT valid_status CHECK (status IN ('completed', 'waiting pickup', 'missing items', 'waiting items', 'to be delivered', 'needs payment', 'canceled'))
''')

# Create the orders table
cursor.execute('''
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    available_date DATE NOT NULL,
    price_amount REAL NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

