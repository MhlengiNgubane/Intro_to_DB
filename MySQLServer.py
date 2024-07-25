import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='username',
        password='password'
    )

    # Check if connection is successful
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create alx_book_store database if it doesn't exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        
        # Execute SQL query
        try:
            cursor.execute(create_db_query)
            print("Database 'alx_book_store' created successfully!")
        except Error as e:
            print(f"Error executing query: {e}")
        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()
    else:
        print("Error connecting to MySQL server.")

except Error as e:
    print(f"Error connecting to MySQL: {e}")
