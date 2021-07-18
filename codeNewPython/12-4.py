import sqlite3 
try :
    conn = sqlite3.connect('test.db')
    conn.execute("UPDATE product SET prodName = 'Galaxy J7'  WHERE prodID = 3")
    conn.commit()
    print('Update successfully')
except conn.Error as e:
    conn.rollback()
    print('Error %s:' % e.args[0])
finally:
    if conn:
        conn.close()
