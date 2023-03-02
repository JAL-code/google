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

# Find the primary key column
for column in columns:
    if column[-1] == 1:
        primary_key_column = column[1]
        break

# Print the primary key column
print("Primary key column: {}".format(primary_key_column))
