def has_digit(input_string):
    return any(char.isdigit() for char in input_string)

# Example usage:
test_string = "Hello123"
result = has_digit(test_string)
print(result)  # Output: True




"""

def has_digit(input_string):
    return any(char.isdigit() for char in input_string)

# Example usage:
test_string = "Hello123"
if has_digit(test_string):
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")


"""
