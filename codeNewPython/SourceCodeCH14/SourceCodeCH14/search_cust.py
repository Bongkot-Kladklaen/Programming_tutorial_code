#!C:\Python36\python
import cgi, cgitb, pymysql
cgitb.enable()
print("Content-Type: text/html")
print()
print("<h1>ผลลัพธ์การค้นหาข้อมูลลูกค้า</h1><p><HR><p>")
data = cgi.FieldStorage()
if "name" not in data :
    print("<H1>ผิดพลาด: กรุณากรอกชื่อ</H1>")
name = data['name'].value
db = pymysql.connect("localhost", "root", "", "order_db", use_unicode=True, charset="utf8")
cursor = db.cursor()
sql = "SELECT * FROM custdetail WHERE name = '%s'" % name
try:
    cursor.execute(sql)
    if not cursor.rowcount:
        print("<h1>ไม่มีลูกค้าชื่อนี้</h1>")
    else:
        print("<TABLE border='1'><TR><TD>ชื่อ</TD><TD>ที่อยู่</TD><TD>เบอร์โทร</TD></TR>")
        results = cursor.fetchall()
        for row in results:
            b = row[1] ; c = row[2] ; d = row[3]
            print("<TR><TD>%s</TD><TD>%s</TD><TD>%s</TD></TR>" % (b,c,d))
        print("</TABLE></BODY></HTML>")
except:
    print("<h1>ผิดพลาด: ไม่สามารถดึงข้อมูลได้<h1>")
db.close()




                     

