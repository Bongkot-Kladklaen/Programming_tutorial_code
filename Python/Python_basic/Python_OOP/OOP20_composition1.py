from datetime import date

class Person:
    def __init__(self, title, fname, lname, dob):
        self.title = title
        self.fname = fname
        self.lname = lname
        self.dob = dob
    def __str__(self):
        return "{} {} {} {}".format(self.title, self.fname, self.lname, self.dob)

class PersonV2:
    def __init__(self, title, fname, lname, titleTh, fnameTh, lnameTh,dob):
        self.title = title
        self.fname = fname
        self.lname = lname
        self.titleTh = titleTh
        self.fnameTh = fnameTh
        self.lnameTh = lnameTh
        self.dob = dob
    def __str__(self):
        return "{} {} {} {} {} {} {}" \
            .format(self.title, self.fname, self.lname,
                    self.titleTh, self.fnameTh, self.lnameTh,
                    self.dob)

class PersonName:
    def __init__(self, title, fname, lname):
        self.title = title
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "{} {} {}".format(self.title, self.fname, self.lname)

# Composition class
class PersonV3:
    def __init__(self, nameEn, nameTh, dob):
        self.nameEn = nameEn
        self.nameTh = nameTh
        self.dob = dob
    def __str__(self):
        return "{}\n{}\n{}".format(self.nameEn, self.nameTh, self.dob)

if __name__ == '__main__':
    p1 = Person("Mr.", "Peter", "Parker", date(1995, 10, 4))
    print(p1)
    p2 = PersonV2("Mr.", "Peter", "Rarker",
                  "นาย","ปีเตอร์", "ปาร๊คเกอร์", date(1995, 10, 4))
    print(p2)
    print("*" * 20)

    # Class parameter
    p3 = PersonV3(PersonName("Mr.", "Peter", "Rarker"),PersonName("นาย","ปีเตอร์", "ปาร๊คเกอร์"),date(1995, 10, 4))
    print(p3)