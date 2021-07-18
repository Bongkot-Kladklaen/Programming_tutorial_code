#!C:\Python36\python
import cgi, cgitb, os, sys
cgitb.enable()
def header():
    print("Content-Type: text/html")
    print()
dir = "./upload"
data = cgi.FieldStorage()
if not "file" in data:
    header()
    print("<h1>ไม่ได้รับไฟล์</h1>")
elif not data["file"].filename:
    header()
    print("<h1>ไม่พบชื่อไฟล์</h1>")
else:
    filedata = data["file"].file
    filename = data["file"].filename
    if filename.find("\\") != -1:
        uploadpath = os.path.join(dir+'/', os.path.basename(filename))
    else:
        uploadpath = os.path.join(dir+'/', filename)
    writefile = open(uploadpath, 'wb')
    filedata.seek(0)
    while True:
        fdata = filedata.read(2<<16)
        if not fdata:
            break
        writefile.write(fdata)
    writefile.close()
    header()
    print("<h1>อัพโหลดไฟล์สำเร็จ</h1>")
