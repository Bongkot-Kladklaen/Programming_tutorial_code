def demo_tuple():
    p12 = "Joe", "Gomez", 12
    print(p12)
    print(p12[0])

def demo_dict():
    p12 = {"fname":"Joe", "lname":"Gomez", "number": 12}
    print(p12)
    print(p12["fname"])

class Player:
    pass

class Player2:
    def __init__ (self):
        self.fname = ""
        self.lname = ""
        self.number = 0

# ควรเขียนแบบนี้
class Player3:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

def demo_simple_player_class():
    p12 = Player()                          #! Instance for class
    p12.fname = "Joe"                       #! Attribute / Property
    p12.lname = "Gomez"
    p12.number = 12
    print(p12.lname) 

def demo_simple_player2_class():
    p12 = Player2()                         #! Instance for class
    p12.fname = "Joe"                       #! Attribute / Property
    p12.lname = "Gomez"
    p12.number = 12
    print(p12.lname) 

def demo_simple_player3_class():
    p12 = Player3("Joe","Gomez",12)         #! Instance for class
    print(p12.lname) 

if __name__ == "__main__":
    # demo_tuple()  
    # demo_dict()
    # demo_simple_player_class()
    # demo_simple_player2_class()
    demo_simple_player3_class()
