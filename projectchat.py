from socket import AF_INET , socket, SOCK_STREAM
from threading import Thread


def host():
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

    clients = {}
    addresses= {}

    HOST='127.0.0.1'
    PORT = 33000
    BUFFERSIZE=1024
    ADDR= (HOST,PORT)

    SERVER= socket(AF_INET, SOCK_STREAM)
    SERVER.bind(ADDR)





if __name__=='__main__':
        SERVER.listen(4)
        print('waiting for connection...')
        ACCEPT_THREAD= Thread(targest= accept_incoming_connections())
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        SERVER.close()

