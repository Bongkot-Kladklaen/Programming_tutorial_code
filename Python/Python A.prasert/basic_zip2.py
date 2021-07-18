from itertools import cycle
def demo1():
    weight = [70,60,48,50]
    height = [170,175,161]
    return [w/(h/100) ** 2 for w, h in zip(weight,height)]

def demo2():
    weight = [70,60,48,50,55]
    height = [170,175,161]
    [print(w, h) for w,h in zip(cycle(weight), cycle(height))] # ใส่ cycle ทั้งคู่มันจะรันไปไม่มีหยุด

def demo3():
    weight = [70,60,48,50,55]
    height = [170,175,161]
    z = zip(weight, height) # generators
    # print(z)
    print(next(z))
    print(next(z))
    print(next(z))
# demo2()
demo3()