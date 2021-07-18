try :
    Val1 = int(input('Type the first number: '))
    Val2 = int(input('Type the second number: '))
    ans = Val1 * Val2
except ValueError:
    print('You must type a whole number!')
else :
      print(Val1, ' * ', Val2, ' = ',ans)
