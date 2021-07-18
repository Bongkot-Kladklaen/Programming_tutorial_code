import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.33'
port = 5000
try:
    s.bind((host, port))
    print ("Socket binded to %s" %port)
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
s.listen(5)
while True:
    conn, address = s.accept()
    print ('Got connection from', address)
    data = conn.recv(1024)
    print ('Data : ', data.decode(encoding='UTF-8',errors='strict'))
    if not data:
        break
    msg = 'Thank you for reporting'
    conn.send(msg.encode(encoding='UTF-8',errors='strict'))
conn.close()
