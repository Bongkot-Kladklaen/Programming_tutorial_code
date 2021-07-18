
#* Creating a Database
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()
sql = "CREATE DATABASE python_basic_db"
mycursor.execute(sql)

#* Check if Database Exists
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

