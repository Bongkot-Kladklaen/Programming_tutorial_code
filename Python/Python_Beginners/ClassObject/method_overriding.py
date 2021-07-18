class A:
    def display(self):
        print('method belongs to class A')

class B(A):
    def display(self):
        print('method belongs to class B')

b1 = B()
b1.display()