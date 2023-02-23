# Chat Openai 2_22_23

import sqlite3

"""
SELECT customers.name, orders.order_id, orders.order_date, orders.total_amount 
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_date = '2022-11-01'

SELECT customers.name, orders.order_id, orders.order_date, orders.total_amount 
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_date = '2022-11-01'
"""

def get_daily_sales_report(date):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Execute the query
    c.execute('''
    SELECT customers.name, orders.order_id, orders.order_date, orders.total_amount 
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
    WHERE orders.order_date = ?
    ''', (date,))

    # Fetch the results
    sales_report = c.fetchall()

    # Close the connection
    conn.close()

    return sales_report

def get_customer_sales_report(name, date):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Execute the query
    c.execute('''
    SELECT customers.name, orders.order_id, orders.order_date, orders.total_amount 
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
    WHERE orders.order_date = ? and customers.name = ?
    ''', (date,name))

    # Fetch the results
    sales_report = c.fetchall()

    # Close the connection
    conn.close()

    return sales_report

def get_customer_report(name):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Execute the query (note: name is passed as a tuple)
    c.execute('''
    SELECT customers.name, customers.address, orders.order_id, orders.total_amount 
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
    WHERE customers.name = ?
    ''', (name, ))

    # Fetch the results
    sales_report = c.fetchall()

    # Close the connection
    conn.close()

    return sales_report

def get_active_orders_report(name=None):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if name is None:
        # Query all customers who have an order
        c.execute('''
        SELECT customers.name, customers.address, orders.order_id, orders.total_amount
        FROM customers
        INNER JOIN orders ON customers.customer_id = orders.customer_id
        ''')
    else:
        # Query a specific customer's orders
        c.execute('''
        SELECT customers.name, customers.address, orders.order_id, orders.total_amount 
        FROM customers
        INNER JOIN orders ON customers.customer_id = orders.customer_id
        WHERE customers.name LIKE ?
        ''', (f'%{name}%',))

    # Fetch the results
    sales_report = c.fetchall()

    # Close the connection
    conn.close()

    return sales_report


sales_report = get_daily_sales_report('2023-02-21')
print(sales_report)
sales_report = get_customer_sales_report('John Smith','2023-02-21')
print(sales_report)
# ERROR: this method is not working.  Date is missing.
sales_report = get_customer_report('')
print(sales_report)
sales_report = get_active_orders_report('')
print(sales_report)

