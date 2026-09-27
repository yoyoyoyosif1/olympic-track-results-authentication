# Olympic Track Results Database
# Milestone 2 - Encryption and User Authentication


def encrypt_password(password):
    encrypted = ""

    for i in range(len(password)):
        character = password[i]

        # Different positions use different shift amounts
        if i % 2 == 0:
            shift = 3
        else:
            shift = 5

        new_character = chr(ord(character) + shift)
        encrypted += new_character

    return encrypted


def main():
    print("Olympic Track Results Database")
    print("------------------------------")

    # Temporary test of our encryption algorithm
    password = input("Enter a password: ")

    encrypted_password = encrypt_password(password)

    print("Original password:", password)
    print("Encrypted password:", encrypted_password)


main()
