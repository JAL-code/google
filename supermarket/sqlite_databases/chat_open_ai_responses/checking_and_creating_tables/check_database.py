# Chat Openai 2_22_23
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor
cursor = conn.cursor()

# Execute the SELECT statement
cursor.execute("SELECT name from sqlite_master WHERE type='table'")

# Fetch the results
tables = cursor.fetchall()

# Close the connection
conn.close()

# Print the list of tables
for table in tables:
    print(table[0])