from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk

def receive():
    #Handles the recieving of messages
    while True:
        try:
            msg=client_socket.recv(BUFSIZ).decode('utf8')
            msg_list.insert(tk.END, msg)
        except OSError: #check to se if client has left the chat
            break


def send(event=None):
    #Handles sending of messages
    msg=my_msg.get()
    my_msg.set('')
    client_socket.send(bytes(msg,'utf8'))
    if msg== '{quit}':
        client_socket.close()
        chatserver.quit()

def on_closing(event=None):
    my_msg.set('{quit}')
    send()

chatserver= tk.Tk()
chatserver.title('ChatServer')

messages_frame=tk.Frame(chatserver)
my_msg=tk.StringVar() #For messages to be sent
my_msg.set('Type messages here')

scrollbar=tk.Scrollbar(messages_frame) #Navigate through past messages

#this then contains the message
msg_list= tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field= tk.Entry(chatserver, textvariable=my_msg)
entry_field.bind('<Return>',send)
entry_field.pack()
send_button=tk.Button(chatserver,text='send',command=send).pack()

chatserver.protocol('WM_DELETE_WINDOW', on_closing)

# Sockets
HOST=input('Enter host: ')
PORT= input('Enter port: ')
if not PORT:
    PORT= 33000
else:
    PORT=int(PORT)

BUFSIZ=1024
ADDR=(HOST,PORT)

client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread= Thread(target=receive)
receive_thread.start()
tk.mainloop()
