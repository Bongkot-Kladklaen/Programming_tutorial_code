import pymysql
db = pymysql.connect( "localhost", "root",  "",  "order_db",
                      use_unicode=True, charset="utf8")       
cursor = db.cursor()
def show():
    sql = "SELECT * FROM custdetail WHERE custID BETWEEN 51 AND 55"
    cursor.execute(sql)
    results = cursor.fetchall()
    for rows in results:
        print(rows[0],'\t', rows[1],'\t', rows[2],'\t', rows[3])

show()
    
sql = "DELETE FROM custdetail WHERE custID = 52"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
print('\n\n After delete data')
show()
db.close()
