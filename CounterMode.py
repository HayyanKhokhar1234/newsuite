#Have an initial constant value, and each time, you increment the value that you shift by one
alphabet1={
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    'I':9,
    'J':10,
    'K':11,
    'L':12,
    'M':13,
    'N':14,
    'O':15,
    'P':16,
    'Q':17,
    'R':18,
    'S':19,
    'T':20,
    'U':21,
    'V':22,
    'W':23,
    'X':24,
    'Y':25,
    'Z':0
}
alphabet2={
    1:'A',
    2:'B',
    3:'C',
    4:'D',
    5:'E',
    6:'F',
    7:'G',
    8:'H',
    9:'I',
    10:'J',
    11:'K',
    12:'L',
    13:'M',
    14:'N',
    15:'O',
    16:'P',
    17:'Q',
    18:'R',
    19:'S',
    20:'T',
    21:'U',
    22:'V',
    23:'W',
    24:'X',
    25:'Y',
    0:'Z'

}
class Countermode:
    #This is used to encrypt the string, where we essentnailly encrypt the data.
    def encrypt(n,string):
        encrypted=""
        constant=n
        for i in range(len(string)):
            if string[i]=='\n':
                break
            if string[i]==" ":
                encrypted= encrypted+ " "
                continue
            p=string[i]
            encrypted=encrypted+(alphabet2[((alphabet1[string[i]]+n)%26)])
            n+=1
        return(encrypted)
    #This is used to decrypt the string, by looping through the string, and then decreasing the integer mapepd value of the letter by n which is a constant, and then incrementing n by one.
    def decrypt(string,n):
        decrypted=""
        for i in range(len(string)):
            if string[i]=='\n':
                break
            if string[i]==" ":
                decrypted=decrypted+" "
                continue
            else:
                decrypted=decrypted+(alphabet2[((alphabet1[string[i]]-n)%26)])
                n+= 1
        return decrypted





string='APPLE'
key=25
c=Countermode.encrypt(key,string)
Countermode.decrypt(c,key)