import socket
def mainRun():
    host = "127.0.0.1"
    port = 5001
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    data = input("Enter text: ")
    while data != 'q' :
        server.sendto(data.encode("utf-8"),server)
        data, addr = server.recv(1024)
        data = data.decode("utf-8")
        print("Message from Server " + data)
        data = input("Enter text: ")

    server.close()

if __name__ == "__main__":
    mainRun()