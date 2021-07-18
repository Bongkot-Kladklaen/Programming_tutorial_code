import sqlite3
try :
    conn = sqlite3.connect('test.db')
    conn.execute('''CREATE TABLE product
        (prodID INT PRIMARY KEY NOT NULL,
        prodName TEXT,
        price REAL);''')
    print('Table created successfully')
except conn.Error as e :
    print('Error %s:' % e.args[0])
conn.close()
