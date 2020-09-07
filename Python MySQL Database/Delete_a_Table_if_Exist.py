''' Python MySQL Database '''

# Delete a Table if Exist

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",      # Use here yourusername
    password = "",       # Use here YourPassword
    database = "atlas"  # Connect your database
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)

