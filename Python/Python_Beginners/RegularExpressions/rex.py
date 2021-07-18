str1 = 'my name is alice'
print(str1.replace('alice','john'))

str2 = 'main street broad road'
print(str2.replace('road','rd'))

print(str2[0:17] + str2[17:].replace('road','rd'))

#! Regular Expression
import re

line = 'pet:cat i love cats'
match = re.match(r"pet:\w\w\w",line)
print(match.group(0))

match = re.search(r"pet:\w\w\w",line)
print(match.group(0))

line = 'i love cats pet:cat'
var = re.match(r"pet:\w\w\w",line)
# print(var.group(0))

var = re.search(r"pet:\w\w\w",line)
print(var.group(0))

line = "pet:cat i love cats pet:cow i love cows"
match = re.findall(r"pet:\w\w\w",line)
print(match)

line = 'i love cats pet:cat i love cows, pet:cow thank you'
s = re.split(r"pet:\w\w\w",line)
print(s)

str1 = 'john@abc.com and alice@pqr.com'
var = re.sub(r"@\w+",'@xyz',str1)
print(var)