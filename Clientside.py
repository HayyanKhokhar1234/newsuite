from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk


def chatserver():
    def receive():
        # Handles the recieving of messages
        while True:
            try:
                message = client_socket.recv(BUFFERSIZE).decode('utf8')
                message_list.insert(tk.END, message)  # Inserts the message in a list at the end.
            except OSError:  # check to se if client has left the chat
                break

    def send(event=None):
        # Handles sending of messages
        message = my_message.get()  # gets the message that is sent from the client socket
        my_message.set('')  # sets the tkinter string variable to blank
        client_socket.send(bytes(message, 'utf8'))  # sends the message
        if message == '{quit}':  # if the message is equal to quit closes appliaction.
            client_socket.close()
            chatserver.quit()

    def on_closing(event=None):
        my_message.set('{quit}')  # As it is closing message is set to quit.
        send()

    chatserver= tk.Tk()
    chatserver.title('ChatServer')
    chatserver.geometry('800x800')


    messages_frame=tk.Frame(chatserver, height=10,width=4, bg='Green')
    my_message=tk.StringVar() #For messages to be sent
    my_message.set('Type messages here')

    scrollbar=tk.Scrollbar(messages_frame) #Navigate through past messages

    #this then contains the message
    message_list= tk.Listbox(messages_frame, height=30, width=50, yscrollcommand=scrollbar.set, )
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    message_list.pack(side=tk.LEFT, fill=tk.BOTH)
    message_list.pack()
    messages_frame.pack()



    entry_field= tk.Entry(chatserver, textvariable=my_message)
    entry_field.bind('<Return>',send)
    entry_field.pack()
    send_button=tk.Button(chatserver,text='send',command=send).pack()

    chatserver.protocol('WM_DELETE_WINDOW', on_closing)

    # Sockets
    HOST='127.0.0.1'
    PORT= 33000
    if not PORT:
        PORT= 33000
    else:
        PORT=int(PORT)

    BUFFERSIZE=1024
    ADDR=(HOST,PORT)

    client_socket=socket(AF_INET,SOCK_STREAM)
    client_socket.connect(ADDR)

    receive_thread= Thread(target=receive)
    receive_thread.start()
    tk.mainloop()

