import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as myclientsocket:
    myclientsocket.connect((HOST, PORT))
    myclientsocket.sendall(b'Hello, world')
    data = myclientsocket.recv(1024)

print('Received', repr(data))