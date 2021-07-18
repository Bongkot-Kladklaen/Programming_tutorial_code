try:
    num = int(input('Enter the number of product in stock : '))
    if num < 0  :
        raise ValueError(' or is not a positive number!')
    print('product in stock = ',num)
except ValueError as e :
    print ('Value is not int type :', e)
finally:
    print ('Thank you for your data')
          
