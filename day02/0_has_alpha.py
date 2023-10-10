def has_alpha(input_string):
    return any(char.isalpha() for char in input_string)


# Example usage:
test_string = "Hello123"
result = has_alpha(test_string)
print(result)  # Output: True

"""

def has_alpha(input_string):
    return any(char.isalpha() for char in input_string)

# Example usage:
test_string = "Hello123"
if has_alpha(test_string):
    print("The string contains at least one alphabetic character.")
else:
    print("The string does not contain any alphabetic characters.")


"""
