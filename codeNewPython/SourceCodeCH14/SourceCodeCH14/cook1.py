#!C:\Python36\python
import time
from http import cookies
cookie = cookies.SimpleCookie()
cookie["name"] = 'tanong'
cookie["date_visited"] = str(time.time())
print(cookie.output())
print("Content-Type: text/html")
print()
print("เนื้อหาในหน้าเว็บแรก")
