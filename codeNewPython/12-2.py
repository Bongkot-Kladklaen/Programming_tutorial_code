import sqlite3
try :
    conn = sqlite3.connect('test.db')
    conn.execute('''INSERT INTO product (prodID,prodName,price)
        VALUES (1, 'Galaxy SIII', 7000.00 )''')
    conn.execute('''INSERT INTO product (prodID,prodName,price)
        VALUES (2, 'iPad mini', 12000.00 )''')
    conn.execute('''INSERT INTO product (prodID,prodName,price)
        VALUES (3, 'iPhone 5s', 17000.00 )''')
    conn.execute('''INSERT INTO product (prodID,prodName,price)
        VALUES (4, 'Galaxy NoteII', 13000.00 )''')
    conn.execute('''INSERT INTO product (prodID,prodName,price)
        VALUES (5, 'Galaxy Note8', 14000.00 )''')
    conn.commit()
    print('Records created successfully')
except conn.Error as e:
    if conn:
        conn.rollback()
        print('Error %s:' % e.args[0])
finally:
    if conn:
        conn.close()
