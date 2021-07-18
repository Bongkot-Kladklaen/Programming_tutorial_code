class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
        
    def total(self):                                            #!Instance method
        return self.gold + self.silver + self.bronze

class Athlete:
    def dummy(self):
        return "hello"