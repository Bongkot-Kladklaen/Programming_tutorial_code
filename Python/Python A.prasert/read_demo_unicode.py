def demo_reader():
    with open("flower.txt") as f:
        print(f.name)
        print(f.mode)
        data = f.read()
        print(data)

def demo_reader_unicode():
    with open("province.txt", mode='r',encoding='utf-8') as f:
        print(f.name)
        print(f.mode)
        data = f.read()
        print(data)

def demo_reader_unicode2():
    with open("province.txt", mode='r',encoding='utf-8') as f:
       for i,line in enumerate(f):
           print("{}. {}".format(i, line), end="")

demo_reader_unicode2()