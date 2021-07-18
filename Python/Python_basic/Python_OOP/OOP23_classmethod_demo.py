"""
    class method สามารถเรียกใช้ได้โดยไม่ต้องสร้าง instance เรียกผ่านชื่อ class ได้เลย
"""

class Eyeglasses:
    def __init__(self, eye, bridge, temple):
       self.eye = eye
       self.bridge = bridge
       self.temple = temple

    @classmethod
    def of(cls, frame_string, sep="-"):
        s = frame_string.split(sep)
        return cls(int(s[0]), int(s[1]), int(s[2]))

    @staticmethod
    def gram_oz(g):
        return g * 0.03527

    def __str__(self):
        return "{}-{}-{}".format(self.eye, self.bridge, self.temple)


if __name__ == "__main__":
    f1 = Eyeglasses(55,16,140)
    f2 = Eyeglasses.of("55,16,140",sep=',')

    print(f1)
    print(f2)
    print(Eyeglasses.gram_oz(20))
    
