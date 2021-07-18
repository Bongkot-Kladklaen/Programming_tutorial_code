print('Please enter an integer value1: ', end=' ')
val1 = int(input())
print('Please enter an integer value2: ', end=' ')
val2 = int(input())
try :
    ans = val1/val2
except ZeroDivisionError as e:
    print('Not allowed : ',e)
else:
    print('Result = ',ans)
