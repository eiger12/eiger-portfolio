"""Simple password strength checker for learning cybersecurity."""

import re

# List of common weak passwords to avoid
weak_passwords = [
    "password",
    "123456",
    "123456789",
    "qwerty",
    "abc123",
    "iloveyou",
    "admin",
    "letmein",
]


def is_strong(password: str) -> bool:
    """Return True if password meets strength rules."""
    if len(password) < 8:
        return False
    if password.lower() in weak_passwords:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+\-=[\]{};:'\\|,.<>/?]", password):
        return False
    return True


def main() -> None:
    password = input("Enter a password to check: ")
    if is_strong(password):
        print("This password looks strong.")
    else:
        print("This password is weak. Try adding uppercase, lowercase, numbers, and symbols.")


if __name__ == "__main__":
    main()
