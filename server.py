import socket
import threading

sock = socket.socket()

sock.bind(('', 9090))

sock.listen()

conns = []
addrs = []
x = 0

def send(conn, x):
    while True:
        data = conn.recv(400)
        tmp = conns
        for client in tmp:
            if client is conn:
                continue
            client.send(data)

while True:
    conn, addr = sock.accept()
    if not(addr in addrs):
        addrs.append(addr)
        conns.append(conn)
        t = threading.Thread(target=send, args=(conn, x), daemon=True)
        t.start()