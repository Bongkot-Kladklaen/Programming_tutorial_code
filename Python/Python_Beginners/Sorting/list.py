num = [10,2,3.4,56,1,1,11]
num2 = [10,2,3.4,56,1,1,11]

num.sort()
print(num)

num2.sort(reverse=True)
print(num2)

list1 = ['aa','b','eeee','ccccc','ddd']
list1.sort(key=len)
print(list1)

list2 = [[2,9],[1,10],[3,7]]
list2.sort()
print(list2)

def SortBySec(element):
    return element[1]

list2.sort(key=SortBySec)
print(list2)