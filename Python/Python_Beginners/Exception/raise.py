try:
    num = int(input('Enter a number: '))
    if num <= 0:
        raise ValueError('That is not postitive number')
except ValueError as error:
    print(error)