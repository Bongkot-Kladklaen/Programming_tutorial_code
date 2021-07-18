import pymysql
db = pymysql.connect( "localhost", "root",  "",  "order_db",
                      use_unicode=True, charset="utf8")       
cursor = db.cursor()
sql = "UPDATE custdetail SET name = 'เส้งโห โลตัสพัทลุง', address='115 ม.2 ต.เขาเจียก อ.เมือง \
จ.พัทลุง 93000', tel = '074-620033' WHERE custID = 1"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

sql = "SELECT * FROM custdetail WHERE custID = 1"
cursor.execute(sql)
row = cursor.fetchone()
print(row[0],'\t', row[1],'\t', row[2],'\t', row[3])
db.close()
