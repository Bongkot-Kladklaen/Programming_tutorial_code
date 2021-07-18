
#* For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#* Looping Through a String
for x in "banana":
  print(x)

#* The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#* The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#* The range() Function
#range(start,end,step)
for x in range(6):
  print(x) #print 0,1,2,3,4,5

for x in range(2, 6):
  print(x) #print 2,3,4,5

for x in range(2, 30, 3):
  print(x) #print 2,5,8,11,14,17,20,23,26,29

#* Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#* Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#* The pass Statement
for x in [0, 1, 2]:
  pass