import re


def is_all_special_characters(input_string):
    # Define a regular expression pattern to match special characters
    pattern = re.compile(r'^[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]+$')

    # Use the pattern to match the entire input string
    return bool(pattern.match(input_string))


# Example usage:
test_string = "!@#$%^"
result = is_all_special_characters(test_string)

print(result)

"""


import re


def is_all_special_characters(input_string):
    # Define a regular expression pattern to match special characters
    pattern = re.compile(r'^[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]+$')

    # Use the pattern to match the entire input string
    match = pattern.match(input_string)

    # Return True if the entire string consists of special characters, False otherwise
    return bool(match)


# Example usage:
test_string = "!@#$%^"
if is_all_special_characters(test_string):
    print("The string consists entirely of special characters.")
else:
    print("The string contains non-special characters.")



"""
