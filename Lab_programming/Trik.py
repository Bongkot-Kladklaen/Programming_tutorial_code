inputData = input()
A = 1
B = C = 0
def swap(a, b):
    temp = a
    A = b
    B = temp
    return A, B
for i in inputData:
    if i == "A": A, B= swap(A,B)
    elif i == "B": B, C= swap(B,C)
    else: C, A= swap(C,A)
if A == 1:print("1")
if B == 1:print("2")
if C == 1:print("3")