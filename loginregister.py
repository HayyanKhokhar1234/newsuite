from tkinter import *
import os
from functools import partial

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title('Success')
    user_not_found_screen.geometry('150x100')
    Label(user_not_found_screen, text='User not Found').pack()
    Button(user_not_found_screen, text='OK',command=delete_user_not_found_screen).pack()

def password_not_recognised():
    global password_not_recog_screen

    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title('Success')
    password_not_recog_screen.geometry('150x100')
    Label(password_not_recog_screen, text='Invalid Password ').pack()
    Button(password_not_recog_screen, text='OK', command=delete_password_not_recognised).pack()


def delete_login_success():
    login_success_screen.destroy()


def login_success():

    global login_success_screen

    login_success_screen=Toplevel(login_screen)
    login_success_screen.title('Success')
    login_success_screen.geometry('150x100')

    Label(login_success_screen,text='Login Success').pack()

    Button(login_success_screen, text='OK', command=delete_login_success).pack()



def login_verify():
    #get username and password
    username1=username_verify.get()
    password1=password_verify.get()

    #this will delete the entry after log in button is pressed

    username_login_entry.delete(0,END)
    password_login_entry.delete(0,END)

    #The method listdir() returns a list containing the names of the entries in teh directory given by path.
    list_of_files = os.listdir()

    #defining verification's conditions
    if username1 in list_of_files:
        file1=open(username1,'r') #Open the file in read mode

#read the file,
#as splitlines() actually splits on the newline character,
#the newline character is not left hanging at the end of each line.
        verify=file1.read().splitlines()
        if password1 in verify():
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()





def login_verification():
    print('Working')


def login():
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    global login_screen
    login_screen=Toplevel(main_screen)
    login_screen.title('Login')
    login_screen.geometry('300x250')
    Label(login_screen, text='Please enter details to log in')
    Label(login_screen,text='').pack()


    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text='Username * ').pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text='').pack()
    Label(login_screen,text='').pack()
    Label(login_screen, text='Password * ').pack()
    password_login_entry = Entry(login_screen, textvariable= password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen,text='').pack()
    Button(login_screen, text='Login',width=10, height=1,command=login_verification).pack()

def register():
    global username
    global password
    global username_entry
    global password_entry
    global register_screen
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

    password_entry = Entry(register_screen, textvariable=password,show='*')
    password_entry.pack()

    Label(register_screen, text= '').pack()

    Button(register_screen, text= 'Register', width=10, height=1, bg='blue',command=register_user).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, 'w')

    file.write(username_info + '\n')
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text='Registration Success', fg='green', font=('calibri', 11)).pack()


def main_account_screen():
    global main_screen
    main_screen = Tk()

    main_screen.geometry('250x350')
    main_screen.title('Account Login')
    Label(text='Choose Log in or Register', bg='blue', width='300', height='2', font= ('Calibri',13)).pack()
    Label(text='').pack()

#Create Log in button
    Button(text='Login', height='2',width='30',command=login).pack()
    Label(text='').pack()

#Create a register button
    Button(text='Register', height='2', width='30',command=register).pack()
    Label(text='').pack()




main_account_screen()
main_screen.mainloop()