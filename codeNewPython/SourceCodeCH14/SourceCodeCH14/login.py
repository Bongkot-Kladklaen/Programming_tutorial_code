#!C:\Python36\python
import cgi, cgitb
cgitb.enable()
def header():
   print("Content-Type: text/html")
   print()
formpage='''<HTML><HEAD><TITLE>Login</TITLE></HEAD><BODY align="center">
<H1>ล็อกอินเข้าสู่ระบบ</H1><HR>
<FORM method="POST" action="login.py">
<p>ชื่อผู้ใช้ : <input type="text" name="login"></p>
<p>รหัสผ่าน : <input type="password" name="password"></p>
<p><input type="submit" value="ล็อกอิน">
<input type="reset" value="เคลียร์"></p>
</FORM>
<HR></BODY></HTML>'''

data = cgi.FieldStorage(keep_blank_values="true")
usr = "tanong"
pwd = "secret"
if not data:
   header()
   print(formpage)
elif not data.getvalue('login') or not data.getvalue('password'):
   header()
   print("<H1>กรุณากลับไปเติมข้อมูลให้ถูกต้อง</H1>")
elif data['login'].value != usr or data['password'].value != "secret":
   header()
   print("<H1>ชื่อหรือรหัสผ่านไม่ถูกต้อง</H1>")
else:
   header()
   print("<H1>เข้าสู่ระบบแล้ว</H1>")
   print("ยินดีต้อนรับคุณ ", data.getvalue('login'))

