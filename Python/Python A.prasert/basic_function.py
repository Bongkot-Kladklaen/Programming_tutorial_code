def rectangle(w, h):
    area = w * h
    return area

def triangle(w, h):
    area = .5 * w * h
    return area

def choice():
    print("1.Rectangle area.")
    print("2.Triangle area.")

choice()
c = input("please select option: ")
w = int(input("width = "))
h = int(input("height = "))
if c == "1":
    print(rectangle(w,h))
else:
    print(triangle(w,h))