
#* Delete a File
import os
# os.remove("myfile.txt")

#* Check if File exist:
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")

#* Delete Folder
import os
# os.rmdir("myfolder")