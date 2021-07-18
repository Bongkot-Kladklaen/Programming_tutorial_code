import ftplib
import os

ftp = ftplib.FTP()
host = "ftp.server.com"
port = 2121

try:
    ftp.connect(host, port)
    ftp.login('usernamer','xxxxxxxx')
    ftp.cwd('/domains/user/public_html/')
    print ("Connect FTP successfully")
except :
    print ("failed to connect")

def downloadFile():
    filename = 'htaccess.txt'
    file = open(filename, 'wb')
    ftp.retrbinary("RETR " + filename, file.write ,1024)
    file.close()
    ftp.quit()

def uploadFile():
    file = open('foo.txt','rb')
    ftp.storbinary('STOR foo.txt', file)
    file.close()
    ftp.quit()
