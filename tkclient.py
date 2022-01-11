import socket
import threading
import tkinter as tk
from tkinter import *

sock = socket.socket()

sock.connect(('127.0.0.1', 9090))

def get(sock, x):
    global top, textfield
    while True:
        data = sock.recv(400)
        textfield.configure(state=NORMAL)
        textfield.insert(END, data.decode("utf-8")+"\n")
        textfield.configure(state=DISABLED)

        print(data.decode("utf-8"))

def send():
    global sock
    data1 = data.get()
    intro = str(sock.getsockname()[0]) + ":" + str(sock.getsockname()[1]) + " says: "
    sock.send(bytes(intro+data1, encoding="utf-8"))

x = 0

t1 = threading.Thread(target=get, args=(sock, x), daemon=True)

t1.start()
   
root = tk.Tk()
root.title("Ultimate messenger")
root.geometry("600x650")

scroll = tk.Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)
    
textfield = tk.Text(root, height=400, width=650, yscrollcommand=scroll.set)
textfield.pack()
textfield.insert(END, "Waiting...\n")

data = tk.StringVar()
data_entry = tk.Entry(textvariable=data)
data_entry.place(relx=.5, rely=.8, anchor="c")
data_button = tk.Button(text="Send", command=send)
data_button.place(relx=.6, rely=.8, anchor="c")

textfield.insert(END, "Best python chat\n")
textfield.configure(state=DISABLED)

root.mainloop()
