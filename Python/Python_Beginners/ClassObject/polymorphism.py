class dog:
    def sound(self):
        print('bow bow')

class cat:
    def sound(self):
        print('meow')

def makesonud(animaltype):
    animaltype.sound()

catobj = cat()
dogobj = dog()
makesonud(catobj)
makesonud(dogobj)