import random

myRandom = random.randrange(1,7)
count = 0
while True:
    number = int(input("Enter number Anwser: "))
    if number<=0 or count==2:
        break
    correct = (number == myRandom)

    if correct:
        print("Gift for you 100000$")
        break
    else:
        if myRandom < number:
            print(f"ค่าน้อยกว่า: {number}")
        else:
            print(f"ค่ามากกว่า: {number}")

    count += 1
print(f"Anwser: {myRandom}")