import math

num = int(input('input: '))
try:
    result = math.factorial(num)
    print(result)
finally:
    print('goodbye!!')