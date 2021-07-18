class father:
    def __init__(self):
        print('I have 5 acres of land.')
class mother :
    def __init__(self):
        print('I have 2 houses')
class son(father, mother):
    def __init__(self):
        print('I have 40000 baht of money')
        father.__init__(self)
        mother.__init__(self)

#main program
s = son()
