import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime())

tuple1 = (1993,6,8,9,20,3,0,0,0)
print(time.mktime(tuple1))

time.sleep(5)
print('hello people')