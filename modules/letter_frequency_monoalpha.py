""" ## Letter Frequency Attack (Mono-Alphabatic \
    Substitution)
    This module contains Letter Frequency Attack logic 
    corresponding to Monoalphabatic Substitution Cipher
"""

# importing required modules, methods and constants
from constants import ENGLISH_LETTERS_SORTED


def possible_messages(cipher_text):
    """Method defined to perform Letter Frequency attack \
    on Cipher Text encrypted using generalized Mono \
    Alphabatic Substitution Cipher Technique returning \
    10 possible solutions.

    \nPARAMETERS\n
    cipher_text: encrypted message string

    \nRETURN\n
    possible_strings: a list of possible decryptions 
        in the order of likelihood (most to least)
    """

    # defining variables
    message_length = len(cipher_text)
    possible_strings = []

    # list to store frequencies
    letter_frequency = [0] * 26
    frequencies_sorted = [None] * 26

    used_letters = [0] * 26

    # looping though message and storing frequencies
    for i in range(message_length):
        if cipher_text[i] != ' ':
            letter_frequency[ord(cipher_text[i]) - 65] += 1

    # Copying the frequency list
    frequencies_sorted = letter_frequency.copy()
    frequencies_sorted.sort(reverse=True)

    # calculating 10 possible plain texts
    for i in range(10):
        position_check = -1

        for j in range(26):
            if (frequencies_sorted[i] == letter_frequency[j]
                    and used_letters[j] == 0):
                used_letters[j] = 1
                position_check = j
                break

        if position_check == -1:
            break

        # Storing the numerical equivalent of letter
        # at ith index of array
        # Calculate the probable shift used in
        # monoalphabetic cipher
        numeric_value = ord(ENGLISH_LETTERS_SORTED[i]) - 65
        numeric_value -= position_check

        possible_message = ""

        for j in range(message_length):
            if cipher_text[j] == ' ':
                possible_message += " "
                continue

            # Shifting the jth letter of the cipher
            current_num_value = ord(cipher_text[j]) - 65
            current_num_value += numeric_value

            if current_num_value < 0:
                current_num_value += 26
            if current_num_value > 25:
                current_num_value -= 26

            possible_message += chr(current_num_value + 65)
        possible_strings.append(possible_message)

    return possible_strings
