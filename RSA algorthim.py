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



class RSA:
    def N(num1,num2):
        return (num1*num2)


    def check_prime(num):
        check = False
        for i in range(num - 1):
            if i == 0:
                continue
            elif i == 1:
                continue
            if num % i == 0:
                return check
        check = True
        return check

    def generate_prime(number1,number2):
        one=RSA.check_prime(number1)
        two=RSA.check_prime(number2)
        if one ==False:
            return None
        elif two ==False:
            return None
        n = int(number1 - 1) * int(number2 - 1)
        return (n)
    #public key

    def generate_public(n):
        for i in range(100000000000):
            if i==0:
                continue
            elif (n%i)==0:

                continue
            else:
                print(i)
                e=i
                return e
        return('No number which is not a factor')
    def private_key(n,e):
        for i in range(1000000):
            if(i*e)%n==1:
                d=i
                print(d)
                return(d)

    def encryption(string,e,n):
        word=list()
        for i in string:
            if i==' ':
                word.append(i)
                continue
            p=(alphabet[i]**e)%n
            print(i)
            word.append(p)
        print(word)
        return word

    def decryption(word,d,n):
        letters=''
        for i in word:
            if i==' ':
                letters=letters+ ' '
                continue
            p=(i**d)%n
            letters=letters+alphabet2[p]
        print(letters)
        return letters



print(RSA.generate_prime(7,17))
N=RSA.N(7,17)
r=RSA.generate_prime(7,17)
f=RSA.generate_public(r)
e=RSA.private_key(r,f)

word=RSA.encryption('SHINGEKI NO KYOJIN',f,N)
wordz=RSA.decryption(word,e,N)