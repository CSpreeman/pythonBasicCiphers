import string

class caesar():


    def caesar_cipher(user_message, user_shift):
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[user_shift:] + alphabet[:user_shift]
        table = str.maketrans(alphabet, shifted_alphabet)
        return user_message.translate(table)


