"""Beginner CTF toolkit for Windows-friendly security tasks."""

import base64
import hashlib
import string
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
        return "Invalid base64 input."


def hex_encode(text: str) -> str:
    return to_bytes(text).hex()


def hex_decode(text: str) -> str:
    try:
        return from_bytes(bytes.fromhex(text))
    except Exception:
        return "Invalid hex input."


def rot13(text: str) -> str:
    return codecs_codec(text, 13)


def caesar_shift(text: str, shift: int) -> str:
    return codecs_codec(text, shift)


def codecs_codec(text: str, shift: int) -> str:
    output = []
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result = chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            output.append(result)
        else:
            output.append(char)
    return ''.join(output)


def xor_string(text: str, key: str) -> str:
    key_bytes = to_bytes(key)
    if not key_bytes:
        return "Key must not be empty."
    result = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(to_bytes(text))])
    return result.hex()


def hash_text(text: str, algorithm: str) -> str:
    try:
        hasher = hashlib.new(algorithm)
        hasher.update(to_bytes(text))
        return hasher.hexdigest()
    except ValueError:
        return "Unsupported hash algorithm."


def url_encode(text: str) -> str:
    return urllib.parse.quote(text)


def url_decode(text: str) -> str:
    return urllib.parse.unquote(text)


def print_menu() -> None:
    print("CTF Toolkit")
    print("Choose a tool:")
    print("1. Base64 encode")
    print("2. Base64 decode")
    print("3. Hex encode")
    print("4. Hex decode")
    print("5. ROT13")
    print("6. Caesar shift")
    print("7. XOR encode")
    print("8. MD5 hash")
    print("9. SHA1 hash")
    print("10. SHA256 hash")
    print("11. URL encode")
    print("12. URL decode")


def main() -> None:
    print_menu()
    choice = input("Select a number: ").strip()
    text = input("Enter text: ").strip()

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
        shift = input("Shift amount (0-25): ").strip()
        try:
            amount = int(shift)
        except ValueError:
            print("Invalid number.")
            return
        print(caesar_shift(text, amount))
    elif choice == "7":
        key = input("Enter XOR key: ").strip()
        print(xor_string(text, key))
    elif choice == "8":
        print(hash_text(text, "md5"))
    elif choice == "9":
        print(hash_text(text, "sha1"))
    elif choice == "10":
        print(hash_text(text, "sha256"))
    elif choice == "11":
        print(url_encode(text))
    elif choice == "12":
        print(url_decode(text))
    else:
        print("Unknown option.")


if __name__ == "__main__":
    main()
