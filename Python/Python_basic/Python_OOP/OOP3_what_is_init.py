class Person:
    # __init__ is Constructor for class
    def __init__(self,fname, lname, country):      
        self.fname = fname
        self.lname = lname
        self.country = country
    
    # __str__ is toString same in java
    def __str__(self):
        return "fname: {} lname: {} country: {}".format(self.fname,self.lname,self.country)

class Person2:
    # __init__ is Constructor for class
    def __init__(self,fname = None, lname = None, country = None):      
        self.fname = fname
        self.lname = lname
        self.country = country
    
    # __str__ is toString same in java
    def __str__(self):
        return "fname: {} lname: {} country: {}".format(self.fname,self.lname,self.country)



if __name__ == "__main__":
    p1 = Person2("Thailand")
    print(p1.fname)

    p2 = Person2("Jay","Cop","Th")
    print(p2)
   