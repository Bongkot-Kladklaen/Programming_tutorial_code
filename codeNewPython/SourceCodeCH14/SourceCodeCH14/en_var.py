#!C:\Python36\python
import os

print ("Content-type: text/html");
print()
print ("<H1>Environment Variables</H1>");
for key in os.environ.keys():
   print ("<b>%20s</b>: %s<br />" % (key, os.environ[key]))
