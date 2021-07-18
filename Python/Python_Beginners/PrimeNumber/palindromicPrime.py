num = int(input("Enter the number: "))
reverse = int(str(num)[::-1])
print('reversed string: ',reverse)
if num == reverse:
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                print(num,"is not prime number! but it is palindrome")
                break
        else:
            print(num,"is palindromic prime number")
else:
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                print(num,"is not prime number! as well as it is palindrome")
                break
        else:
            print(num,"is prime number but not palindrome!")

    