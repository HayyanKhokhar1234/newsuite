import tkinter
import smtplib

#Main Screen

def send():
     try:
         username = temp_username.get()
         password= temp_password.get()
         to=temp_reciever.get()

def reset():
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0, 'end')
    recieverEntry.delete(0, 'end')
    subjectEntry.delete(0, 'end')
    bodyentry.delete(0, 'end')




master=Tk()
master.title('Current Email App')

Label(master, test='Current Email App', font=('Calibri',15)).grid(row=0, sticky=N)
Label(master, text="Use the form below to send an email", font=('Calibri',11)).grid(row=1,sticky=W, padx=5)

Label(master, text='Email', font=('Calibri',11)).grid(row=2,sticky=W, padx=5)
Label(master, text="Password", font=('Calibri',11)).grid(row=3,sticky=W, padx=5)
Label(master, text='To', font=('Calibri',11)).grid(row=4,sticky=W, padx=5)
Label(master, text='Subject', font=('Calibri',11)).grid(row=5,sticky=W, padx=5)
Label(master, text='body', font=('Calibri',11)).grid(row=6,sticky=W, padx=5)
Label(master, text='', font=('Calibri',11)).grid(row=7,sticky=S, padx=5)

#storage
temp_username=StringVar()
temp_password=StringVar()
temp_reciever=StringVar()
temp_subject=StringVar()
temp_subject=StringVar()
temp_body=StringVar()

#Entries
usernameEntry= Entry(master, textvariable= temp_username )
usernameEntry.grid(row=2,column=0,padx=10)
passwordEntry=Entry(master,show='*' ,textvariable= temp_password)
passwordEntry.grid(row=3,column=0)
recieverEntry=Entry(master,textvariable= temp_password)
recieverEntry.grid(row=3,column=0)

subjectEntry=Entry(master,textvariable=temp_subject)
subjectEntry.grid(row=5,column=0)

bodyentry= Entry(master, textvariable=temp_subject)
subjectBody.grid(row=6,column=0)

#Buttons

Button(master, text='Send', command=send).grid(row=7, sticky=W,pady=15, padx=5)
Button(master, text='Reset', command=reset).grid(row=7, sticky=W,pady=45,padx=45)




master.mainloop()


