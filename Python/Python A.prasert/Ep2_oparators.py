
#* การประยุกต์ใช้ floor division(//) และ mod(%)

def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False
def leap_year_buddhist(year):
    if year % 4 == 3:
        return True
    else:
        return False

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
def is_odd(n):
    return not is_even(n)

def promotion(come, pay, per_head, pax):
    return (pax // come) * (pay * per_head) + (pax % come) * per_head 

print(promotion(4,3,100,8))
