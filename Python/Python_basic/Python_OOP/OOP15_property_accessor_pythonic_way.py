class Person:
    def __init__(self,fname,lname,blood):
        self.fname = fname
        self.lname = lname
        self.blood = blood          #! A,B,AB,O
        
    @property                       #! Getter
    def fname(self):
        return self.__fname

    @fname.setter                   #! Setter
    def fname(self,fname):
        self.__fname = fname.strip().title()

    @property
    def blood(self):                #! Getter
        return self.__blood

    @blood.setter
    def blood(self,blood):          #! Setter
        if blood.upper() in ["A","B","AB","O"]:
            self.__blood = blood.upper()
        else:
            raise ValueError("invalid blood group")

    def __str__(self):
        return "{!r} {} blood group: {}".format(self.fname,self.lname,self.blood)

if __name__ == "__main__":
    p1 = Person("Peter","Parker","A")
    print(p1)
    p1.blood = "O"
    print(p1)
    print(p1.blood)
   