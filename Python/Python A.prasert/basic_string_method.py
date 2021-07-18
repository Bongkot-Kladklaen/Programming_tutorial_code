
#* split() , strip() ลบช่องว่าง, isdigit() เซ็คค่าว่าเป็นตัวเลขหรือไม่
s = " test "
t = "test"
ss = s.strip() 

def demo_isdigit(p):
    total = 0
    for c in p:
        if c.isdigit():
            total += int(c)
    return total

print(ss == t)
plate = "1กท 4567"
print(demo_isdigit(plate))
