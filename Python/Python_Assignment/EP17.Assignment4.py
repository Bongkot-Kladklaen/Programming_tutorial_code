
#?แลกเงินและหาจำนวนแบงค์
# 2000 => 1000 => 2 ใบ
# 1500 => 1000 => 1 ใบ, 500 => 1 ใบ
# 1800 => 1000 1 ใบ, 500 => 1 ใบ, 100 =>  3ใบ
# 100 => 50 2 ใบ

number = int(input("Enter money: "))
if number >= 1000:
    print(f"1000 บาท = {number // 1000} ใบ")
    number %= 1000
if number >= 500:
    print(f"500 บาท = {number // 500} ใบ")
    number %= 500
if number >= 100:
    print(f"100 บาท = {number // 100} ใบ")
    number %= 100
if number >= 50:
    print(f"50 บาท = {number // 50} ใบ")
    number %= 50
if number >= 20:
    print(f"20 บาท = {number // 20} ใบ")
    number %= 20
