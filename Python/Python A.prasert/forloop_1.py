def loop1():
    for i in range(11):
        print(i)

def loop2():
    for i in range(1,11):
        print(i)
def loop3():
    for i in range(1,11,2):
        print(i)
        print("-----")
    print("Bye")
def loopStr():
    s = "hello"
    for c in s:
        print(c)
def loopTuple():
    flowers = ("lily","jasmine")
    for f in flowers:
        print(f)
def loopTuple2():
    flowers = ("lily","jasmine","rose")
    for i in range(len(flowers)):
        print(i + 1, flowers[i], sep=".")
if __name__ == "__main__":
    # loop1()
    # loop2()
    # loop3()
    # loopStr()
    # loopTuple()
    loopTuple2()