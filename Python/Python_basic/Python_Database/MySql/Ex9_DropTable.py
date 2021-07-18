import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_basic_db"
)

mycursor = mydb.cursor()
sql = "DROP TABLE customers"

#* Delete table if it exists
# sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)