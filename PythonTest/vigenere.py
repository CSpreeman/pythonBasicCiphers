
class vigenere():


    def vigenere_cipher(key, message, mode):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        translated = [] # stores the encrypted/decrypted message string
        keyIndex = 0
        key = key.upper()
        for symbol in message: # loop through each character in message
            num = LETTERS.find(symbol.upper())
            if num != -1: # -1 means symbol.upper() was not found in LETTERS
                if mode == 'encrypt':
                    num += LETTERS.find(key[keyIndex]) # add if encrypting
                elif mode == 'decrypt':
                    num -= LETTERS.find(key[keyIndex]) # subtract if decrypting
                num %= len(LETTERS) # handle the potential wrap-around
                if symbol.isupper():
                    translated.append(LETTERS[num])
                elif symbol.islower():
                    translated.append(LETTERS[num].lower())
                keyIndex += 1 # move to the next letter in the key
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                translated.append(symbol)
        return ''.join(translated)


def encryptMessage(key, message):
    return vigenere.vigenere_cipher(key, message, 'encrypt')


def decryptMessage(key, message):
    return vigenere.vigenere_cipher(key, message, 'decrypt')
