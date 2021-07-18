import sqlite3
try :
    conn = sqlite3.connect('test.db')
    conn.execute('DROP TABLE IF EXISTS product')
    print('Drop table successfully')
except conn.Error as e :
    print('Error %s:' % e.args[0])
finally:
    if conn:
        conn.close()
