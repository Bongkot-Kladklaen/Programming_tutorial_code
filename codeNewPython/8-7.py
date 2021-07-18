class Compare :
        def __init__(self, x = 0, y = 0) :
            self.x = x
            self.y = y
        def __lt__(self,obj) :
            self.cmp = (self.x ** 2) + (self.y ** 2)
            obj.cmp = (obj.x ** 2) + (obj.y ** 2)
            return self.cmp < obj.cmp
A1 = Compare(4,2)
A2 = Compare(1,5)
print(A1 < A2)
