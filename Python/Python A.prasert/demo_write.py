import csv

def demo1():
    with open("some1.csv",'a', newline="", encoding="utf8") as f:
        fw = csv.writer(f)
        # fw.writerow(["one", "two",'three'])
        # fw.writerow(("lily","carnation",'rose'))
        # fw.writerow(["th","thailand",'ประเทศไทย'])
        fw.writerow(["a","b","c"])

def demo2():
    menus = [
        ['mocha',30],
        ['latte',40],
        ['espresso',50]
    ]
    with open("some.csv",'w', newline="", encoding="utf8") as f:
        fw = csv.writer(f, delimiter="|", quoting=csv.QUOTE_NONNUMERIC)
        fw.writerow(["menu","s","m","l"])
        fw.writerows(menus)

demo1()
# demo2()