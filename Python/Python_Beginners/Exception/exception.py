import math

num = int(input('please enter the number to calculate factorial of: '))
try:
    result = math.factorial(num)
    print(result)
except:
    print('connot compute the factorial of negative numbers')
