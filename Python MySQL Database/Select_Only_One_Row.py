''' Python MySQL Database '''

# Select Only One Row

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",          # Use here yourusername
    password = "",          # Use here YourPassword
    database = "atlas"      # Connect your database
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

# fetchone() select only one row
myresult = mycursor.fetchone()

print(myresult)

