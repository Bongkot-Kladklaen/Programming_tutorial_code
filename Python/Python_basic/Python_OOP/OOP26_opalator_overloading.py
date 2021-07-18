class FootInch:
    def __init__(self, foot, inch):
        self.foot = foot
        self.inch = inch
        self.inches = self.foot * 12 + self.inch

    def __str__(self):
        return "{}'{}\"".format(self.foot, self.inch)

    # Overload opalator
    # opalator +
    def __add__(self, other):
        x = self.inches + other.inches
        f = x // 12
        i = x % 12
        return FootInch(f,i)

    # opalator -
    def __sub__(self, other):
        x = self.inches - other.inches
        f = x // 12
        i = x % 12
        return FootInch(f, i)
    

if __name__ == '__main__':
    m1 = FootInch(5,7)
    m2 = FootInch(3,9)
    m = m1 + m2
    mm = m1 - m2
    print(m)
    print(mm)