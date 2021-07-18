class shop :
    'This is my shop class'
    shopName = ''
	
class productB :
    'Products of my company'
    prodID =0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        productB.prodID += 1


    def dispProduct(self):
        print ('Name : ', self.name,  ', Price : ', self.price)

    def salesAmount(self, amount):
        return (self.price * amount)

myShop = shop()
myShop.shopName = 'NanaBook Store'
print('My shop is : ', myShop.shopName)
book1 = productB('Photoshop', 299)
print('ProductID ',book1.prodID)
print('Salesamount : ',book1.salesAmount(255))
book1.dispProduct()
book2 = productB('Microsoft Word', 179)
print('ProductID ',book2.prodID)
book2.dispProduct()
print('Salesamount : ',book2.salesAmount(479))
#print('Salesamount : {:,}'. format(book2.salesAmount(479)))

