import pymysql
db = pymysql.connect("localhost", "root","", "order_db",
                     use_unicode=True,charset="utf8")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
ver = cursor.fetchone()
print("Database version : %s " % ver)
db.close()
