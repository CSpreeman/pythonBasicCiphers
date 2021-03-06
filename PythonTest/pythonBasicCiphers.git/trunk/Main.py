import caesar
import vigenere

MAX_KEY_SIZE = 26


def getMode():
    while True:
        print('Do you wish to Encrypt or Decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "Encrypt" or "E" or "Decrypt" or "D".')

def getType():
    while True:
        print('Which Cipher would you like to use?')
        cipher = input().lower()
        if cipher in 'caesar c vigenere v'.split():
            return cipher
        else:
            print('Enter either "Caesar" or "C" or "Vigenere" or "V".')


def getMessage():
    print('Enter your message:')
    return input()


def getKey():
    while True:
        if cipher[0] == 'c':
            try:
                print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
                key = int(input())
                if (key >= 1 and key <= MAX_KEY_SIZE):
                    return key
            except:
                print("Looks like you didnt type a number try again!")
                continue
        else:
            try:
                print('Please enter a Key')
                key = input()
                if key.isalpha():
                    return key
            except:
                print('Looks like you entered an invalid key, Vigenere keys must be all letters! try again!')
                continue


def getTranslatedMessage(mode, cipher, message, key):
    if mode[0] == 'd' and cipher[0] == 'c':
        key = -key
    translated = ''

    if cipher[0] == 'c':
        translated = caesar.caesar.caesar_cipher(message, key)
    else:
        if mode[0] == 'e':
            translated = vigenere.encryptMessage(key, message)
        else:
            translated = vigenere.decryptMessage(key, message)
    return translated


mode = getMode()
cipher = getType()
message = getMessage()
key = getKey()


print('Your translated text is:')
print(getTranslatedMessage(mode, cipher, message, key))