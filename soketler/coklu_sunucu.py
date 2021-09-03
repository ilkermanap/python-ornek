import selectors
import socket
import types

class Message:
    def __init__(self, host, port, msg):
        self.host = host
        self.port = port
        self.msg = msg

    def __str__(self):
        return f"{self.host}:{self.port}"


class MYSocketServer:
    def __init__(self, host, port):
        self.queue = []
        self.myselector = selectors.DefaultSelector()
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.bind((host, port))
        lsock.listen()
        print('listening on', (host, port))
        lsock.setblocking(False)
        self.myselector.register(lsock, selectors.EVENT_READ, data=None)

        while True:
            events = self.myselector.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    self.accept_wrapper(key.fileobj)
                else:
                    self.service_connection(key, mask)

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        print('accepted connection from', addr)
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.myselector.register(conn, events, data=data)


    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                print('received', repr(recv_data), 'from connection', data.connid)
                data.recv_total += len(recv_data)
            if not recv_data or data.recv_total == data.msg_total:
                print('closing connection', data.connid)
                self.myselector.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            print(data)
            if not data.outb and data.messages:
                data.outb = data.messages.pop(0)
            if data.outb:
                print('sending', repr(data.outb), 'to connection', data.connid)
                sent = sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]


if __name__ == "__main__":
    s = MYSocketServer("127.0.0.1", 10500)