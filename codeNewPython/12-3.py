import sqlite3
print('ProductID \tProductName  \tPrice')
print('--------------------------------------------')
try :
    conn = sqlite3.connect('test.db')
    data = conn.execute('SELECT * FROM product')
    for row in data :
        print ('  ', row[0], '\t\t', row[1], '\t', row[2])
except conn.Error as e:
    print('Error %s:' % e.args[0])
finally:
    if conn:
        conn.close()
