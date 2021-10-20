# importing required modules, methods and constants
from constants import ENGLISH_ALPHABETS
from utilities import inverse_Z26


def encrypt(message, a, b):
    """Method Defined for ENCRYPTION of a Simple String message 
    into a Cipher Text Using Affine Cipher Technique

    \nPARAMETERS\n
    message: string to be encrypted
    a: integer coefficient of x
    b: integer additive value

    \nRETURNS\n
    Cipher_Text: encrypted Message string
    """

    if inverse_Z26(a) == None:
        return

    Cipher_Text = ""
    message_chars = message.upper().split(" ")
    for char in message_chars:
        for i in char:
            if i in ENGLISH_ALPHABETS:
                index = ((a*ENGLISH_ALPHABETS.index(i))+b) % 26
                Cipher_Text += ENGLISH_ALPHABETS[index]
            else:
                print("Invalid Input\n")
                return
        Cipher_Text += " "
    return Cipher_Text[:-1]


def decrypt(Cipher_Text, a, b):
    """Method Defined to DECRYPTION of a Cipher Text String 
    into the original Message Using Affine Cipher Technique

    \nPARAMETERS\n
    CipherText: string to be decrypted
    a: integer coefficient of x
    b: integer additive value

    \nRETURNS\n
    message: decrypted string of Original Message
    """

    a_inverse = inverse_Z26(a)
    if a_inverse == None:
        return

    message = ""
    Cipher_Text_chars = Cipher_Text.upper().split(" ")
    for char in Cipher_Text_chars:
        for i in char:
            if i in ENGLISH_ALPHABETS:
                index = (a_inverse*(ENGLISH_ALPHABETS.index(i)-b)) % 26
                message += ENGLISH_ALPHABETS[index]
            else:
                print("Invalid Input\n")
                return
        message += " "
    return message[:-1]
