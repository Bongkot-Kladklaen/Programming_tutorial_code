class addObj :
    def __init__(self, x = 0, y = None, z = 0) :
        self.x = x
        self.y = y
        self.z = z
    def __str__(self) :
        return str(self.x) + ' ' + self.y + ' ' + str(self.z)
    def __add__(self,obj):
        x = self.x + obj.x
        y = self.y + obj.y
        z = self.z + obj.z
        return addObj(x,y,z)

A1 = addObj(4,'Python ',6)
A2 = addObj(6,'Programming',6)
print(A1 + A2)
