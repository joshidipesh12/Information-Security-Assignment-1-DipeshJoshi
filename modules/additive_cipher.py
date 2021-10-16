from string import ascii_uppercase as English_Alphabet


def encrypt(m, key):
    CT = ""
    message = m.upper().split(" ")
    for part in message:
        for i in part:
            if i in English_Alphabet:
                index = (English_Alphabet.index(i) + key) % 26
                CT += English_Alphabet[index]
            else:
                print("Invalid Input\n")
                return
        CT += " "
    return CT


def decrypt(C_text, key):
    message = ""
    CT = C_text.upper().split(" ")
    for part in CT:
        for i in part:
            if i in English_Alphabet:
                index = (English_Alphabet.index(i) - key) % 26
                message += English_Alphabet[index]
            else:
                print("Invalid Input\n")
                return
        message += " "
    return message
