
# Basic class
class Player:
    # Constructor
    def __init__(self):
        # Arrtribute       
        self.fname = ""         
        self.lname = ""        
        self.number = ""  

class Player2:
    def __init__(self,fname,lname,number):     
        self.fname = fname
        self.lname = lname
        self.number = number

if __name__ == "__main__":
    p1 = Player()       # Make Instant for Object Class
    p1.fname = "Jay"
    p1.lname = "Cop"
    p1.number = 31
    print(p1.fname)

    p2 = Player2("Jay","Cop",31)
    print(f"Firstname: {p2.fname} Lastname: {p2.lname} No: {p2.number}")
