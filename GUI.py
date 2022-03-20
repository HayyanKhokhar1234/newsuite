import tkinter as tk

def encryption_back():
    encryption_screen.destroy()

def Encryption():
    #This is a function used to see which algorthim is selected from drop down menu
    def option_changed(choice):

        tk.Label(encryption_screen, text=f'You have selected: {variable.get()}').place(x=0, y=230)
    def option_changed2(choice):

        tk.Label(encryption_screen, text=f'You have selected: {variable2.get()}').place(x=600, y=230)
    #making encryption_Screen global for easier use across program
    global encryption_screen
    #making a screen for the encryption/decryption cipher
    encryption_screen=tk.Tk()
    encryption_screen.title('Encryption Cipher')
    encryption_screen.geometry('800x800')
    tk.Label(encryption_screen,text='Encryption/Decryption Suite', font=('Arial', 25), bg='Green').pack()
    tk.Button(encryption_screen,text='Back',font=('Arial',15),command=encryption_back,bg='Red').pack()
    variable=tk.StringVar()
    variable.set('Select an encryption')
    drop=tk.OptionMenu(encryption_screen, variable, 'Vernier Cipher','RSA','Counter Mode','Ceaser Cipher',command=option_changed).place(x=0,y=200)
    print(variable.get())
    tk.Text(encryption_screen,height=20,width=40).place(x=0,y=300)
    tk.Button(encryption_screen,text='Encrypt',bg='Green').place(x=0,y=250)
    p1=tk.Text(encryption_screen, height=2,width=5).place(x=70,y=250)
    p2=tk.Text(encryption_screen, height=2, width=5).place(x=140, y=250)


    variable2=tk.StringVar()
    variable.set('Select An encryption')
    tk.Button(encryption_screen, text='Decrypt', bg='Red').place(x=750, y=250)
    drop2=tk.OptionMenu(encryption_screen, variable2, 'Vernier Cipher','RSA','Counter Mode','Ceaser Cipher',command=option_changed2).place(x=700,y=200)
    p3=tk.Text(encryption_screen,height=2,width=5).place(x=680,y=250)
    p4=tk.Text(encryption_screen,height=2,width=5).place(x=630,y=250)
    decrypt=tk.Text(encryption_screen,height=20,width=40).place(x=450,y=300)
    encryption_screen.mainloop()





def main_screen():
    window=tk.Tk()
    #Changing size of window to 800 by 800 pixels
    window.geometry('800x800')
    tk.Label(text='Cipher Suite', font=('Arial',25)).pack()

    tk.Button(text='Ecryption/Decryption Cipher', font=('Arial',25),bg='Green', fg='Red',height=5,command=Encryption).place(x=0,y=200)
    tk.Button(text='Chatserver', font=('Arial',25),bg='Black', fg='White',height=5,width=15).place(x=450,y=200)
    window.mainloop()

main_screen()