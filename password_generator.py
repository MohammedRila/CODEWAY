import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    # Define character sets based on specified complexity
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Generate password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_to_file(passwords):
    try:
        with open("generated_passwords.txt", "w") as file:
            for password in passwords:
                file.write(password + "\n")
        print("Passwords saved to generated_passwords.txt")
    except Exception as e:
        print("An error occurred while saving passwords:", e)

def main():
    try:
        # Prompt the user for password length
        length = int(input("Enter the desired length of the password: "))

        # Prompt user for complexity options
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        # Prompt user for number of passwords to generate
        num_passwords = int(input("How many passwords do you want to generate?: "))

        # Generate passwords
        passwords = [generate_password(length, use_lowercase, use_uppercase, use_digits, use_special) for _ in range(num_passwords)]

        # Display generated passwords
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"Password {i}: {password}")

        # Save passwords to a file
        save_to_file(passwords)
    except ValueError:
        print("Please enter valid input.")

if __name__ == "__main__":
    main()
