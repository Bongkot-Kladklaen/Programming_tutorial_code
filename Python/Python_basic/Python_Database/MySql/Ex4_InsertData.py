import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_basic_db"
)

mycursor = mydb.cursor()

#* Insert Into Table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# value = ("John", "Highway 21")
# mycursor.execute(sql,value)

#* Insert Multiple Vaule
value = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql,value)

mydb.commit()

print(mycursor.rowcount,"Successfully")