# Chat Openai 2_22_23
import sqlite3

def move_closed_orders(month):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Execute the query to move orders
    c.execute('''
    INSERT INTO closed_orders
    SELECT *
    FROM orders
    WHERE status IN ('completed', 'canceled') AND strftime('%Y-%m', order_date) = ?
    ''', (month,))

    # Delete the moved orders from the orders table
    c.execute('''
    DELETE FROM orders
    WHERE status IN ('completed', 'canceled') AND strftime('%Y-%m', order_date) = ?
    ''', (month,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
