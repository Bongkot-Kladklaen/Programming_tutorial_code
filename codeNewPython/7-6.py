def max_value(num1, num2):
    if num1 >  num2 :
        print('max value is ', num1)
    else :
        print('max value is ', num2)

print('Please enter an integer value1: ', end='')
value1 = int(input())
print('Please enter an integer value2: ', end='')
value2 = int(input())
max_value(value1,value2)
