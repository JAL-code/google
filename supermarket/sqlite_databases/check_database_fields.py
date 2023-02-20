# Chat Openai 2_22_23
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor
cursor = conn.cursor()

# Specify the table name
table_name = "customers"

# Execute the PRAGMA statement to retrieve the columns
cursor.execute("PRAGMA table_info({})".format(table_name))

# Fetch the results
columns = cursor.fetchall()

# Close the connection
conn.close()

# Print the list of columns
for column in columns:
    print("{}: {}".format(column[1], column[2]))
