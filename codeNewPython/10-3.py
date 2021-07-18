try :
    f = open('sample1.txt', 'r')
except IOError as e :
        print('Input/output operation fails ',e)
else :
      print(f.read())
      f.close()
      print ('Reading content in the file successfully')
