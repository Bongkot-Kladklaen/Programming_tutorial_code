def funcMain():
    x = 30
    
    def funcSub():
        nonlocal x
        x = 48

    print('Value of x before calling funcSub: ',x)
    print('calling funcSub now:')
    funcSub()
    print('Value of x after call funcSub: ',x)

x = 16
funcMain()
print('Value of x in main program : ',x)
