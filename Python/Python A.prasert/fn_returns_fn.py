def fx(op):
    if op == '+':
        return lambda a, b: a+b
    else:
        return lambda a,b: a-b

def fx2(op):
    def add(a,b): return a + b
    def subtract(a,b): return a - b
    if op=='+':
        return add
    else:
        return subtract

def fx3(op):
    d = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b
    }
    return d[op]

if __name__ == "__main__":
    # func = fx2('+')
    # print(func(5,3))

    func = fx3('-')
    print(func(5,3))
