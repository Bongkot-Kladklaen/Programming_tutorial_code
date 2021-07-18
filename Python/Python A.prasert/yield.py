def station():
    yield "A"
    yield "B"
    yield "C"
    yield "D"
def sum_all_digit(n):
    return sum([int(c) for c in str(n)])
def lucky(target = 9, start_num=1,stop_num=100):
    d = []
    for i in range(start_num, stop_num + 1):
        if sum_all_digit(i) == target:
            d.append(i)
    return d
def luck_gen(target = 9, start_num = 1):
    i = start_num
    while True:
        if sum_all_digit(i) == target:
            yield i 
        i += 1

print(lucky(8,1,100))
g = luck_gen(8,1)
print(g)
print(next(g))
print(next(g))

# s = station()
# print(s)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))