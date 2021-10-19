from constants import ENGLISH_LETTERS_SORTED_BY_FREQUENCY


def possible_messages(message):
    message_length = len(message)
    plain_texts = []

    letter_frequencies = [0] * 26
    letters_sorted_by_frequencies = [None] * 26

    used_letters = [0] * 26

    for i in range(message_length):
        if message[i] != ' ':
            letter_frequencies[ord(message[i]) - 65] += 1

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

        numeric_value = ord(ENGLISH_LETTERS_SORTED_BY_FREQUENCY[i]) - 65
        numeric_value -= position_check

        possible_message = ""

        for k in range(message_length):
            if message[k] == ' ':
                possible_message += " "
                continue

            current_num_value = ord(message[k]) - 65
            current_num_value += numeric_value

            if current_num_value < 0:
                current_num_value += 26
            if current_num_value > 25:
                current_num_value -= 26

            possible_message += chr(current_num_value + 65)
        plain_texts.append(possible_message)
    return plain_texts


def most_probable(message):
    all_possible = possible_messages(message)
    return all_possible[0]
