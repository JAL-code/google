# Chat Openai 2_22_23
import sqlite3
from typing import List

def create_query_list(command, item_str):
    # create a custom query (JAL)
    pragma_list = list()
    pragma_list.append("PRAGMA ")
    pragma_list.append(command)
    pragma_list.append("(")
    pragma_list.append(item_str)
    pragma_list.append(")")
    print(f"Pragma Request: {pragma_list}")
    return pragma_list

def create_query(query_list: List[str]) -> str:
    # convert list to a query (JAL)
    sum_str = "".join(query_list[x] for x in range(0,len(query_list)))
    return sum_str

def setup_connection():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    return conn

def close_connection(conn):
    # Close the connection
    conn.close()

def PRAGMA_database_metrics(conn):

    # Create a cursor
    cursor = conn.cursor()

    # Execute PRAGMA statement to get tables
    cursor.execute("SELECT name from sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"Tables accessed: {tables}")

    # Print the list of tables
    for table in tables:
        print(table[0])
        
        pragma_list = "table_info"

        temp_list = create_query_list(pragma_list, table[0])
        current_command = create_query(temp_list)

        # Execute the first PRAGMA statement
        cursor.execute(current_command)
        columns = cursor.fetchall()
        print(columns)

        pragma_list = "foreign_key_list"

        temp_list = create_query_list(pragma_list, table[0])
        current_command = create_query(temp_list)

        # Execute the second PRAGMA statement
        cursor.execute(current_command)
        foreign_keys = cursor.fetchall()
        
        # Find the primary key column
        for column in columns:
            if column[-1] == 1:
                primary_key_column = column[1]
                break

        # Print the results
        print("Columns:")
        for column in columns:
            print("{}: {}".format(column[1], column[2]))

        print("\nForeign keys:")
        for foreign_key in foreign_keys:
            print("{}: {}".format(foreign_key[2], foreign_key[3]))

        print("\nPrimary key column: {}".format(primary_key_column))

conn1 = setup_connection()
PRAGMA_database_metrics(conn1)
close_connection(conn1)
