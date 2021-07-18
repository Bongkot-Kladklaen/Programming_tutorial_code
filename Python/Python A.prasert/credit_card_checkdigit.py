def remove_none_digit(s):
    d = []
    for c in s:
        if c.isdigit():
            d.append(int(c))
    return d

def print_digit(v):
    for i in v:
        print("{:>2} |".format(i), end="")
    print()
if __name__ == "__main__":
    card = "4597 7692 1332 987"
    print(card)
    card = remove_none_digit(card)
    print_digit(range(15))
    print_digit(card)
    a = [2,1] * 7 + [2]
    print_digit(a)
    print("-" * 60)
    y = [m * n for m,n in zip(card,a)]
    print_digit(y)
    y2 = [n if n < 10 else n // 10 + n % 10 for n in y]
    print_digit(y2)
    sum_yw = sum(y2)
    print("sum = {}".format(sum_yw))

    r = sum_yw % 10
    chk_digit = 0 if r == 0 else 10 - r
    print("check digit = {}".format(chk_digit))
