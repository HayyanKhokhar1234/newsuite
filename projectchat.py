from socket import AF_INET , socket, SOCK_STREAM
from threading import Thread



global SERVER
global accept_incoming_connections

def accept_incoming_connections():
    #sets up handling for incoming clients
    while True:
        client,client_address = SERVER.accept()
        print('%s:%s has connected.' % client_address)
        client.send(bytes('Type your name and enter','utf8'))
        addresses[client]= client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
            #Handles a single client connection
            name=client.recv(BUFFERSIZE).decode('utf8')
            welcome='Welcome %s! If you want to quit, type quit or press back. '%name
            client.send(bytes(welcome,'utf8'))
            message='%s has joined the chat' % name
            broadcast(bytes(message,'utf8'))
            clients[client] = name

            while True:
                message=client.recv(BUFFERSIZE)
                if message != bytes('{quit}','utf8'):
                    broadcast(message,name+': ')
                else:
                    client.send(bytes("{quit}","utf8"))
                    client.close()
                    del clients[client]
                    broadcast(bytes('%s has left the chat'% name, 'utf8'))
                    break



def broadcast(message, prefix=''): #prefix is for name identifying
        for sock in clients:
            sock.send(bytes(prefix,'utf8')+message)

#List to store clients, and addresses to store clients.
clients = {}
addresses= {}

#Host that the server is on
HOST='127.0.0.1'
#The port that the server is using.
PORT = 33000
#Maximum size of bytes that can be sent
BUFFERSIZE=1024
#Address is just a bracket of the host and port
ADDR= (HOST,PORT)

#This is the server socket being created binded to the address
SERVER= socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)





if __name__=='__main__':
        SERVER.listen(4)
        print('waiting for connection...')
        ACCEPT_THREAD= Thread(targest= accept_incoming_connections())
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        SERVER.close()

