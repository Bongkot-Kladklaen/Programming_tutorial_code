fileObj = open('writeTest.txt', 'r', encoding = 'utf-8')
str = fileObj.read()
print(str)
fileObj.close()
