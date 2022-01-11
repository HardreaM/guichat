import socket
import threading
from easygui import *

sock = socket.socket()

sock.connect(('127.0.0.1', 9090))

def get(sock, x):
    while True:
        data = sock.recv(400)
        textbox(text=data.decode("utf-8"))
        print(data.decode("utf-8"))

def send(sock, x):
    while True:
        data = enterbox()
        sock.send(bytes(data, encoding="utf-8"))
x = 0

t1 = threading.Thread(target=get, args=(sock, x), daemon=True)
t2 = threading.Thread(target=send, args=(sock, x), daemon=True)

t1.start()
t2.start()

t1.join()
t2.join()