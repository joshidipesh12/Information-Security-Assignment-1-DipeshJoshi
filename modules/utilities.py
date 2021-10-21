""" ## Utilities 🛠
    module for centralized utility methods used 
    all over the project.
"""

# importing required modules, methods and constants
from constants import ENGLISH_ALPHABETS
import numpy as np
import math


def get_string_input(message="Enter: "):
    """Method Defined to take string inputs from user with
    some default value and avoid exceptions


    PARAMETERS\n
    message: string to show as prompt (default: 'Enter: ')

    RETURNS\n
    input_value: user input as string (default: ' ')
    """

    while(True):
        try:
            input_value = input(message) or " "
            break
        except:
            print("Invalid Input, Try again!\n")
    return input_value


def get_integer_input(message="Enter: "):
    """Method Defined to take integer inputs from user with
    some default value and avoid exceptions

    PARAMETERS\n
    message: string to show as prompt for input (default: 'Enter: ')

    RETURNS\n
    input_value: user input as integer (default: 10)
    """

    input_value = None
    while(True):
        try:
            input_value = int(input(message) or "10")
            break
        except:
            print("Invalid Input, Try again!\n")
    return input_value


def string_to_Matrix_Z26(message, m_rows, n_cols):
    """Method Defined to convert a string to \
    corresponding integer matrix to be used for \
    2x2 Hill Cipher.
    \nNOTE: In case of 2x2 Hill Cipher, both \
    m_rows and n_cols is 2

    \nPARAMETERS\n
    message: string to be converted
    m_rows: integer as number of rows (2)
    n_cols: integer as number of columns (2)

    \nRETURNS\n
    matrix: a numpy matrix reshaped to mxn
    """

    # calculating overflow
    # to fill with dimmy alphabets
    overflow_count = m_rows*n_cols - len(message)

    if overflow_count < 0:
        print("Invalid Input: m_rows x n_cols")
        return

    else:  # converting alphabets to numbers in Z-26

        matrix_list = []
        for i in message.upper():
            if i in ENGLISH_ALPHABETS:
                matrix_list.append(ENGLISH_ALPHABETS.index(i))
            else:  # inserting 'Z' inplace of other chars
                matrix_list.append(ENGLISH_ALPHABETS.index("Z"))

        for _ in range(overflow_count):
            # adding trailing Z as Dummy Alphabet
            matrix_list.append(ENGLISH_ALPHABETS.index("Z"))
        matrix = np.matrix(matrix_list)

        # returning mxn matrix with Fortran-like index order
        return matrix.reshape(m_rows, n_cols, order="F")


def matrix_inverse_Z26(input_matrix):
    """Method Defined to calculate the inverse of \
    2x2 matrix in Z-26 to be used for 2x2 Hill \
    Cipher Technique. In case of 2x2 Hill Cipher, \
    both m_rows and n_cols is 2.

    \nPARAMETERS\n
    input_matrix: a numpy matrix instance to be inversed

    \nRETURNS\n
    output_matrix: the inverse of input_matrix in Z-26
    """

    # creting copy of original matrix
    output_matrix = input_matrix.copy()

    if output_matrix.shape[0] != output_matrix.shape[1]:
        print("Not Invertible Matrix Recieved!")
        return

    else:  # trying to find inverse of determinant
        det_inverse = None
        try:
            det = np.linalg.det(output_matrix)
            det_inverse = inverse_Z26(math.floor(det))
        except:
            print("Non-Invertible Matrix Recieved!")
        if type(det_inverse) == type(None):
            return

        # switching values of indexes (i,i) type
        # for creating adjoint of original matrix
        temp = output_matrix[0, 0]
        output_matrix[0, 0] = output_matrix[1, 1]
        output_matrix[1, 1] = temp

        # creating adjoint and then output matrix
        for i in range(output_matrix.shape[1]):
            for j in range(output_matrix.shape[0]):
                adjoint = pow(-1, i+j)*output_matrix[i, j]
                output_matrix[i, j] = det_inverse * adjoint

        return np.matrix(output_matrix % 26)


def inverse_Z26(integer):
    """Method Defined to calculate the inverse of \
    an Integer in Z-26  and avoiding ValueError is \
    inverse doesn't exists

    \nPARAMETERS\n
    integer: input integer for inversion

    \nRETURNS\n
    inverse: the inverse of integer in Z-26 \
        (or None if ValueError)
    """

    inverse = None
    try:
        inverse = pow(integer, -1, 26)
    except ValueError:
        print(f"Value of 'a' -> {integer} is Non-Invertible in Z-26.")

    return inverse
