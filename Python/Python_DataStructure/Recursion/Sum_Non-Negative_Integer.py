def sumDigit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigit(int(n/10))

print(sumDigit(678))