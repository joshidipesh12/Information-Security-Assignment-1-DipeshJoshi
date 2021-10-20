from string import ascii_uppercase as English_Alphabets
from modules.additive_cipher import decrypt
from constants import ENGLISH_LETTERS_SORTED


def possible_messages(cipher_text: str):
    """
    Method defined to perform Letter Frequency attack on Cipher Text 
    encrypted using Additive Cipher Technique returning 10 possible solutions.

    \nPARAMETERS\n
    cipher_text: encrypted message string

    \nRETURN\n
    possible_strings: a list of possible decryptions 
    in the order of likelihood (most to least)
    """

    possible_strings = dict({})  # key: string

    letter_frequencies = dict({i: 0 for i in English_Alphabets})

    for i in cipher_text.upper():
        if i in English_Alphabets:
            letter_frequencies[i] += 1

    sorted_letters = list(dict(sorted(letter_frequencies.items(),
                                      key=lambda item: item[1],
                                      reverse=True)).keys())

    for i in range(10):
        key = (English_Alphabets.index(sorted_letters[i])
               - English_Alphabets.index(ENGLISH_LETTERS_SORTED[i])) % 26
        possible_message = decrypt(cipher_text, key)
        possible_strings.update({key: possible_message})

    return list(possible_strings.values())