
#* Open a File on the Server
f = open("demo.txt","r")
print(f.read())

#* Read Only Parts of the File
f = open("demofile.txt", "r")
print(f.read(5))

#* Read Lines
f = open("demofile.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
  print(x)

#* Close Files
f.close()