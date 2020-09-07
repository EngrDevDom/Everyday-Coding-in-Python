''' Python MySQL Database '''

# Delete Record

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",      # Use here yourusername
    password = "",       # Use here YourPassword
    database = "atlas"  # Connect your database
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

