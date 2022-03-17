from tkinter import *
from functools import partial

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_Screen.geometry('300x250')
    main_screen.title('Account Login')



#Create form label
Label(text='Choose Log in or Register', bg='blue', width='300', height='2', font= ('Calibri',13)).pack()
Label(text='').pack()

#Create Log in button
Button(text='Login', height='2',width='30').pack()
Label(text='').pack()

#Create a register button
Button(text='Register', height='2', width='30').pack()
Label(text='').pack()

main_screen.mainloop()







def register():

    register_screen= Toplevel(main_screen)
    register_screen.title('Register')
    register_screen.geometry('300x250')

    #set text variables
    username=StringVar()
    password=StringVar()

    Label(register_screen, text='Please enter details below', bg='blue').pack()
    Label(register_screen, text='').pack()

    username_lable= Label(register_screen, text='Username * ')
    username_lable.pack()

    username_entry = Entry(register_screen, textvariable = username)
    username_entry.pack()

    password_lable = Label(register_screen, text= 'Password * ')
    password_lable.pack()

    password_entry = Entry(register_screen, textvariable=password, show='*')
    passord_entry.pack()

    Label(register_screen, text= '').pack()

    Button(register_screen, text= 'Register', width=10, height=1, bg='blue').pack()