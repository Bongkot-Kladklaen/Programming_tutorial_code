point = int(input())
midterm = int(input())
final = int(input())

gpa = point+midterm+final

if gpa>=80 and gpa<=100 :
    print("A")
elif gpa>=75 :
    print("B+")
elif gpa>=70 :
    print("B")
elif gpa>=65 :
    print("C+")
elif gpa>=60 :
    print("C")
elif gpa>=55 :
    print("D+")
elif gpa>=50 :
    print("D")
else:
    print("F")