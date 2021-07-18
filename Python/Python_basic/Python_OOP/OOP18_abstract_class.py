"""
    Abstract class สร้างไว้เพื่อให้ class อื่นสืบทอดเท่านั้น ไม่สามารถสร้าง instant ด้วยตัวเอง
    การสร้าง Abstact class ต้อง import libraly
        - from abc import ABC, abstractmethod

"""

from abc import ABC, abstractmethod   # Abstract Base Class

class Member(ABC):
    def __init__(self, m_id, fname, lname):
        self.m_id = m_id
        self.fname = fname
        self.lname = lname
    def __str__(self):
        return "ID: {} {} {}".format(self.m_id, self.fname, self.lname)

    @abstractmethod
    def discount(self):
        pass

    def full_name(self):
        return "{} {}".format(self.fname, self.lname)

class Gold(Member):
    def discount(self):
        return .10

class Silver(Member):
    def discount(self):
        return .05

if __name__ == '__main__':
    # m = Member("007", "James", "Bond")
    # print(m)
    g = Gold("123", "Peter", "Parker")
    print(g)
    print(g.discount())
    print(g.full_name())
    s = Silver("123", "jay", "cop")
    print(s)
    print(s.discount())
    print(s.full_name())
