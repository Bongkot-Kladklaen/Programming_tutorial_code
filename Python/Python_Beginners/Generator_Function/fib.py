def fib(mymax):
    a,b=0,1
    while True:
        c = a+b
        if c < mymax:
            print('before yield key')
            yield c
            print('after yield key')
            a=b
            b=c
        else:
            break

generator = fib(10)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
