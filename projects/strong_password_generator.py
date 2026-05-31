"""Create a strong password using secure random choices."""

import secrets
import string


def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Return a secure random password."""
    characters = list(string.ascii_lowercase)
    if use_upper:
        characters.extend(string.ascii_uppercase)
    if use_digits:
        characters.extend(string.digits)
    if use_symbols:
        characters.extend("!@#$%^&*()-_=+[]{};:,.<>?/")

    if not characters:
        raise ValueError("Password must include at least one character set.")

    return "".join(secrets.choice(characters) for _ in range(length))


def main() -> None:
    print("Strong Password Generator")
    print("Use this to create a strong password for accounts or tools.")

    try:
        length_str = input("Enter password length (12-32): ")
        length = int(length_str)
    except ValueError:
        print("Please enter a valid number.")
        return

    if length < 8 or length > 64:
        print("Choose a length between 8 and 64.")
        return

    password = generate_password(length=length)
    print("\nYour strong password:")
    print(password)


if __name__ == "__main__":
    main()
