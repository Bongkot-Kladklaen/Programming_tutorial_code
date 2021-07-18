number = sorted([int(x) for x in input().split()])
s = input()
l = []
for i in s:
    if i == "A": l.append(number[0])
    elif i == "B": l.append(number[1])
    else: l.append(number[2])
for i in range(len(l)): print(l[i], end=" ")
