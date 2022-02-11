#Adding Encryption for sending numbers

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




def generate_prime(number1,number2):
    n=int(number2-1)*int(number2-1)
    return (n)
    #public key

def generate_public(n):
    for i in range(100000000000):
        if n%i==0:
            continue
        else:
            e=i
    return e

def private_key(n,e):
    for i in range(1000000):
        if(i*e)%n==1:
            d=i
            return(d)

#encryption time baby

def encryption(string,e,n):
    word=list()
    for i in string:
        p=(alphabet[i]**e)%n
        word.append(p)
    return word

def decryption(word,d,n):
    letters=''
    for i in word:
        p=(i**d)%n
        letters.join(alphabet[p])
    return letters



