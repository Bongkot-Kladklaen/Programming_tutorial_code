list1 = [1,2,3,4]
list2 = ['a','b','c','d']
dict1 = {1:'apple',2:'ball',3:'cat'}
dict2 = {'o':'orange'}

print(list1+list2)
dict1.update(dict2)
print(dict1)
print(dict2)

dict1 = {1:'a',2:'b'}
list1 = [3,'c']
dict1.update([list1])
print(dict1 )
