''' Python MySQL Database '''

# Delete a Table

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",      # Use here yourusername
    password = "",       # Use here YourPassword
    database = "atlas"  # Connect your database
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)

