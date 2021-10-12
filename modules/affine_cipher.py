from string import ascii_uppercase as EA


def inverse_Z26(a):
    try:
        y = pow(a, -1, 26)
        return y
    except ValueError:
        print(f"Value of 'a' -> {a} is Non-Invertible in Z-26.")
        return None


def encrypt(m, a, b):
    if inverse_Z26(a) == None:
        return

    CT = ""
    message = m.upper().split(" ")
    for word in message:
        for i in word:
            if i in EA:
                index = ((a*EA.index(i))+b) % 26
                CT += EA[index]
            else:
                print("Invalid Input\n")
                return
        CT += " "
    return CT


def decrypt(C_text, a, b):
    a_inverse = inverse_Z26(a)
    if a_inverse == None:
        return

    message = ""
    CT = C_text.upper().split(" ")
    for word in CT:
        for i in word:
            if i in EA:
                index = (a_inverse*(EA.index(i)-b)) % 26
                message += EA[index]
            else:
                print("Invalid Input\n")
                return
        message += " "
    return message
