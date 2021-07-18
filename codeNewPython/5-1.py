score = input('Please enter your score : ')
score = int(score)
if score >=80 and score <= 100 :
    print('Score = ',score,' Grad is A')
elif score >=70 and score <= 79 :
    print('Score = ',score,' Grad is B')
elif score >=60 and score <= 69 :
    print('Score = ',score,' Grad is C')
elif score >=50 and score <= 59 :
    print('Score = ',score,' Grad is D')
elif score >=0 and score <= 49 :
    print('Score = ',score,' Grad is F')
else :
    print('Score error')
