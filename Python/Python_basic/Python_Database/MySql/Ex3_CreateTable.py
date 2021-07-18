import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_basic_db"
)

mycursor = mydb.cursor()

# Creating a Table
sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
# mycursor.execute(sql)

#If the table already exists, use the ALTER TABLE keyword:
addsql = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
mycursor.execute(addsql)