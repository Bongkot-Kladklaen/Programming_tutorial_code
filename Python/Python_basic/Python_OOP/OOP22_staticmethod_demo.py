"""
    static method สามารถเรียกใช้ได้โดยไม่ต้องสร้าง instance เรียกผ่านชื่อ class ได้เลย
"""
class Student:
    num_student = 0
    def __init__(self, fname, lname, w_kg, h_cm):
        self.fname = fname
        self.lname = lname
        self.w_kg = w_kg
        self.h_cm = h_cm

    def __str__(self):
        return "{} W: {}kg.({:.1f}lbs) H: {}cm.({:.1f})in".format(self.fname, self.w_kg, Student.kg_pound(self.w_kg), self.h_cm, Student.cm_inch(self.h_cm))

    def bmi(self):  # instance method
        return self.w_kg/(self.h_cm/100)**2

    @staticmethod
    def kg_pound(kg):
        return kg * 2.20462

    @staticmethod
    def cm_inch(cm):
        return cm * .393701
    
    @staticmethod
    def foo():
        print(Student.num_student)


if __name__ == '__main__':
    s = Student("Jay", "Cop", 50, 164)
    print(s.bmi())
    print(Student.kg_pound(50))
    print(s)

