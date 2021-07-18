def exp(a,n): 
    if n == 0: 
        return 1
    else:
        return a * exp(a,n-1)
print(exp(2,4))