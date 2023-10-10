import re


def is_special_character(char):
    # Define a set of allowed special characters
    allowed_special_characters = set("!@#$%^&*()_+{}[]:;<>,.?~\\/-")

    # Check if the character is in the set of allowed special characters
    return char in allowed_special_characters


# Example usage:
test_char = "@"
result = is_special_character(test_char)

print(result)

"""

def is_special_character(char):
    # Define a set of allowed special characters
    allowed_special_characters = set("!@#$%^&*()_+{}[]:;<>,.?~\\/-")

    # Check if the character is in the set of allowed special characters
    return char in allowed_special_characters


# Example usage:
test_char = "@"
if is_special_character(test_char):
    print(f"{test_char} is a special character.")
else:
    print(f"{test_char} is not a special character.")

"""


def is_special_character(char):
    # Define a regular expression pattern to match special characters
    pattern = re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]')

    # Use the pattern to search for the character in the allowed special characters
    return bool(pattern.search(char))


# Example usage:
test_char = "@"
result = is_special_character(test_char)

print(result)

"""

def is_special_character2(char):
    # Define a regular expression pattern to match special characters
    pattern = re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]')

    # Use the pattern to search for the character in the allowed special characters
    match = pattern.search(char)

    # Return True if the character is a special character, False otherwise
    return bool(match)


# Example usage:
test_char = "@"
if is_special_character(test_char):
    print(f"{test_char} is a special character.")
else:
    print(f"{test_char} is not a special character.")

"""
