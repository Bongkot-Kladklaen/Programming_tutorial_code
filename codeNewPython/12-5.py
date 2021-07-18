import sqlite3
try :
    conn = sqlite3.connect('test.db')
    conn.execute('DELETE from product WHERE prodID = 2')
    conn.commit()
    print('Deleted successfully')
except conn.Error as e :
    conn.rollback()
    print('Error %s:' % e.args[0])
finally:
    if conn:
        conn.close()
