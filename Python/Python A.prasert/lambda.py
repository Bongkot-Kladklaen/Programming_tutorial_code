def rectangle(w,h):
    return w * h

rect = lambda w, h: w * h # แบบที่หนึ่ง
triangle = lambda w,h: w*h*.5

def area(func, w, h): #แบบที่สองเรียนใช้ผ่านฟังก์ชั่น โดยส่งไปเป็นอากิวเม้น
    return func(w,h)

# lambda มังใช้กับควบคู่กับ map,filter,reduce
# apply (pandas)
def demo1():
    usd = [10,12,10,8]
    thb = list(map(lambda v: v * 32, usd))
    print(thb)
# print(rectangle(5,10))
# print(rect(5,10))
# print(area(rect, 5, 10))
# print(area(triangle, 5, 10))
demo1()