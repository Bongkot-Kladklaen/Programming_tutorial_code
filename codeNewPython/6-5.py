num,sum =1,0
while num < 10:
    sum += num
    if num > 5 :
        break
    print('Value of sum loop ',num,' = ',sum)
    num +=1
print('Here outside loop')
