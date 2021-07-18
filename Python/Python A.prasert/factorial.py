import math
def fac(n):
    if n >= 0:
        if n == 0 or n ==1:
            return 1
        else:
            f = 1
            for i in range(2,n+1):
                f = f * i
            return f
    else:
        return math.nan
def permut(n,k):
    return fac(n) // fac(n-k)
def combin(n,k):
    # return fac(n) // (fac(k) * fac(n-k))
    return permut(n,k) // fac(k)

if __name__ == "__main__":
    # print(fac(0))
    print(permut(10,3))
    print(combin(10,3))
    