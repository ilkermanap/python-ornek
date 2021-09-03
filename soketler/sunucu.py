import socket

HOST = '127.0.0.1' 
PORT = 12345       

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
    mysocket.bind((HOST, PORT))
    mysocket.listen()
    conn, addr = mysocket.accept()
    with conn:
        print(addr, ' den baglanti')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
