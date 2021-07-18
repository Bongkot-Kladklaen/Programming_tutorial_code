import re

class Person:
    def __init__(self, fname, lname, sex):
        self.fname = fname.strip().title()
        self.lname = lname.strip().title()
        self.sex = sex

    def __str__(self):
        return "{!r} {!r} Sex: {}".format(self.fname, self.lname, self.sex)

class Student(Person):
    def __init__(self, s_id, fname, lname, sex):
        super().__init__(fname, lname, sex)
        self.s_id = self.remove_non_digit(s_id)

    def __str__(self):
        return "{} {}".format(self.s_id, super().__str__())

    @staticmethod
    def remove_non_digit(s):
        return re.sub(r"[\D]", "", s)

    def email(self):
        return "{}.{}{}@abc.com".format(self.fname, self.lname, self.s_id[:2])

class ExchangeStudent(Student):
    def __init__(self, s_id, fname, lname, sex, partner_univ):
        super().__init__(s_id, fname, lname, sex)
        self.partner_univ = partner_univ

    def foo(self, s):
        return self.remove_non_digit(s)

if __name__ == '__main__':
    s1 = Student("123-456", "  jay", "Cop", "M")
    print(s1)
    print(s1.email())
    s2 = ExchangeStudent("213-(245)", "Peter", "Parker", "F", "Univer")
    print(s2)
    print(s2.email())