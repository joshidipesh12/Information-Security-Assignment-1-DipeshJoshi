"""module for centralized utility methods used 
    all over the project.
"""

# importing required modules, methods and constants
from constants import ENGLISH_ALPHABETS
import numpy as np


def string_to_Matrix_Z26(message_text, m_rows, n_cols) -> np.matrix:
    """Method Defined to convert a string to corresponding integer
    matrix to be used for 2x2 Hill Cipher Technique.
    \nNOTE: In case of 2x2 Hill Cipher, both m_rows and n_cols is 2

    \nPARAMETERS\n
    message_text: string to be converted
    m_rows: integer as number of rows (2)
    n_cols: integer as number of columns (2)

    \nRETURNS\n
    matrix: a numpy matrix reshaped to mxn
    """

    overflow_count = m_rows*n_cols - len(message_text)

    if overflow_count < 0:
        print("Invalid Input: m_rows x n_cols")
        return

    else:
        matrix_list = []
        for i in message_text.upper():
            if i in ENGLISH_ALPHABETS:
                matrix_list.append(ENGLISH_ALPHABETS.index(i))
            else:
                print("Invalid Input\n")
                return

        matrix_list = [ENGLISH_ALPHABETS.index(
            i) for i in message_text.upper()]
        for _ in range(overflow_count):  # adding trailing Z as Dummy Alphabet
            matrix_list.append(ENGLISH_ALPHABETS.index("Z"))
        matrix = np.matrix(matrix_list)

        return matrix.reshape(m_rows, n_cols, order="F")


def matrix_inverse_Z26(input_matrix: np.matrix):  # only for 2x2 matrix
    """Method Defined to calculate the inverse of 2x2 matrix
    in Z-26 to be used for 2x2 Hill Cipher Technique.
    In case of 2x2 Hill Cipher, both m_rows and n_cols is 2

    \nPARAMETERS\n
    input_matrix: a numpy matrix instance to be inversed

    \nRETURNS\n
    output_matrix: the inverse of input_matrix in Z-26
    """

    output_matrix = input_matrix.copy()

    if output_matrix.shape[0] != output_matrix.shape[1]:
        print("Not Invertible Matrix Recieved!")
        return

    else:
        determinant = None
        try:
            determinant = inverse_Z26(
                int(np.linalg.determinant(output_matrix)))
        except:
            print("Non-Invertible Matrix Recieved!")
            return determinant

        output_matrix[0, 0], output_matrix[1,
                                           1] = output_matrix[1, 1], output_matrix[0, 0]
        for i in range(output_matrix.shape[1]):
            for j in range(output_matrix.shape[0]):
                output_matrix[i, j] = determinant * \
                    pow(-1, i+j)*output_matrix[i, j]

        return np.matrix(output_matrix % 26)


def inverse_Z26(integer):
    """Method Defined to calculate the inverse of an Integer in Z-26 
    and avoiding ValueError is inverse doesn't exists

    \nPARAMETERS\n
    integer: input integer for inversion

    \nRETURNS\n
    inverse: the inverse of integer in Z-26 (or None if ValueError)
    """
    inverse = None
    try:
        inverse = pow(integer, -1, 26)
    except ValueError:
        print(f"Value of 'a' -> {integer} is Non-Invertible in Z-26.")

    return inverse
