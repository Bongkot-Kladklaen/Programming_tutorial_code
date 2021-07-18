""" 
    immutable ไม่เปลี่ยนแปลงค่า 
        - nummeric
        - string
    mutable เปลียนแปลงค่า
        - object
"""
def immutable_demo():

    n = 5
    print("id(n) = {}, n = {}".format(id(n), n))
    n = n + 4
    print("id(n) = {}, n = {}".format(id(n), n))

    s = "rain"
    print("id(s) = {}, n = {}".format(id(s), s))
    s = s + "bow"
    print("id(s) = {}, n = {}".format(id(s), s))
    
def mutable_demo():
    p = ["Peter"]
    print("id(p) = {}, n = {}".format(id(p), p))
    p[0] = "spiderman"
    print("id(p) = {}, n = {}".format(id(p), p))

class Contact:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        
    def __str__(self):
        return "id(self = {}, name = {}, phone = {}".format(id(self), self.name,self.phone)

if __name__ == "__main__":
    # immutable_demo()
    # mutable_demo()
    a = Contact("Fah", "11111111")
    print(a)
    a.phone = "2222222"
    print(a)
    b = a
    print(b)
    b.phone = "33333"
    print(a)
    print(b)