import pyuca
provinces = ["พิษณุโลก", "ชัยนาท", "เลย", "เพชรบุรี", "ลำปาง", "ขอนแก่น", "กรุงเทพ","เชียงใหม่", "ตาก", "แพร่"]
s = sorted(provinces) # sort แบบ unicode
print(s)
s_correct = sorted(provinces,key = pyuca.Collator().sort_key) #sort ถูกต้องตามพจนานุกรมไทย
print(s_correct)
print(provinces)
provinces.sort(key = pyuca.Collator().sort_key)#sort ถูกต้องตามพจนานุกรมไทย อัพเดทตัว provinces โดยตรง
print(provinces)