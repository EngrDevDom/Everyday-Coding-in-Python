''' Python MySQL Database '''

# Check Database Exist

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",      # Use here yourusername
    password = ""       # Use here YourPassword
)

mycursor = mydb.cursor()

# Check if created Database exist
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

