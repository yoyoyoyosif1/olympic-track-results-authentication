import os

def encrypt(text):
    encrypted = ""

    for i in range(len(text)):
        if i % 2 == 0:
            encrypted += chr(ord(text[i]) + 3)
        else:
            encrypted += chr(ord(text[i]) + 5)

    return encrypted


print("Olympic Track Results Database")
print()
print("1. Create an Account")
print("2. Log In")

choice = input("Enter choice: ")


if choice == "1":
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    encrypted_password = encrypt(password)

    file = open("users.txt", "a")
    file.write(username + "," + encrypted_password + "\n")
    file.close()

    print("Account created successfully!")


elif choice == "2":

    if os.path.exists("users.txt"):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        encrypted_password = encrypt(password)

        file = open("users.txt", "r")

        login_successful = False

        for line in file:
            account = line.strip().split(",")

            if username == account[0] and encrypted_password == account[1]:
                login_successful = True

        file.close()

        if login_successful:
            print("Login successful!")
            print("Welcome to the Olympic Track Results Database!")
        else:
            print("Incorrect username or password.")

    else:
        print("No accounts have been created yet.")


else:
    print("Invalid choice.")