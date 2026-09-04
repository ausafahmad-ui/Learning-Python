"""
Palindrome checker - Check if strings or numbers are palindromes
"""


def is_palindrome_string(text):
    """
    Check if a string is a palindrome (ignoring spaces and case)
    
    Args:
        text (str): The string to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    # Compare with reversed string
    return cleaned == cleaned[::-1]


def is_palindrome_strict(text):
    """
    Check if a string is a palindrome (strict - considers spaces and case)
    
    Args:
        text (str): The string to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    return text == text[::-1]


def is_palindrome_alphanumeric(text):
    """
    Check if a string is a palindrome (only alphanumeric characters, ignore case)
    
    Args:
        text (str): The string to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def is_palindrome_number(num):
    """
    Check if a number is a palindrome
    
    Args:
        num (int): The number to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    str_num = str(abs(num))  # Convert to string, handle negative numbers
    return str_num == str_num[::-1]


def find_palindromes_in_list(words):
    """
    Find all palindromes in a list of words
    
    Args:
        words (list): List of strings to check
    
    Returns:
        list: Palindromes found in the list
    """
    return [word for word in words if is_palindrome_string(word)]


def longest_palindrome(text):
    """
    Find the longest palindromic substring
    
    Args:
        text (str): The string to search
    
    Returns:
        str: The longest palindromic substring
    """
    if not text:
        return ""
    
    text = text.lower()
    longest = ""
    
    for i in range(len(text)):
        # Check for odd-length palindromes
        left, right = i, i
        while left >= 0 and right < len(text) and text[left] == text[right]:
            palindrome = text[left:right + 1]
            if len(palindrome) > len(longest):
                longest = palindrome
            left -= 1
            right += 1
        
        # Check for even-length palindromes
        left, right = i, i + 1
        while left >= 0 and right < len(text) and text[left] == text[right]:
            palindrome = text[left:right + 1]
            if len(palindrome) > len(longest):
                longest = palindrome
            left -= 1
            right += 1
    
    return longest


# Test cases
if __name__ == "__main__":
    print("=== String Palindrome Tests ===")
    test_strings = ["racecar", "hello", "A man a plan a canal Panama", "madam"]
    for test in test_strings:
        result = is_palindrome_string(test)
        print(f"'{test}' -> {result}")
    
    print("\n=== Strict Palindrome Tests ===")
    test_strict = ["racecar", "Racecar", "A man a plan a canal Panama"]
    for test in test_strict:
        result = is_palindrome_strict(test)
        print(f"'{test}' -> {result}")
    
    print("\n=== Alphanumeric Palindrome Tests ===")
    test_alpha = ["race car", "A man, a plan, a canal: Panama", "Was it a car or a cat I saw?"]
    for test in test_alpha:
        result = is_palindrome_alphanumeric(test)
        print(f"'{test}' -> {result}")
    
    print("\n=== Number Palindrome Tests ===")
    test_numbers = [121, 123, 9009, -121, 1001]
    for num in test_numbers:
        result = is_palindrome_number(num)
        print(f"{num} -> {result}")
    
    print("\n=== Find Palindromes in List ===")
    words = ["racecar", "hello", "madam", "world", "level", "python"]
    palindromes = find_palindromes_in_list(words)
    print(f"Palindromes: {palindromes}")
    
    print("\n=== Longest Palindrome Test ===")
    text = "babad"
    result = longest_palindrome(text)
    print(f"Longest palindrome in '{text}' -> '{result}'")
