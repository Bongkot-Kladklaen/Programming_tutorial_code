#!C:\Python36\python
from http import cookies
import time, os
cook = os.environ.get("HTTP_COOKIE")
cookie = cookies.SimpleCookie(cook)
user = cookie.get("name")
lasttime = cookie.get("date_visited")
#dtime = str(time.ctime(int(lasttime)))
if user == None:
    cookie = cookies.SimpleCookie()
    cookie["name"] = "amrin"
    cookie["date_visited"] = str(time.time())
    print(cookie)
    msg = "<p>คุณคือ -> %s</p>" % cookie["name"].value
else:
    dtime = time.ctime(float(lasttime.value))
    msg = "<p>ขอต้อนรับอีกครั้งคุณ -> %s, เยี่ยมชมล่าสุด : %s</p>" % (user.value, dtime)                             
print("Content-Type: text/html")
print()
print(msg)
print("<h1>เนื้อหาหน้าเว็บที่สอง</h1>")
