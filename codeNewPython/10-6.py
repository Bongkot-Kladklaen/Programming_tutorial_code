try:
    num = int(input('Enter the number of product in stock : '))
    if num < 0  :
        raise ValueError(' or is not a positive number!')
except ValueError as e :
    print ('Value is not int type :', e)
else :
    print('product in stock = ',num)         
