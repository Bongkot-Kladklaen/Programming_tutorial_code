import pymysql
db = pymysql.connect("localhost", "root","", "order_db",
                     use_unicode=True,charset="utf8")
cursor = db.cursor()
cursor.execute('''CREATE TABLE custdetail(custID int(2) UNSIGNED NOT NULL AUTO_INCREMENT,
    name varchar(50) DEFAULT NULL, address varchar(200) DEFAULT NULL,
    tel varchar(20) DEFAULT NULL, primary key(custID))''')
db.close()
