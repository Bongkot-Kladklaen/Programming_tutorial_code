num = int(input("Enter the number of rows: "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*", end=" ")
    print()

# Odd number
#for i in range(0,num):
#    for j in range(0,num-i-1):
#        print(end=" ")
#    for j in range(0,2*i+1):
#        print("*", end=" ")
#    print()


def pyramid(rows):
    for i in range(rows):
        print(''*(rows-i-1)+'*'*(i+1))
        #print(''*(rows-i-1)+'*'*(2*i+1)) # Odd number