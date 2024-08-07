import random
import string

def generate_password(length):
    if length < 8:
        return "Length must be at least 8"

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_characters = letters + digits + symbols
    for _ in range(length - 3):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return ''.join(password)

def main():
    print(" ")
    print("Password Generator")
    print(" ")

    while True:
        length = input("Enter desired password length (or 'exit' to quit): ")

        if length.lower() == 'exit':
            print("Exiting.")
            break

        if not length.isdigit():
            print("Invalid input")
            continue

        length = int(length)
        if length < 8:
            print("Length must be at least 8")
            continue

        password = generate_password(length)
        print(" ")
        print("Generated Password: " + password)
        print(" ")

        another = input("Generate another password? (yes/no): ")
        if another.lower() != 'yes':
            print(" ")
            print("Thank you. Goodbye!")
            break

main()
