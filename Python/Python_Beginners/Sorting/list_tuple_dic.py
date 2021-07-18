list1 = [7,5,6,3,4,2,3,1]
tuple1 = ((3,8),(2,9),(1,10),(4,7))
d1 = {3:"e",2:"a",1:"c",7:"b",5:"d"}

print(sorted(list1))
print(sorted(list1,reverse=True))

print(sorted(tuple1))

print(sorted(d1))
print(sorted(d1.values()))
print(sorted(d1.items()))
print(sorted(d1.items(),key=lambda x: x[1]))

tuple2 = ((1,'a'),(4,'s'),(3,'z'),(2,'r'))
print(sorted(tuple2))

def SecondValue(element):
    return element[1]

print(sorted(tuple2,key=SecondValue))