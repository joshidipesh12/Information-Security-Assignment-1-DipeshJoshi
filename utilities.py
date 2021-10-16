import numpy as np


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


def inverse_Z26(a):
    try:
        y = pow(a, -1, 26)
        return y
    except ValueError:
        print(f"Value of 'a' -> {a} is Non-Invertible in Z-26.")
        return None
