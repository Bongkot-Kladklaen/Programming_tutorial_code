
#! dunder -> double underscore

class Alpha:
    mormal = 1
    _lucky = 13
    __secret = 777      #! Name mangled -> change _classname__attribute

    def fx(self):
        print("this is fx in A")
    def _fy(self):
        print("this is fy in A")
    def __fz(self):                 #! Final method
        print("this is fz in A")

class Beta(Alpha):
    def __fz(self):
        print("this is fz in B")

if __name__ == "__main__":
    # print(Alpha.mormal)
    # print(Alpha._lucky)
    # # print(Alpha.__secret)
    # print(Alpha._Alpha__secret)
    # print(Alpha.__dict__)
    # Alpha.normal = 99
    # Alpha._lucky = 123
    # Alpha.__secret = 9999
    # print(Alpha.normal)
    # print(Alpha._lucky)
    # print(Alpha.__secret)
    # print(Alpha._Alpha__secret)
    print(Alpha.__dict__)
    a = Alpha()
    a.fx()
    a._fy()
    a._Alpha__fz()

    b = Beta()
    b._Beta__fz()
    b._Alpha__fz()
