import tkinter as tk
import RSA, VernierCipher, CounterMode
from RSA import RSAalgo
from threading import Thread
from socket import AF_INET, socket, SOCK_STREAM




def encrypt():
    if variable.get() == 'RSA':
        int1 = int(p1.get("1.0", "end"))
        int2 = int(p2.get("1.0", "end"))


        N = RSAalgo.N(int1, int2)
        r = RSAalgo.generate_prime(int1, int2)
        e = RSAalgo.generate_public(r)
        d = RSAalgo.private_key(r, e)
        print(encryption.get("1.0", "end"))
        result = RSAalgo.encryption(encryption.get("1.0", "end"), e, N)
        print(result)

        encryption.delete('1.0', 'end')
        encryption.insert('1.0', result)
        tk.Label(encryption_screen,text=f"Your private Key is {d}").place(x=250,y=200)

    if variable.get()=='Counter Mode':
        int1 = int(p1.get("1.0", "end"))
        result=CounterMode.Countermode.encrypt(int1,encryption.get("1.0", "end"))
        encryption.delete('1.0', 'end')
        encryption.insert('1.0', result)
    if variable.get()=='Vernier Cipher':
        key=p1.get('1.0','end')
        print(key)
        key2=VernierCipher.VernierCipher.generateKey(encryption.get("1.0", "end"),key)
        result = VernierCipher.VernierCipher.encryption(encryption.get("1.0", "end"),key2)
        encryption.delete('1.0', 'end')
        encryption.insert('1.0', result)
        print(result)
        tk.Label(encryption_screen, text=f"Your private Key is {key2}").place(x=250, y=200)


def decrypt():
    if variable2.get()=='RSA':
        int3=int(p3.get('1.0','end'))
        int4=int(p4.get('1.0','end'))
        int5=int(p5.get('1.0','end'))
        N=RSAalgo.N(int3,int4)
        result=RSAalgo.decryption(decryption.get('1.0','end'),int5,N)
        decryption.delete('1.0','end')
        decryption.insert('1.0',result)
    if variable2.get()=='Counter Mode':
        int3=int(p3.get('1.0','end'))
        result=CounterMode.Countermode.decrypt(decryption.get('1.0','end'),int3)
        decryption.delete('1.0', 'end')
        decryption.insert('1.0', result)
    if variable2.get()=='Vernier Cipher':
        key=p3.get('1.0','end')
        result=VernierCipher.VernierCipher.decryption(decryption.get('1.0','end'),key)
        decryption.delete('1.0', 'end')
        decryption.insert('1.0', result)



def encryption_back():
    encryption_screen.destroy()

def Encryption():
    #These are all global varables that will be used when encrypting data
    global encryption_screen
    global p1
    global p2
    global p3
    global p4
    global p5
    global encryption
    global decryption
    global variable
    global variable2
    #This is a function used to see which algorthim is selected from drop down menu
    def option_changed(choice):

        tk.Label(encryption_screen, text=f'You have selected: {variable.get()}').place(x=0, y=230)
        print(variable.get())
    #Same purpose, just to see which algorthim is selected from drop down menu.
    def option_changed2(choice):

        tk.Label(encryption_screen, text=f'You have selected: {variable2.get()}').place(x=600, y=230)



    #making encryption_Screen global for easier use across program

    #making a screen for the encryption/decryption cipher
    encryption_screen=tk.Tk()
    encryption_screen.title('Encryption Cipher')
    encryption_screen.geometry('800x800')

    #This label s used to show that the page applicaton is for encrypting/decrypting data
    tk.Label(encryption_screen,text='Encryption/Decryption Suite', font=('Arial', 25), bg='Green').pack()
    #This button is used to go back.
    tk.Button(encryption_screen,text='Back',font=('Arial',15),command=encryption_back,bg='Red').pack()
    #Used to store the algorthim selected from drop down menu
    variable=tk.StringVar()
    #The drop down menu
    drop=tk.OptionMenu(encryption_screen, variable, 'Vernier Cipher','RSA','Counter Mode',command=option_changed).place(x=0,y=200)
    print(variable.get())
    #The texts used for encrypting data
    p1=tk.Text(encryption_screen, height=2,width=5)
    p1.place(x=70,y=250)
    p2=tk.Text(encryption_screen, height=2, width=5)
    p2.place(x=140,y=250)
    #encryption text box to enter encryped text
    encryption = tk.Text(encryption_screen, height=20, width=40)
    encryption.place(x=0,y=300)
    #encryption button to encrypt data
    tk.Button(encryption_screen, text='Encrypt', bg='Green', command=encrypt).place(x=0, y=250)



    #second variable selected from drop down menu to select algorthim to decrypt text.
    variable2=tk.StringVar()
    variable2.set('Select An encryption')
    #Button to decrypt text
    tk.Button(encryption_screen, text='Decrypt', bg='Red',command=decrypt).place(x=750, y=250)
    #Second drop down menu to select encryption algorthim
    drop2=tk.OptionMenu(encryption_screen, variable2, 'Vernier Cipher','RSA','Counter Mode','Ceaser Cipher',command=option_changed2).place(x=700,y=200)
    #Text boxes to encrypt data.
    p3=tk.Text(encryption_screen,height=2,width=5)
    #p3 Another textbox used to enter a private key for RSA algorthim
    p3.place(x=680,y=250)
    p4=tk.Text(encryption_screen,height=2,width=5)
    #p4 is used for a textbox to enter a second key if needed
    p4.place(x=640,y=250)
    p5=tk.Text(encryption_screen,height=2,width=5)
    #p5 used to enter key for decryptng
    p5.place(x=590,y=250)

    decryption=tk.Text(encryption_screen,height=20,width=40)
    decryption.place(x=450,y=300)




    encryption_screen.mainloop()





def main_screen():
    global window






    window=tk.Tk()
    #Changing size of window to 800 by 800 pixels
    window.geometry('800x800')
    tk.Label(text='Cipher Suite', font=('Arial',25)).pack()

    tk.Button(text='Ecryption/Decryption Cipher', font=('Arial',25),bg='Green', fg='Red',height=5,command=Encryption).place(x=0,y=200)
    tk.Button(text='Chatserver', font=('Arial',25),bg='Black', fg='White',height=5,width=15).place(x=450,y=200)



    window.mainloop()


main_screen()
