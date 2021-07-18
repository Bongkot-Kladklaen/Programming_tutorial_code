# number = []
# while True:
#     x = int(input("Enter number: "))
#     if x < 0:
#         break
#     number.append(x)
#     number.sort()
#     number.reverse()
# print(number)
# print(min(number))
# print(max(number))
# print(sum(number))


fish_kg = []
number = []
while True:
  x = int(input())
  if x == 0:
    max_min = input().lower()
    if max_min == "max":
      fish_kg.sort()
      fish_kg.reverse()
      for i in fish_kg:
        a = str(i)
        number.append(a)
    if max_min == "min":
      fish_kg.sort()
      for i in fish_kg:
        a = str(i)
        number.append(a)
    break
  fish_kg.append(x)
result = " ".join(number)
print(result)

# number = ["1","2","3","4"]
# a = []
# for i in number:
#     b = int(i)
#     a.append(b)
# # txt = " ".join(number)
# print(a)
    
