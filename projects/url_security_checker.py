"""A simple URL security checker for safe browsing habits."""

from urllib.parse import urlparse


def is_secure_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme.lower() == "https" and bool(parsed.netloc)


def explain_url(url: str) -> str:
    if is_secure_url(url):
        return "This link uses HTTPS, which is better for keeping your data safe."

    parsed = urlparse(url)
    if not parsed.scheme:
        return "This link has no URL scheme. Try adding 'https://' at the start."
    if parsed.scheme.lower() != "https":
        return f"This link uses {parsed.scheme.upper()}. HTTPS is safer because it encrypts the connection." 
    if not parsed.netloc:
        return "This looks like an incomplete URL. Check that the domain name is correct."
    return "This link may not be safe. Use HTTPS and make sure the website is real."


def main() -> None:
    print("URL Security Checker")
    print("Enter a website link to see if it is using HTTPS.")

    url = input("URL: ").strip()
    if not url:
        print("Please type a URL and try again.")
        return

    if not urlparse(url).scheme:
        url = "https://" + url

    print("\nResult:")
    print(explain_url(url))


if __name__ == "__main__":
    main()
