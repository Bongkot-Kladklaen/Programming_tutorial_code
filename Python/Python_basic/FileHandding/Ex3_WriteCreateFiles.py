
#* Write to an Existing File
# f = open("demo2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

#open and read the file after the appending:
f = open("demo2.txt", "r")
print(f.read())

# f = open("demo3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

#open and read the file after the appending:
f = open("demo3.txt", "r")
print(f.read())

#* Create a New File
f = open("myfile.txt", "x")
# print(f.read())

f = open("myfile.txt", "w")
# print(f.read())