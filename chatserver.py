import socket
import threading

port = 5000

SERVER= socket.gethostbyname(socket.gethostname())

ADDRESS=(SERVER,PORT)

FORMAT= "utf-8"

clients,names= [],[]

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDRESS)

def startChat():
    print("server is working on "+ SERVER)

    server.listen()

    while True:

        conn,addr=server.accept()
        conn.send("NAME".encode(FORMAT))

        name=conn.recv(1024).decode(FORMAT)

        names.append(name)
        clients.append(conn)

        broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))

        conn.send('Connection successful!'.encode(FORMAT))

        thread=threading.Thread(target = handle, args = (conn,addr))
        thread.start()

        

