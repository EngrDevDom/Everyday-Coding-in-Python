''' Python MySQL Database '''

# Create Database

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",      # Use here yourusername
    password = ""       # Use here YourPassword
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE atlas")

