# Program to check whether a string or number is a palindrome
# A palindrome reads the same forwards and backwards (e.g. "madam", 121)


def is_palindrome(value):
    """Return True if the given value is a palindrome, else False."""
    text = str(value).lower()
    # Keep only alphanumeric characters so phrases like "Never odd or even" work
    cleaned = "".join(ch for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def main():
    user_input = input("Enter a word or number: ")

    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')


if __name__ == "__main__":
    main()
