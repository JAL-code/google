# Chat Openai 2_22_23

import sqlite3

def create_orders_table():
    # Connect to or create a SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Create the table
    c.execute('''CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, FOREIGN KEY(customer_id) REFERENCES customers(customer_id))''')
    
    # Save changes and close the connection
    conn.commit()
    conn.close()
