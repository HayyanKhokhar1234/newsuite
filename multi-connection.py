import selectors
import socket
import types
import sys

sel= selectors.DefaultSelector()

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key,mask):
    sock=key.fileobj
    data=key.data
    if mask & selectors.EVENT_READ:
        recv_data= sock.recv(1024) #Should be ready to read
        if recv_data:
            data.outb +=recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing ', repr(data.outb), 'to', data.addr)
            sent=sock.send(data.outb) #should be ready to write
            data.outb= data.outb[sent:]






HOST='127.0.0.1' #Standard loopback interface address (local host)
PORT= 17000    #port to listen on (non  privileged ports are >1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST,PORT))
#     s.listen()
#     conn,addr =s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data=conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)

host, port = sys.argv[1], int(sys.argv[2])
lsock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print('Listening on ', (host,port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)




try:
    while True:
        events=sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                print('Hi'
                )
                accept_wrapper(key.fileobj)
            else:
                service_connection(key,mask)
except KeyboardInterrupt:
    print('Caught keyboard interrupt, exiting')
finally:
    sel.close()


