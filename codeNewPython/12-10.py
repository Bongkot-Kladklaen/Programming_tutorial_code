import pymysql
db = pymysql.connect( "localhost", "root",  "",  "order_db",
                      use_unicode=True, charset="utf8")       
cursor = db.cursor()
sql = "SELECT name, tel FROM custdetail WHERE custID BETWEEN 31 AND 35"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
      name = row[0]
      tel = row[1]
      print(row[0],'\t\t\t', row[1])
      #print ("Customer : %s,Tel. : %s" % name, tel)
except:
    print ("Error: unable to fetch data")
db.close()
