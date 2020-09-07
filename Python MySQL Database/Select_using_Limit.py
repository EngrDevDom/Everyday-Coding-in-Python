''' Python MySQL Database '''

# Select using Limit

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",          # Use here yourusername
    password = "",          # Use here YourPassword
    database = "atlas"      # Connect your database
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

