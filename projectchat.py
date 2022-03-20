from socket import AF_INET , socket, SOCK_STREAM
from threading import Thread



def accept_incoming_connections():
    #sets up handling for incoming clients
    while True:
        client,client_address = SERVER.accept()
        print('%s:%s has connected.' % client_address)
        client.send(bytes('Hello, welcome to the chat type your name adn enter','utf8'))
        addresses[client]= client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
        #Handles a single client connection
        name=client.recv(BUFSIZ).decode('utf8')
        welcome='Welcome %s! If you want to quit, type quit or press back. '%name
        client.send(bytes(welcome,'utf8'))
        msg='%s has joined the chat' % name
        broadcast(bytes(msg,'utf8'))
        clients[client] = name

        while True:
            msg=client.recv(BUFSIZ)
            if msg != bytes('{quit}','utf8'):
                broadcast(msg,name+': ')
            else:
                client.send(bytes("{quit}","utf8"))
                client.close()
                del clients[client]
                broadcast(bytes('%s has left the chat'% name, 'utf8'))
                break



def broadcast(msg, prefix=''): #prefix is for name identifying
    for sock in clients:
        sock.send(bytes(prefix,'utf8')+msg)

clients = {}
addresses= {}

HOST=''
PORT = 33000
BUFSIZ=1024
ADDR= (HOST,PORT)

SERVER= socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)




if __name__=='__main__':
    SERVER.listen(5)
    print('waiting for connection...')
    ACCEPT_THREAD= Thread(targest= accept_incoming_connections())
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
