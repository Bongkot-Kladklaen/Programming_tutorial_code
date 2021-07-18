num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    for j in range(i):
        print('*',end=" ")
    print()