class Medal:
    def __init__(self,country,gold,silver,bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
    
    def total(self):                #! Instance method
        return self.gold + self.silver + self.bronze
    
    # def __str__(self):              #! toString()
    #     return "{:15} g: {:3} s: {:3} b: {:3} t: {:3}".format(self.country,self.gold,self.silver,self.bronze,self.total())

    def __repr__(self):             #! String representation
        return "{}{}".format(self.__class__.__name__,repr((self.country,self.gold,self.silver,self.bronze)))

if __name__ == "__main__":
    # th = Medal("thailand",5,6,10)
    # print(th)
    m = [
        Medal("Thailand",5,6,10),
        Medal("Japan",4,4,50),
        Medal("China",2,8,20)
    ]
    for c in m:
        print(c)
