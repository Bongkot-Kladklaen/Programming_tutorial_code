str1 = "hello welcome to amuls academy"
print(str1)
print(str1.capitalize())

str2 = "Welcome to amuls academy"
print(str2.capitalize())

str1 = """johny johny yes papa
eating sugar no papa
telling lie no papa
open your mouth haha
"""
print(str1)

print(str1.count('no'))
print(str1.count('papa'))

str1 = "google.com"
print(str1.endswith('com'))
print(str1.endswith('m'))
print(str1.endswith('org'))
print(str1.find('m'))
print(str1.split('.'))
print(str1.title())
print(str1.upper())
print(str1.lower())
print(str1.islower())
print(str1.isupper())

str3 = "hello Welocme to AMULS academy"
print(str3.swapcase())

str4 = "hello"
print(str4.replace('hello','new'))

digit = '123g'
digit1 = '123'
print(digit.isdigit())
print(digit1.isdigit())
print(digit1.isalpha())
print(digit.isalpha())

print(str4.isalpha())

str5 = '!!!!!hello!!!!!'
print(str5.strip('!'))
str6 = '!!!!!hello!!!!!'
print(str6.lstrip('!'))
str7 = '!!!!!hello!!!!!'
print(str7.rstrip('!'))

string = 'abcde'
dict1 = {'a':'1','b':'2'}
t = string.maketrans(dict1)
print(t)
print(ord('a'))

string1 = "hello guys and welcome"
dict2 = {'a':'1','b':'2','c':'3','d':'4'}
table = string1.maketrans(dict2)
print(table)
print(chr(97))

string = "hello guys and welcome"
str1 = 'abcde'
str2 = '12345'
t = string.maketrans(str1,str2)
print(t)
print(chr(49))

string = "((hello guys and welcome))"
str1 = 'abcde'
str2 = '12345'
str3 = '($&'
tt = string.maketrans(str1,str2,str3)
print(t)
print(chr(36))

print(string.translate(table))
print(string.translate(t))
print(string.translate(tt))
