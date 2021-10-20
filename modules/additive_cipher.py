"""This module contains the encryption and decryption 
    logic corresponding to Additive Cipher
"""

# importing required modules, methods and constants
from constants import ENGLISH_ALPHABETS


def encrypt(message, key):
    """Method Defined for ENCRYPTION of a Simple String message 
    into a Cipher Text Using Additive Cipher Technique

    \nPARAMETERS\n
    message: string to be encrypted
    key: integer as key for the encryption

    \nRETURNS\n
    Cipher_Text: encrypted Message string
    """

    CipherText = ""
    message_chars = message.upper().split(" ")
    for part in message_chars:
        for i in part:
            if i in ENGLISH_ALPHABETS:
                index = (ENGLISH_ALPHABETS.index(i) + key) % 26
                CipherText += ENGLISH_ALPHABETS[index]
            else:
                print("Invalid Input\n")
                return
        CipherText += " "
    return CipherText[:-1]


def decrypt(CipherText, key):
    """Method Defined to DECRYPTION of a Cipher Text String 
    into the original Message Using Additive Cipher Technique

    \nPARAMETERS\n
    CipherText: string to be decrypted
    key: integer as key used while encryption

    \nRETURNS\n
    message: decrypted string of Original Message
    """
    message = ""
    CipherText_chars = CipherText.upper().split(" ")
    for part in CipherText_chars:
        for i in part:
            if i in ENGLISH_ALPHABETS:
                index = (ENGLISH_ALPHABETS.index(i) - key) % 26
                message += ENGLISH_ALPHABETS[index]
            else:
                print("Invalid Input\n")
                return
        message += " "
    return message[:-1]
