from functools import reduce

def demo():
    n = range(1,6)
    sum = 0
    for i in n:
        sum += i
    return sum
def demo1():
    n = range(1,6)
    sum = reduce(lambda cv,v: cv + v, n)
    return sum

def fac(n):
    fact = reduce(lambda cv,v: cv * v,range(1, n+1),1)
    return fact

def fac2(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f
if __name__ == "__main__":
    # print(demo())
    # print(demo1())
    print(fac(5))
    print(fac2(5))