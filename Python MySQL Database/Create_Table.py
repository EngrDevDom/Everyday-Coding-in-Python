''' Python MySQL Database '''

# Create Table

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",          # Use here yourusername
    password = "",          # Use here YourPassword
    database = "atlas"      # Connect your database
)

mycursor = mydb.cursor()

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

