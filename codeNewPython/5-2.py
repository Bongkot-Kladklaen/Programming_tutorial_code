n = input('Please enter Integer number : ')
n = int(n)
if n > 0 :
    if n%2 ==0:
        print('Positive even number')
    else:
        print('Positive odd number')
elif n == 0 :
    print('Zero number')
else :
    print('Negative number')
