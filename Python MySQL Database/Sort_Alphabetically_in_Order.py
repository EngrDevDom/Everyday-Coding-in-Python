''' Python MySQL Database '''

# Sort Alphabetically in Order

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",      # Use here yourusername
    password = "",       # Use here YourPassword
    database = "atlas"  # Connect your database
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

