''' Python MySQL Database '''

# Check Table Exist

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",          # Use here yourusername
    password = "",          # Use here YourPassword
    database = "atlas"      # Connect your database
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

