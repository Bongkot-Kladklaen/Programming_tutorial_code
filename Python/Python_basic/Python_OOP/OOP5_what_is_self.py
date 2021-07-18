class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total(self):                                            #!Instance method
        return self.gold + self.silver + self.bronze

    def dummy(self,a,b):
        return a+b

        
if __name__ == "__main__":
    p1 = Medal("Thai",2,3,4)
    print(p1.total())
    print(p1.dummy(1,2))