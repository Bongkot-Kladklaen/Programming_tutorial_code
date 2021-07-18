def price_with_vat(amount):
    vat = amount * 7 / 107
    price = amount - vat
    return price, vat

# print(price_with_vat(107))
# a = price_with_vat(200)
# print(a)
# print('price = ',a[0])
# print('vat = ',a[1])
# p, v = price_with_vat(200)
# print('p = ',p)
# print('v = ',v)

def thai_area(sqwa):
    rai = sqwa //400
    ngan = (sqwa - (rai * 400)) // 100
    wa = sqwa % 100
    return rai, ngan, wa

a = 956
print(thai_area(a))
r,n,w = thai_area(a)
print(r,n,w , sep="-")