class person:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("hello",self.name)

# main
p = person('Jaycop')
p.display()
person('bongkot').display()