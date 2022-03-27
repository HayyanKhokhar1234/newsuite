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




class VernierCipher:
    def generateKey(string, key):

        key = list(key)
        key.pop(len(key)-1)
        print(key)
        if len(string) == len(key):
            return (key[0:len(key)-1])
        elif len(key)>len(string):
            key=key[0:len(string)]

        else:
            for i in range(len(string) - len(key)):

                if i=='\n':
                    break
                key.append(key[i % len(key)])
        print(key)
        print('Hi')
        return ("".join(key))

    def encryption(string, key):
        encrypt_text = []

        for i in range(len(string)):
            if string[i]=='\n':
                break
            print(string[i])
            if string[i]==' ':
                encrypt_text.append(' ')
                continue
            x = (alphabet[(string[i])] + alphabet[(key[i])])%26
            encrypt_text.append(alphabet2[x])
        return ("".join(encrypt_text))

    def decryption(encrypt_text, key):


        orig_text = []
        for i in range(len(encrypt_text)):

            if encrypt_text[i]=='\n':
                continue
            if encrypt_text[i]=='{':
                letters=letters+ ' '
                continue
            if encrypt_text[i]=='}':
                continue
            if encrypt_text[i]==' ':
                orig_text.append(' ')
                continue
            x = (alphabet[(encrypt_text[i])] - alphabet[(key[i])])%26
            orig_text.append(alphabet2[x])
        return ("".join(orig_text))


# string='Apple'
# a=VernierCipher.generateKey(string,'Banana')
# k=VernierCipher.encryption(string,a)
# e=VernierCipher.decryption(k,a)
# print(k)
# print(e)
# print(ord('A'))
# print(chr(ord('A')))