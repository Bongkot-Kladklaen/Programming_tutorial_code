#!C:\Python36\python
import cgi, cgitb
cgitb.enable()
data = cgi.FieldStorage(keep_blank_values="true")
print("Content-Type: text/html")
print()
print("<p>ชื่อ:", data['name'].value)
if data['sex'].value == "1":
   print("<p>เพศ: ชาย")
else: print("<p>เพศ: หญิง")
if data['carr'].value == "1":
   print("<p>อาชีพ: นักเรียน/นักศึกษา")
elif data['carr'].value == "2":
   print("<p>อาชีพ: พนักงานบริษัท")
elif data['carr'].value == "3":
   print("<p>อาชีพ: เกษตรกร")
elif data['carr'].value == "4":
   print("<p>อาชีพ: นักธุรกิจ")
else: print("<p>อาชีพ: นักกีฬา")
if data.getvalue('movie'):
   movie = "ดูหนังฟังเพลง"
else: movie = ""
if data.getvalue('game'):
   game = " เล่นเกม"
else: game = ""
if data.getvalue('read'):
   read = " อ่านหนังสือ"
else: read = ""
print("<p>งานอดิเรก:", movie+game+read)
print("<p>ชอบเราที่:", data['fav'].value)

