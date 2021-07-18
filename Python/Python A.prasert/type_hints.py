from datetime import date

def beta(a: str):
    print(a.upper())

def dateTime(a: date, b):
    print(a.year)
    print(b.year)

def bar(a, b) -> str:
    return a + b

class Person:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def foo(self):
        print("hello")

def epsilon(a: Person,b):
    a.foo()
    
if __name__ == "__main__":
    # beta("Hello")
    # t1 = date(2016, 7, 20)
    # t2 = date(2017, 1, 9)
    # dateTime(t1,t2)
    p = Person("Peter","Parker",25)