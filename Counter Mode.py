#Have an initial constant value, and each time, you increment the value that you shift by one
alphabet={
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
    'Z':26

}

def encrypt(n,string):
    encrypted=""
    constant=n
    for i in len(string):
        encrypted.join(alphabet[string[i+n]])
        n+=1
    return(encrypted)
def decrypt(string,n):
    total=n+len(string)
    decrypted=""
    for i in len(string):
        decrypted.join(alphabet[string[i-total]])
        total-= 1

    return decrypted





string=input('Enter word')