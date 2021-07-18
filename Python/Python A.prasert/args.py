# print(3,5,10)
# print(3,10)
# print(2, 'two',1)
def avg(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args) 

def print_bullet(*items, bullet="\u2022"):
    for e in items:
        print("{} {}".format(bullet, e))

# print(avg(2,3,5,6))
print_bullet('lily','rose','jasmine')