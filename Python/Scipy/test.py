string = "tHIS IS bORNTOdEV"
output = ""
for i in string:
  if i == i.upper():
    output += i.lower()
  else:
    output += i.upper()

print(output)