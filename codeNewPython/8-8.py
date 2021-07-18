class A():
    __private = 'I am private'
    _protected = 'I am protected'
    public = 'I am public'
    def __init__(self):
        print('----------inside class---------')
        print(self.__private)
        print(self._protected)
        print(self.public)
    def printPV(self):
        print('Print private data : ',self.__private)

class B(A):
    def __init__(self):
        print('----------inside subclass---------')
        print(self._protected)
        print(self.public)
    

a = A()
b = B()
print('----------outside class---------')
print(a.public)
print(b.public)
b.printPV()

