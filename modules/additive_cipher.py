""" # Additive Cipher
    This module contains the encryption & decryption \
    logic corresponding to Additive Cipher
"""

# importing required modules, methods and constants
from constants import ENGLISH_ALPHABETS


def encrypt(message, key):
    """Method Defined for ENCRYPTION of Simple String \
    message into a Cipher Text Using Additive Cipher.

    \nPARAMETERS\n
    message: string to be encrypted
    key: integer as key for the encryption

    \nRETURNS\n
    Cipher_Text: encrypted Message string
    """

    CipherText = ""

    # converting message chars to uppercase
    # and segmenting spaces
    message_chars = message.upper().split(" ")
    for part in message_chars:
        for i in part:

            # using english aplhabet indexes
            # to find shift key
            if i in ENGLISH_ALPHABETS:
                index = (
                    ENGLISH_ALPHABETS.index(i) + key
                ) % 26
                CipherText += ENGLISH_ALPHABETS[index]

            else:  # if invalid character is encountered
                CipherText += i
        CipherText += " "

    # the last is leftout because of trailing space
    return CipherText[:-1]


def decrypt(CipherText, key):
    """Method Defined to DECRYPTION of Cipher Text \
    String into the original Message Using Additive \
    Cipher Technique

    \nPARAMETERS\n
    CipherText: string to be decrypted
    key: integer as key used while encryption

    \nRETURNS\n
    message: decrypted string of Original Message
    """

    message = ""

    # converting message chars to uppercase and segmenting spaces
    CipherText_chars = CipherText.upper().split(" ")
    for part in CipherText_chars:
        for i in part:

            if i in ENGLISH_ALPHABETS:
                index = (ENGLISH_ALPHABETS.index(i) - key) % 26
                message += ENGLISH_ALPHABETS[index]

            else:  # if invalid character is encountered
                message += i
                return
        message += " "

    # the last is leftout because of trailing space
    return message[:-1]
