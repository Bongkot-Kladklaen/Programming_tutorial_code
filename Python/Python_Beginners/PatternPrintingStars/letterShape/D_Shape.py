for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col==1 or col==2 or col==3)):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()