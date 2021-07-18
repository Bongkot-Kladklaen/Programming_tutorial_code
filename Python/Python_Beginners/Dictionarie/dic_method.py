list1 = [1,2,3,4]
print(dict.fromkeys(list1))

print({}.fromkeys(range(1,7),10))

students = {'john':20,'ria':21,'ann':22}
print(students.setdefault('john'))
print(students.setdefault('anable'))
print(students)
print(students.setdefault('roo',10))
print(students)