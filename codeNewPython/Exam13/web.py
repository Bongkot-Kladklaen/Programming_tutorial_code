import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'www.reviva.co.th'
port = 80
request = "GET / HTTP/1.1\nHost:"+server+"\n\n"
s.connect((server, port))
s.send(request.encode())
result = s.recv(4096)
s.close()
print(result.decode('UTF-8'))
