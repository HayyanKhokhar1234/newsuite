
class VernierCipher:
    def generateKey(string, key):
        key = list(key)
        if len(string) == len(key):
            return (key)
        else:
            for i in range(len(string) - len(key)):
                key.append(key[i % len(key)])
        print(key)
        return ("".join(key))

    def encryption(string, key):
        encrypt_text = []
        for i in range(len(string)):
            x = (ord(string[i]) + ord(key[i]))
            encrypt_text.append(chr(x))
        return ("".join(encrypt_text))

    def decryption(encrypt_text, key):
        orig_text = []
        for i in range(len(encrypt_text)):
            x = (ord(encrypt_text[i]) - ord(key[i]))
            orig_text.append(chr(x))
        return ("".join(orig_text))



a=VernierCipher.generateKey('Hello, my name is Hayyan.','B')
k=VernierCipher.encryption('Hello, my name is Hayyan.',a)
e=VernierCipher.decryption(k,a)
print(k)
print(e)
print(ord('A'))
print(chr(ord('A')))