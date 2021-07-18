phone = input('Enter your Phone number : ')
for tel in phone:
    if tel == '-' :
        continue
    print(tel,end='')
print('\nEnd of loop')
