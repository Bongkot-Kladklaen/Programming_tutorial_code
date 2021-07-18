# import random
# for _ in range(5):
#     print("Hello")

# for _ in range(5):
#     print(random.randint(1,6))

__all__ = ["circle","Alpha","_Beta"] #! __all__ กำหนด method ที่ต้องการให้ไฟล์อื่นเรียกใช้ได้ method ที่เรากำหนดให้ใช้เท่านั้น
_recipe = "a7b3c15"         #! ใช้ _ หน้าตัวแปรจะเป็น Private variable
vat = 0.7

def _rectangle(w,h):
    return w*h

def circle(r):
    return 22/7 * r

class Alpha:
    @staticmethod
    def foo():
        print("hello")
class _Beta:
    @staticmethod
    def bar():
        print("wow")