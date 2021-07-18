
#* Creating a Function & Calling a Function
#Creating a Function
def my_function():
  print("Hello from a function")

#Calling a Function
my_function()

#* Parameters and Arguments
def my_function(fname):         #fname is parameter
  print(fname + " Refsnes")

my_function("Emil")             # "Emil" Argument
my_function("Tobias")           # "Tobias" Argument
my_function("Linus")            # "Linus" Argument

#* Multiple of Parameter and Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#* Arbitrary Arguments, *args
#( * -> one parameter multiple arguments)
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#* Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#* Arbitrary Keyword Arguments, **kwargs
#( ** -> one parameter multiple arguments keyworld name key = value)
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#* Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#* Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#* Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#* The pass Statement
def myfunction():
  pass

#* Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)