# importing required modules, methods and constants
from utilities import matrix_inverse_Z26, string_to_Matrix_Z26
from constants import ENGLISH_ALPHABETS
import math


def encrypt(message_text, key):
    """
    Method Defined for ENCRYPTION of a Simple String message 
    into a Cipher Text Using 2x2 Hill Cipher Technique

    \nPARAMETERS\n
    message_text: string to be encrypted
    key: integer key for encryption

    \nRETURNS\n
    cipher_text: encrypted Message string
    """

    # for 2x2 Hill Cipher the length of key must be <= 4
    # print("Warning: All Spaces with be lost!")
    cipher_text = ""

    key_matrix = None
    if len(key) <= 4:
        key_matrix = string_to_Matrix_Z26(key, 2, 2)
    else:
        print("Length of Key must be less than 5 for 2x2 Hill Cipher")
        return

    pairs = math.ceil((len(message_text)/2))
    matrix = string_to_Matrix_Z26(message_text, 2, pairs)

    for i in range(pairs):
        result_char = (key_matrix*matrix[:, i]) % 26
        cipher_text += ENGLISH_ALPHABETS[result_char[0, 0]]
        cipher_text += ENGLISH_ALPHABETS[result_char[1, 0]]

    return cipher_text


def decrypt(cipher_text, key):
    """
    Method Defined for DECRYPTION of a String Cipher Text 
    into the original message Using 2x2 Hill Cipher Technique

    \nPARAMETERS\n
    cipher_text: string to be decrypted
    key: integer key used while encryption

    \nRETURNS\n
    message: decrypted Message string
    """

    message_text = ""

    key_matrix = None
    if len(key) <= 4:
        key_matrix = string_to_Matrix_Z26(key, 2, 2)
        key_matrix = matrix_inverse_Z26(key_matrix)
    else:
        print("Length of Key must be less than 5 for 2x2 Hill Cipher")
        return

    pairs = math.ceil((len(cipher_text)/2))
    matrix = string_to_Matrix_Z26(cipher_text, 2, pairs)

    for i in range(pairs):
        result_char = (key_matrix*matrix[:, i]) % 26
        message_text += ENGLISH_ALPHABETS[result_char[0, 0]]
        message_text += ENGLISH_ALPHABETS[result_char[1, 0]]

    return message_text
