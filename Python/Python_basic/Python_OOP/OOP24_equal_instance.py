"""
    __eq__ เอาไว้ใช้สำหรับเปรียบเทียบ instance ว่ามีค่าเท่ากันหรือไม่
"""

class Student:
    def __init__(self, fname, score):
        self.fname = fname
        self.score = score

    def __str__(self):
        return "{}, score = {}".format(self.fname, self.score)

    def __eq__(self, other):
        return self.score == other.score

if __name__ == '__main__':
    s1 = Student("Peter", 20)
    s2 = Student("Taylor",20)
    s3 = Student("Taylor",20)
    s4 = Student("And", 38)
    print(s1)
    print(s2)
    print("*" * 10)
    
    print(s1 == s2)
    print(s2 == s3)
    print((s1 == s4))
    print(s1.__eq__(s4))
    print(s1.__eq__(s2))