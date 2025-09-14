import string
import secrets  # more secure than random

def password_generator():
    try:
        length = int(input("Enter your password length: "))
        if length <= 0:
            print("❌ Password length must be greater than 0.")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a number for length.")
        return

    # Ask for character set preferences
    lowercase = input("Include lowercase letters (y/n)? : ").strip().lower().startswith("y")
    uppercase = input("Include uppercase letters (y/n)? : ").strip().lower().startswith("y")
    digits = input("Include digits (y/n)? : ").strip().lower().startswith("y")
    special_character = input("Include special characters (y/n)? : ").strip().lower().startswith("y")

    # Build pools
    char_sets = []
    if lowercase:
        char_sets.append(string.ascii_lowercase)
    if uppercase:
        char_sets.append(string.ascii_uppercase)
    if digits:
        char_sets.append(string.digits)
    if special_character:
        char_sets.append(string.punctuation)

    if not char_sets:
        print("⚠ You must select at least one character type!")
        return

    # Ensure password has at least one character from each selected set
    password = [secrets.choice(charset) for charset in char_sets]

    # Fill the remaining length with random characters from all pools combined
    all_chars = ''.join(char_sets)
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]

    # Shuffle password to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)

    print("\n✅ Generated password:", ''.join(password))


if __name__ == "__main__":
    password_generator()
