#!C:\Python36\python
import cgi, cgitb, pymysql
cgitb.enable()
def header():
    print("Content-Type: text/html")
    print()
data = cgi.FieldStorage()
if "name" not in data or "address" not in data or "tel" not in data :
    header()
    print("<H1>มีข้อผิดพลาด</H1>")
    print("กรุณาเพิ่มข้อมูลให้ครบถ้วน")
    exit()
name = data['name'].value
address = data['address'].value
tel = data['tel'].value
db = pymysql.connect("localhost", "root", "", "order_db", use_unicode=True, charset="utf8")
cursor = db.cursor()
sql = '''INSERT INTO custdetail(name, address, tel) VALUES ("%s", "%s", "%s")'''%(name, address, tel)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
header()
print("<H1>เพิ่มข้อมูลลูกค้าใหม่เรียบร้อยแล้ว</H1>")

                     

