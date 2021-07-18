number_even = []
number_odd = []
while True:
    x = int(input("Enter number: "))
    if x<0 or x == None:
        break
    if x%2 == 0:
        number_even.append(x)
    else:
        number_odd.append(x)

print(f"Number Even: {number_even}")
print(f"Number Odd: {number_odd}")