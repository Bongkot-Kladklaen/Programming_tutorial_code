class mom:
    def print(self):
        print('This is method of class mom')

class child(mom):
    def print(self):
        print('This is method of class child')

objA = mom()
objB = child()
objA.print()			
objB.print()
