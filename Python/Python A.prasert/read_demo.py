def demo_reader():
    f = open("flower.txt")
    data = f.read()
    print(data)
    f.close()
def demo_readline():
    f = open("flower.txt")
    data = f.readline() # readline อ่านที่ละแถว
    print(data)
    f.close()
def demo_readline2():
    f = open("flower.txt")
    for i in range(3):
        print(f.readline(), end="")
    f.close()
def demo_readlines():
    f = open("flower.txt")
    data = f.readlines() # readlines ส่งค่ากลับมาเป็น list และมี \n ติดมาด้วย
    print(data)
    f.close()

# demo_reader()
# demo_readline()
demo_readline2()
# demo_readlines()