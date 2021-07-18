
#?โปรแกรมคำนวฯค่า BMI (ดัชนีมวลกาย)
#? BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)

print("โปรแกรมคำนวน BMI")
weight = int(input("กรอกน้ำหนัก(kg) : "))
height = int(input("ส่วนสูง(cm) : "))

height /= 100
result = weight / (height * height)
print("ค่าดัชนีมวลการ = ",result)

