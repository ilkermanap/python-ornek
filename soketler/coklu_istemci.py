import selectors
import socket
import types

if __name__ == "__main__":

    import selectors
    sel = selectors.DefaultSelector()
    # ...
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sel.register(lsock, selectors.EVENT_READ, data=None)

        


    def start_connections(host, port, num_conns):
        messages = [b'Message 1 from client.', b'Message 2 from client.']

        server_addr = (host, port)
        for i in range(0, num_conns):
            connid = i + 1
            print('starting connection', connid, 'to', server_addr)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setblocking(False)
            sock.connect_ex(server_addr)
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
            data = types.SimpleNamespace(connid=connid,
                                        msg_total=sum(len(m) for m in messages),
                                        recv_total=0,
                                        messages=list(messages),
                                        outb=b'')
            sel.register(sock, events, data=data)

    start_connections("127.0.0.1",10500, 2)