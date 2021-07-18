import socket
def mainRun():
    host = "127.0.0.1" #IP
    port = 5000
    server = socket.socket()
    server.bind((host,port)) #Connect host,port
    
    server.listen(1) # New Client host 1
    print('Wait...Client connect:')
    client,addr = server.accept()
    print(f"Connect From : {str(addr)}")
    while True :
        # Input for client
        data = client.recv(1024).decode('utf-8') #tranfer byte -> string
        if not data:
            break
        print(f"Meassage From Client : {data}")

        # Response to client
        data = str(data.upper())
        client.send(data.encode('utf-8'))
    client.close() 

if __name__ == "__main__":
    mainRun()