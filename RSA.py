#Adding Encryption for sending numbers

#initial alphabet dictionary, this is for mapping values of letters to numbers
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
    'Z':0

}

#Second alphabet dictionary, used for mapping numbers to letters, used in decryption.
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



class RSAalgo:
    #Finds product of two primes
    def N(num1,num2):
        return (num1*num2)

    #Used to check if two numbers are prime
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
    #generates a number which is equal to (primenumber-1)*(primenumber-2), and check if the numbers are prime.
    def generate_prime(number1,number2):
        one=RSAalgo.check_prime(number1)
        two=RSAalgo.check_prime(number2)
        if one ==False:
            return None
        elif two ==False:
            return None
        n = int(number1 - 1) * int(number2 - 1)
        return (n)
    #public key
    #generates a public key which is used to encrypt the data
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

    #generates private key used to decrypt the data.
    def private_key(n,e):
        for i in range(1000000):
            if(i*e)%n==1:
                d=i
                print(d)
                return(d)
    #Encrypts the data by mapping each letter to integers then appending it to the list
    def encryption(string,e,N):
        word=list()
        for i in string:
            if i=='\n':
                continue
            elif i==' ':
                word.append(i)
                continue

            p=(alphabet[i]**e)%N
            print(i)
            word.append(p)
        print(word)
        return word
    #Decrypts data by mapping each number to letter then appending it to string.
    def decryption(word,d,N):
        word=word.split(' ')
        print(word)
        letters=''
        for i in word:
            if i==' ':
                letters=letters+ ' '
                continue
            p=(int(i)**d)%N
            letters=letters+alphabet2[p]
        print(letters)
        return letters


#num1=3
#num2=5
#print(RSA.generate_prime(num1,num2))
#N=RSA.N(num1,num2)
#r=RSA.generate_prime(num1,num2)

#e=RSA.generate_public(r)
#d=RSA.private_key(r,e)

#word=RSA.encryption('APPLE',e,N)
#wordz=RSA.decryption(word,d,N)