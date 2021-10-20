"""main module for project execution
    start by running `python3 main.py`
"""

__version__ = '0.1'
__author__ = 'Dipesh Joshi'

# importing required modules, methods and constants
import time
from modules import (
    additive_cipher,
    affine_cipher,
    hill_cipher,
    letter_frequency_additive,
    letter_frequency_monoalphabatic
)


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


if __name__ == "__main__":
    print("\n########## Information Security Assignment - 1 ##########")

    while True:
        time.sleep(1)
        print("\nSelect one of the options!")
        print("1.Encrypt a Message using Additive Cipher Method")
        print("2.Decrypt a Cipher Text using Additive Cipher Method")
        print("3.Encrypt a Message using Affine Cipher Method")
        print("4.Decrypt a Cipher Text using Affine Cipher Method")
        print("5.Perform Letter Frequency Attack (Additive Cipher)")
        print("6.Perform option-5 (Monoalphabatic Substitution Cipher)")
        print("7.Encrypt a Message using 2x2 Hill Cipher Method")
        print("8.Decrypt a Cipher Text using 2x2 Hill Cipher Method")
        print("0.Exit")

        try:
            choice = int(input("\nEnter your Choice: "))
        except:
            choice = None

        if choice == 1:
            message = get_string_input("\nEnter Message Text: ")
            key = get_integer_input("Enter value of key (default 10): ")
            print("Encrypted Text")
            print(f"\t'{additive_cipher.encrypt(message, key)}'")

        elif choice == 2:
            cipher_text = get_string_input("\nEnter Cipher Text Text: ")
            key = get_integer_input("Enter value of key (default 10): ")
            print("Decrypted Text")
            print(f"\t'{additive_cipher.decrypt(cipher_text, key)}'")

        elif choice == 3:
            message = get_string_input("\nEnter Message Text: ")
            a = get_integer_input("Enter value of 'a' (default 10): ")
            b = get_integer_input("Enter value of 'b' (default 10): ")
            print("Encrypted Text")
            print(f"\t'{affine_cipher.encrypt(message, a, b)}'")

        elif choice == 4:
            cipher_text = get_string_input("\nEnter Cipher Text Text: ")
            a = get_integer_input("Enter value of 'a' (default 10): ")
            b = get_integer_input("Enter value of 'b' (default 10): ")
            print("Decrypted Text")
            print(f"\t'{affine_cipher.decrypt(cipher_text, a, b)}'")

        elif choice == 5:
            text = get_string_input(
                "\nEnter Cipher Text (encrypted by additive cipher): ")
            print("\nPerforming Letter Frequency Attack.....")
            time.sleep(2)
            print("Top 10 Results ->")
            results = letter_frequency_additive.possible_messages(text)
            for i in range(len(results)):
                print(f"\t{i+1}. {results[i]}")

        elif choice == 6:
            text = get_string_input(
                "\nEnter Cipher Text (Mono-Alphabatic Substitution): ")
            print("\nPerforming Letter Frequency Attack.....")
            time.sleep(2)
            print("\nTop 10 Results ->")
            results = letter_frequency_monoalphabatic.possible_messages(text)
            for i in range(len(results)):
                print(f"\t{i+1}. {results[i]}")

        elif choice == 7:
            message = get_string_input("\nEnter Message Text: ")
            key = get_string_input("Enter value of key (4 chars max): ")
            print("Encrypted Text")
            print(f"\t'{hill_cipher.encrypt(message, key)}'")

        elif choice == 8:
            cipher_text = get_string_input("\nEnter Cipher Text Text: ")
            key = get_string_input("Enter value of key (4 chars max): ")
            print("Decrypted Text")
            print(f"\t'{hill_cipher.decrypt(cipher_text, key)}'")

        elif choice == 0:
            print("\nHave A Noice Day!\n::Thank::You::")
            break

        else:
            print("\nInvalid Choice !")
