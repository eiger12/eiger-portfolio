"""Cybersecurity Tips Assistant for beginner safety guidance."""

import random

TIPS = {
    "Passwords": [
        "Use a long password with letters, numbers, and symbols.",
        "Avoid repeating the same password on multiple sites.",
        "Use a password manager if you can.",
        "Never use '123456' or 'password' — they are easy to guess.",
    ],
    "Accounts": [
        "Turn on two-factor authentication when it is available.",
        "Don't share your private passwords with anyone.",
        "Use a unique email or username for important accounts.",
        "Log out of shared computers when you are done.",
    ],
    "Browsing": [
        "Only enter passwords on websites that use HTTPS.",
        "Don't click suspicious links from unknown messages.",
        "Update your browser and apps to fix security bugs.",
        "Use strong and unique passwords for your accounts.",
    ],
    "Devices": [
        "Install updates on your phone and computer regularly.",
        "Use a screen lock or password on devices you carry.",
        "Back up your important files so you do not lose them.",
        "Do not connect to unknown public Wi-Fi without protection.",
    ],
}


def choose_tip(category: str) -> str:
    """Return a random tip from the selected category."""
    return random.choice(TIPS[category])


def list_categories() -> list[str]:
    """Return the available tip categories."""
    return list(TIPS)


def main() -> None:
    print("Cybersecurity Tips Assistant")
    print("Choose a category to get a quick safety tip.")
    categories = list_categories()
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    selection = input("Enter a number (or press Enter for a random tip): ").strip()
    if not selection:
        category = random.choice(categories)
    else:
        try:
            index = int(selection) - 1
            category = categories[index]
        except (ValueError, IndexError):
            print("Invalid choice. Showing a random tip.")
            category = random.choice(categories)

    tip = choose_tip(category)
    print(f"\nCategory: {category}")
    print(f"Tip: {tip}")


if __name__ == "__main__":
    main()
