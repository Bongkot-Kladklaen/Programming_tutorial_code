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
conn, address = s.accept()
print ('Got connection from', address)
while True:
    data = conn.recv(1024)
    result = data.decode(encoding='UTF-8',errors='strict')
    print('Received ',result,'from client')
    print(' Process data')

    if (result=='Hello server'):
        msg = 'Hello client'
        conn.send(msg.encode(encoding='UTF-8',errors='strict'))
        print(' Process data reply sent')

    elif (result=='disconnect') :
       msg = 'goodbye'
       conn.send(msg.encode(encoding='UTF-8',errors='strict'))
       conn.close()
       break;

    else:
       msg = 'Invalid request'
       conn.send(msg.encode(encoding='UTF-8',errors='strict'))
       print(' Process data reply sent')
