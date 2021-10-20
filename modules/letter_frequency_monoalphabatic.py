from constants import ENGLISH_LETTERS_SORTED


def possible_messages(cipher_text):
    """
    Method defined to perform Letter Frequency attack on Cipher Text 
    encrypted using generalized Mono-Alphabatic Substitution Cipher 
    Technique returning 10 possible solutions.

    \nPARAMETERS\n
    cipher_text: encrypted message string

    \nRETURN\n
    possible_strings: a list of possible decryptions 
        in the order of likelihood (most to least)
    """

    message_length = len(cipher_text)
    possible_strings = []

    letter_frequencies = [0] * 26
    letters_sorted_by_frequencies = [None] * 26

    used_letters = [0] * 26

    for i in range(message_length):
        if cipher_text[i] != ' ':
            letter_frequencies[ord(cipher_text[i]) - 65] += 1

    # Copying the frequency list
    letters_sorted_by_frequencies = letter_frequencies.copy()
    letters_sorted_by_frequencies.sort(reverse=True)

    for i in range(10):
        position_check = -1

        for j in range(26):
            if (letters_sorted_by_frequencies[i] == letter_frequencies[j]
                    and used_letters[j] == 0):
                used_letters[j] = 1
                position_check = j
                break

        if position_check == -1:
            break

        numeric_value = ord(ENGLISH_LETTERS_SORTED[i]) - 65
        numeric_value -= position_check

        possible_message = ""

        for k in range(message_length):
            if cipher_text[k] == ' ':
                possible_message += " "
                continue

            current_num_value = ord(cipher_text[k]) - 65
            current_num_value += numeric_value

            if current_num_value < 0:
                current_num_value += 26
            if current_num_value > 25:
                current_num_value -= 26

            possible_message += chr(current_num_value + 65)
        possible_strings.append(possible_message)
    return possible_strings
