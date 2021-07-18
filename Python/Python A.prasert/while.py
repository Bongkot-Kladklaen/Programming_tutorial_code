def demo():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print("bye")

def demo_for():
    for i in range(1,11):
        print(i)
    print("bye")

def sum_input(): # while
    n = int(input("Enter Number"))
    total = 0
    while n != 0 :
        total += n
        n = int(input("Enter Number"))
    print("Total = ", total)

def sum_input_repeat_unit(): # do...while
    total = 0
    while True:
        n = int(input("Enter Number"))
        if n != 0:
            total += n
        else:
            break
    print("Total = ", total)

# demo()
# sum_input()
sum_input_repeat_unit()
