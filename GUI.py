import tkinter as tk
import RSA, VernierCipher, CounterMode
from RSA import RSAalgo

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




def encryption_back():
    encryption_screen.destroy()

def Encryption():

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
    def option_changed2(choice):

        tk.Label(encryption_screen, text=f'You have selected: {variable2.get()}').place(x=600, y=230)



    #making encryption_Screen global for easier use across program

    #making a screen for the encryption/decryption cipher
    encryption_screen=tk.Tk()
    encryption_screen.title('Encryption Cipher')
    encryption_screen.geometry('800x800')

    tk.Label(encryption_screen,text='Encryption/Decryption Suite', font=('Arial', 25), bg='Green').pack()
    tk.Button(encryption_screen,text='Back',font=('Arial',15),command=encryption_back,bg='Red').pack()
    variable=tk.StringVar()
    drop=tk.OptionMenu(encryption_screen, variable, 'Vernier Cipher','RSA','Counter Mode','Ceaser Cipher',command=option_changed).place(x=0,y=200)
    print(variable.get())

    p1=tk.Text(encryption_screen, height=2,width=5)
    p1.place(x=70,y=250)
    p2=tk.Text(encryption_screen, height=2, width=5)
    p2.place(x=140,y=250)

    encryption = tk.Text(encryption_screen, height=20, width=40)
    encryption.place(x=0,y=300)
    tk.Button(encryption_screen, text='Encrypt', bg='Green', command=encrypt).place(x=0, y=250)




    variable2=tk.StringVar()
    variable2.set('Select An encryption')

    tk.Button(encryption_screen, text='Decrypt', bg='Red',command=decrypt).place(x=750, y=250)
    drop2=tk.OptionMenu(encryption_screen, variable2, 'Vernier Cipher','RSA','Counter Mode','Ceaser Cipher',command=option_changed2).place(x=700,y=200)
    p3=tk.Text(encryption_screen,height=2,width=5)
    p3.place(x=680,y=250)
    p4=tk.Text(encryption_screen,height=2,width=5)
    p4.place(x=640,y=250)
    p5=tk.Text(encryption_screen,height=2,width=5)
    p5.place(x=590,y=250)

    decryption=tk.Text(encryption_screen,height=20,width=40)
    decryption.place(x=450,y=300)




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