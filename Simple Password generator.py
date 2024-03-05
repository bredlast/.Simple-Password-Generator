import string
import random
import os

def generate_password(length, use_special_chars=True, use_numbers=True):
    """Generate a random password of specified length with optional special characters and numbers."""
    all_characters = string.ascii_letters
    if use_special_chars:
        all_characters += string.punctuation
    if use_numbers:
        all_characters += string.digits
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def save_password(password, name):
    """Save the generated password to a file with a specified name."""
    with open(f"{name}_password.txt", "w") as f:
        f.write(password)

def look_at_saved_passwords():
    """Print the contents of all saved password files."""
    for filename in os.listdir():
        if filename.endswith("_password.txt"):
            with open(filename, "r") as f:
                print(f"{filename}: {f.read()}")

if __name__ == "__main__":
    while True:
        print("\nPassword Manager Menu")
        print("1. Generate a new password")
        print("2. Look at saved passwords")
        print("3. Quit")

        option = int(input("Enter your choice (1-3): "))

        if option == 1:
            name = input("Enter a name for the password: ")
            length = int(input("Enter the length of the password: "))
            use_special_chars = input("Include special characters? (yes/no) ").lower() == "yes"
            use_numbers = input("Include numbers? (yes/no) ").lower() == "yes"
            while True:
                password = generate_password(length, use_special_chars, use_numbers)
                print(f"Generated password: {password}")
                confirm = input("Do you like this password? (yes/no) ")
                if confirm == "yes":
                    save_password(password, name)
                    print(f"Generated and saved password for {name}.")
                    break
                elif confirm == "no":
                    print("Enter the new length of the password: ")
                else:
                    print("Invalid response. Please enter 'yes' or 'no'.")

        elif option == 2:
            look_at_saved_passwords()

        elif option == 3:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")