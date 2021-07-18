import pymysql
db = pymysql.connect( "localhost", "root",  "",  "order_db",
                      use_unicode=True, charset="utf8")       
cursor = db.cursor()
sql = "DROP TABLE custdetail"
cursor.execute(sql)
db.close()
