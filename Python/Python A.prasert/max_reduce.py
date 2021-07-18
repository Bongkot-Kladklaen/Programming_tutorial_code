from functools import reduce
def max_loop(numbers):
    x = numbers[0]
    for n in numbers:
        if n > x:
            x=n
    return x

def max_reduce(numbers):
    x = reduce(lambda cv, v: (v if v > cv else cv), numbers)
    print(x)

def min_reduce(numbers):
    x = reduce(lambda cv, v: (v if v < cv else cv), numbers)
    print(x)

if __name__ == "__main__":
    numbers = [3,6,14,2]
    # print(max_loop(numbers))
    max_reduce(numbers)
    min_reduce(numbers)