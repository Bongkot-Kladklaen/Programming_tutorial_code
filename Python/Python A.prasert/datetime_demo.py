# import datetime
from datetime import date,datetime

def demo():
    today = date.today()
    print(today)
    dt = datetime.today()
    print(dt)
    print(today.month)
    print(today.day)
def demo2():
    songkran = date(2016,4,13)
    print(songkran)
    bd = datetime(1995,7,20,17,40,35)
    print(bd)
def demo3():
    d1 = datetime.strptime("20160413", "%Y%m%d")
    print(d1)
    d2 = datetime.strptime("20160413", "%Y%m%d").date()
    print(d2)
    d3 = datetime.strptime("05/09/2106", "%d/%m/%Y").date()
    print(d3)
    d4 = datetime.strptime("5/09/2106T06:45", "%d/%m/%YT%H:%M")
    print(d4)
demo3()
