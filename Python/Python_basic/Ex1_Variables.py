"""
Variable names are case-sensitive
Variable names Rules
    **การตั้งชื่อตัวแปรที่ถูกต้อง
        myvar = 'John'
        my_var = 'John'
        _my_var = 'John'
        myVar = 'John'
        MYVAR = 'John'
        myvar2 = 'John'
    **การตั้งชื่อตัวแปรที่ไม่ถูกต้อง
        2myvar = "John"
        my-var = "John"
        my var = "John"
Use (+) to combine both text and a variables
String not combine a Number 
"""
#* Creating Variables
# x = 5 # x is of type int->integer
# y = "John" # y is of type str->string
#
# #* Assing Value to Multiple Variable
# a, b = 5, "John"
# c = d = e = "Orange"  #Variable all "Orange" value

#* Output Variables
# print(c)
# print("Python is " + d)
# z = b + c
# print(z)

#* Global Variables
# x = "awesome" #สามารถเรียกใช้ได้ทุกที่
# def myfunc():
#     x = "Test" #เปลี่ยนค่า x ภายในจะไม่ส่งผลกับ x ตัวนอก
#     print("Python is " + x)
# myfunc()
# print(x)
# print("-"*10)

#* The global Keyword
# print(x)
# def globalKeyword():
#     global x #เป็นการทำให้ตัวแปรภายในเป็นตัวแปร global จะมีผมกระทบต่อตัวแปร global ภายนอกเมื่อมีการกำหนดค่าใหม่
#     x = "fantastic"
# globalKeyword()
# print(x)

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
