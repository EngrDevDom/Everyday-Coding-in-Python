''' Python MySQL Database '''

# Create Connection

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",      # Use here yourusername
    password = ""       # Use here YourPassword
)

print(mydb)

