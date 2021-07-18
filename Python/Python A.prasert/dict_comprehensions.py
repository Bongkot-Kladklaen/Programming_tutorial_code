import datetime 
def demo():
    t = [('sun','red'), ('mon','yellw'), ('tue','pink'),('wed','green'),('thu','orange'),('fri','blue'),('sat','purple')]
    d = {}
    for k, v in t:
        d[k] = v
    print(d)

    d1 = {k.capitalize(): v for k,v in t}
    print(d1)

    today = datetime.datetime.now()
    print(today.strftime("%a"))
    weekday = today.strftime("%a")
    weekcolor = d1[weekday]
    print(weekday, weekcolor)

import csv
def demo2():
    weekdays = ["sun","mon", "tue", "wed", "thu", "fri", "sat"]
    wekkcolors = ['red','yellow','pink','green','orange','blue','purple']
    t = zip(weekdays, wekkcolors)
    d1 = {k.capitalize(): v for k,v in t}
    print(d1)

def nato_from_file():
    with open("nato.txt") as f:
        d = {line[0]:line[:-1] for line in f}
        return d
def convert(s):
    d = nato_from_file()
    r = [d[c.upper()] for c in s]
    return " ".join(r)
    
def abbr_province_dict():
    with open("abbr_province.txt", encoding='utf-8') as f:
        data = csv.reader(f)
        d = {k:v for k, v in data}
        return d
# demo2()
# print(nato_from_file())
# print(convert("python"))
p = abbr_province_dict()
print(p)
print(p["ชพ"])