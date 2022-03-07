import selectors
import socket
import types
import sys

sel=selectors.DefaultSelector()
def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)



messages = [b"Message 1 from client.", b"Message 2 from client."]


def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print(f"Starting connection {connid} to {server_addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=connid,
            msg_total=sum(len(m) for m in messages),
            recv_total=0,
            messages=messages.copy(),
            outb=b"",
        )
        sel.register(sock, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            print(f"Received {recv_data!r} from connection {data.connid}")
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print(f"Closing connection {data.connid}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:
            print(f"Sending {data.outb!r} to connection {data.connid}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

HOST='127.0.0.1' #Standard loopback interface address (local host)
PORT= 17000
start_connections(HOST,PORT,2)

try:
    while True:
        events = sel.select(timeout=1)
        if events:
            for key, mask in events:
                    service_connection(key, mask)
                    print('Lol')
        if not sel.get_map():
            break

except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()



#
# HOST='127.0.0.1' #Standard loopback interface address (local host)
# PORT= 17000   #port to listen on (non  privileged ports are >1023)
#
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


