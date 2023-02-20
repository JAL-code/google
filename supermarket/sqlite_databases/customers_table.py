# Chat Openai 2_22_23

import sqlite3

def create_customers_table():
    # Connect to or create a SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Create the table
    c.execute('''CREATE TABLE customers (name TEXT, address TEXT, customer_id INTEGER PRIMARY KEY)''')
    
    # Save changes and close the connection
    conn.commit()
    conn.close()
