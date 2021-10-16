from string import ascii_uppercase as English_Alphabet
import numpy as np
import math

from affine_cipher import inverse_Z26


def matrix_inverse_Z26(matrix: np.matrix):  # only for 2x2 matrix
    if matrix.shape[0] != matrix.shape[1]:
        print("Not Invertible Matrix Recieved!")
        return

    else:
        determinant = None
        try:
            determinant = inverse_Z26(int(np.linalg.determinant(matrix)))
        except:
            print("Non-Invertible Matrix Recieved!")
            return

        matrix[0, 0], matrix[1, 1] = matrix[1, 1], matrix[0, 0]
        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[0]):
                matrix[i, j] = determinant*pow(-1, i+j)*matrix[i, j]

        return matrix % 26


def string_to_Matrix_Z26(message_text, m_rows, n_cols):
    overflow_count = m_rows*n_cols - len(message_text)

    if overflow_count < 0:
        print("Invalid Input: m_rows x n")
        return

    else:
        matrix = []
        for i in message_text.upper():
            if i in English_Alphabet:
                matrix.append(English_Alphabet.index(i))
            else:
                print("Invalid Input\n")
                return

        matrix = [English_Alphabet.index(i) for i in message_text.upper()]
        for _ in range(overflow_count):  # adding trailing Z as Dummy Alphabet
            matrix.append(English_Alphabet.index("Z"))
        matrix = np.matrix(matrix)

        return matrix.reshape(m_rows, n_cols, order="F")


def encrypt(message_text, key):  # for 2x2 Hill Cipher the length of key must be <= 4
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
        cipher_text += English_Alphabet[result_char[0, 0]]
        cipher_text += English_Alphabet[result_char[1, 0]]

    return cipher_text


def decrypt(cipher_text, key):
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
        message_text += English_Alphabet[result_char[0, 0]]
        message_text += English_Alphabet[result_char[1, 0]]

    return message_text
