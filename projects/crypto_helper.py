"""Beginner cryptography helper for Windows-friendly CTF-style tasks."""

import base64
import hashlib
import urllib.parse


def to_bytes(text: str) -> bytes:
    return text.encode("utf-8")


def from_bytes(data: bytes) -> str:
    return data.decode("utf-8", errors="replace")


def base64_encode(text: str) -> str:
    return base64.b64encode(to_bytes(text)).decode("utf-8")


def base64_decode(text: str) -> str:
    try:
        return from_bytes(base64.b64decode(text))
    except Exception:
        return "Invalid Base64 input."


def hex_encode(text: str) -> str:
    return to_bytes(text).hex()


def hex_decode(text: str) -> str:
    try:
        return from_bytes(bytes.fromhex(text))
    except ValueError:
        return "Invalid hex input."


def rot13(text: str) -> str:
    return text.translate(str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
    ))


def caesar_shift(text: str, shift: int) -> str:
    def shift_char(char: str) -> str:
        if char.isalpha():
            base = "A" if char.isupper() else "a"
            return chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        return char

    return "".join(shift_char(c) for c in text)


def vigenere_encode(text: str, key: str) -> str:
    if not key:
        return "Key is required."

    result = []
    key_index = 0
    key = key.upper()

    for char in text:
        if char.isalpha():
            base = "A" if char.isupper() else "a"
            shift = ord(key[key_index % len(key)]) - ord("A")
            result.append(chr((ord(char) - ord(base) + shift) % 26 + ord(base)))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def vigenere_decode(text: str, key: str) -> str:
    if not key:
        return "Key is required."

    result = []
    key_index = 0
    key = key.upper()

    for char in text:
        if char.isalpha():
            base = "A" if char.isupper() else "a"
            shift = ord(key[key_index % len(key)]) - ord("A")
            result.append(chr((ord(char) - ord(base) - shift) % 26 + ord(base)))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def xor_encode(text: str, key: str) -> str:
    if not key:
        return "Key is required."

    key_bytes = to_bytes(key)
    encoded = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(to_bytes(text))])
    return encoded.hex()


def hash_value(text: str, algorithm: str) -> str:
    data = to_bytes(text)
    algorithm = algorithm.lower()
    if algorithm == "md5":
        return hashlib.md5(data).hexdigest()
    if algorithm == "sha1":
        return hashlib.sha1(data).hexdigest()
    if algorithm == "sha256":
        return hashlib.sha256(data).hexdigest()
    return "Unsupported algorithm."


def print_menu() -> None:
    print("Crypto Helper")
    print("1. Base64 encode")
    print("2. Base64 decode")
    print("3. Hex encode")
    print("4. Hex decode")
    print("5. ROT13")
    print("6. Caesar shift")
    print("7. Vigenere encode")
    print("8. Vigenere decode")
    print("9. XOR encode")
    print("10. Hash text")
    print("0. Exit")


def main() -> None:
    while True:
        print_menu()
        choice = input("Choose a number: ").strip()

        if choice == "0":
            print("Goodbye.")
            break

        if choice in {"1", "2", "3", "4", "5", "8", "9", "10"}:
            text = input("Enter text: ")

        if choice == "1":
            print(base64_encode(text))
        elif choice == "2":
            print(base64_decode(text))
        elif choice == "3":
            print(hex_encode(text))
        elif choice == "4":
            print(hex_decode(text))
        elif choice == "5":
            print(rot13(text))
        elif choice == "6":
            text = input("Enter text: ")
            shift = input("Shift amount: ").strip()
            try:
                print(caesar_shift(text, int(shift)))
            except ValueError:
                print("Invalid number.")
        elif choice == "7":
            text = input("Enter text: ")
            key = input("Enter key: ")
            print(vigenere_encode(text, key))
        elif choice == "8":
            key = input("Enter key: ")
            print(vigenere_decode(text, key))
        elif choice == "9":
            key = input("Enter XOR key: ")
            print(xor_encode(text, key))
        elif choice == "10":
            algo = input("Hash algorithm (md5/sha1/sha256): ").strip().lower()
            print(hash_value(text, algo))
        else:
            print("Invalid option.")

        input("Press Enter to continue...\n")


if __name__ == "__main__":
    main()
