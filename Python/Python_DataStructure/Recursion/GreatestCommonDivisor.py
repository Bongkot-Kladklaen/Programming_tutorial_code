def gcd(a,b):
    low = min(a, b)
    high = max(a, b)

    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return gcd(low,high%low)

print(gcd(6,39))