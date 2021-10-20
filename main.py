# importing required modules, methods and constants
import time
from modules import additive_cipher, affine_cipher, hill_cipher


def get_string_input(message="Enter: "):
    """Method Defined to take string inputs from user with 
    some default value and avoid exceptions


    PARAMETERS\n
    message: string to show as prompt for input (default: 'Enter: ')

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


if __name__ == "__main__":
    print("\n############# Information Security Assignment - 1 ###############")

    while True:
        time.sleep(0.8)
        print("\nSelect one of the options!")
        print("1. Encrypt a Message using Additive Cipher Method")
        print("2. Decrypt a Cipher Text using Additive Cipher Method")
        print("3. Encrypt a Message using Affine Cipher Method")
        print("4. Decrypt a Cipher Text using Affine Cipher Method")
        print("5. Perform Letter Frequency Attack on Text Encrypted using Additive Cipher")
        print("6. Perform Letter Frequency Attack on Text Encrypted using Monoalphabatic Substitution Cipher")
        print("7. Encrypt a Message using 2x2 Hill Cipher Method")
        print("8. Decrypt a Cipher Text using 2x2 Hill Cipher Method")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your Choice: "))
        except:
            choice = None

        if choice == 1:
            message = get_string_input("\nEnter Message Text: ")
            key = get_integer_input("Enter value of key (default 10): ")
            print(f"Encrypted Text: '{additive_cipher.encrypt(message, key)}'")

        elif choice == 2:
            cipher_text = get_string_input("\nEnter Cipher Text Text: ")
            key = get_integer_input("Enter value of key (default 10): ")
            print(
                f"Decrypted Text: '{additive_cipher.decrypt(cipher_text, key)}'")

        elif choice == 3:
            message = get_string_input("\nEnter Message Text: ")
            a = get_integer_input("Enter value of 'a' (default 10): ")
            b = get_integer_input("Enter value of 'b' (default 10): ")
            print(f"Encrypted Text: '{affine_cipher.encrypt(message, a, b)}'")

        elif choice == 4:
            cipher_text = get_string_input("\nEnter Cipher Text Text: ")
            a = get_integer_input("Enter value of 'a' (default 10): ")
            b = get_integer_input("Enter value of 'b' (default 10): ")
            print(
                f"Decrypted Text: '{affine_cipher.decrypt(cipher_text, a, b)}'")

        elif choice == 5:
            cipher_text = get_string_input(
                "\nEnter Cipher Text Text (encrypting using additive cipher): ")

        elif choice == 6:
            print("\nLetter Frequency Attack (Mono-Alphabatic Substitution Cipher)")

        elif choice == 7:
            message = get_string_input("\nEnter Message Text: ")
            key = get_string_input("Enter value of key (4 chars at max): ")
            print(f"Encrypted Text: '{hill_cipher.encrypt(message, key)}'")

        elif choice == 8:
            cipher_text = get_string_input("\nEnter Cipher Text Text: ")
            key = get_string_input("Enter value of key (4 chars at max): ")
            print(f"Decrypted Text: '{hill_cipher.decrypt(cipher_text, key)}'")

        elif choice == 0:
            print("\nHave A Noice Day!\n::Thank::You::")
            break

        else:
            print("\nInvalid Choice !")
