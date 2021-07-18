def demo1():
    flowers = ["lily","carnation","jasmine","rose","tulip"]
    flower2 = list(map(str.capitalize, flowers))
    print(flower2)

def usd2thb(usd):
    return usd * 33

def demo2():
    price_usd = [10,30,70,100]
    price_thb = [n * 33 for n in price_usd]
    price_thb2 = list(map(lambda n: n * 33, price_usd))
    price_thb3 = list(map(usd2thb, price_usd))
    print(price_thb)
    print(price_thb2)
    print(price_thb3)

def area():
    s = input("rai-ngan-sqwa ").split("-")
    # print(s)
    # lst_n = list(map(int, s))
    rai, ngan, sqwa = list(map(int, s))
    print(rai, ngan, sqwa)
    total = rai * 400 + ngan * 100 + sqwa
    print(total)

def area2():
    rai, ngan, sqwa = list(map(int, input("rai-ngan-sqwa ").split("-")))
    return rai * 400 + ngan * 100 + sqwa

if __name__ == "__main__":
    # demo1()
    # demo2()
    # area()
    print(area2())