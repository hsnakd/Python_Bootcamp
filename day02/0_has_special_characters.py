import re


def has_special_characters(input_string):
    # Define a regular expression pattern to match special characters
    pattern = re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]')

    # Use the pattern to search for special characters in the input string
    return bool(pattern.search(input_string))


# Example usage:
test_string = "Hello!123"
result = has_special_characters(test_string)

print(result)




"""

import re


def has_special_characters(input_string):
    # Define a regular expression pattern to match special characters
    pattern = re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]')

    # Use the pattern to search for special characters in the input string
    match = pattern.search(input_string)

    # Return True if special characters are found, False otherwise
    return bool(match)


# Example usage:
test_string = "Hello!123"
if has_special_characters(test_string):
    print("The string has special characters.")
else:
    print("The string does not have special characters.")


"""
