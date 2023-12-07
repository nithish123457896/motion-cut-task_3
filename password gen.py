import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("----------------------------------")

    # Get user input
    length = int(input("Enter the desired length for your password: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate passwords
    passwords = [generate_password(length) for _ in range(num_passwords)]

    # Display generated passwords
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
