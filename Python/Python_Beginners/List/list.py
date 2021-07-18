animal = ['dog','cat','monkey']
print(animal)
print(animal[0])

#? Nested list
list1 = [[10,20],[30,40]]
print(list1[0])
print(list1[0][0])

#? Replace
list2 = [10,20,30,40]
list2[0] = 1
print('Replace : ',list2)

#? Insert
list3 = [10,20,30,40]
list3.insert(2,'hello')
print('Insert : ',list3)

#? Sort
list4 = [30,20,10,40]
list4.sort()
print('Sort : ',list4)

#? Delete
list5 = [10,20,30,40]
del list5[1]
print('Delete : ',list5)

#? Append
list6 = [10,20,30,40]
list6.append(80)
print('Append : ',list6)

#? Reverse
list7 = [10,20,30,40]
list7.reverse()
print('Reverse : ',list7)

animal1 = ['dog','cat','monkey']
animal1.reverse()
print('Reverse string : ',animal1)