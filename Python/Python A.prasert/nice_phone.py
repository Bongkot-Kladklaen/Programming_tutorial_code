def sum_phone(phone_number):
    total = 0
    for c in phone_number:
        total += int(c)
    return total
def interpret(number):
    meaning = ""
    if number in (9,14,15,19,23,24,32,36,40,41,42,44,45,46,50,51,54,55,56,59,63,64,65):
        meaning = "ดีมาก"
    elif number in (69,79):
        meaning = "ประสบความสำเร็จ"
    elif number in (10,13,16,18,20,22,25,26,28,31,35,38,39,47,49,52,53,57,58,60,61):
        meaning = "ดีปานกลาง"
    elif number in (62,66,68,74,75):
        meaning = "เหนื่อย"
    elif number in (11,12,17,21,27,29,30,33,34,37,43,48,67,70,71,72,73,76,77,78,80):
        meaning = "เหนื่อยมาก"  
    return meaning
n = sum_phone("0634172459")
print(interpret(n))

