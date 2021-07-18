#!C:\Python36\python
import cgi, cgitb
cgitb.enable()
data = cgi.FieldStorage()
print("Content-Type: text/html")
print()
if "name" not in data or "age" not in data:
    print("<H1>มีความผิดพลาด</H1>")
    print("กรุณาป่อนชื่อและอายุของคุณ")
    exit()
print("<p>ชื่อ:", data['name'].value)
print("<p>อายุ:", data['age'].value)
