temp = input("ป้อนอุณหภูมิ (องศา) : ")
degree = int(temp[:-1])
unit = temp[-1:].upper()

if unit == "C" :
    result = (degree * 9 / 5) + 32
if unit == "F" :
    result = (degree - 32) * 5 / 9

print(result)