"""
# String Methods
    • Python has a built-in string class named str
    • The built-in string class (str) has a set of built-in methods that we can use
    • A string object is immutable, methods of string cannot change the original string, therefore, they return new values

"""



# capitalize(): Converts the first character of the string to uppercase.
original_string = "hello world"
capitalized_string = original_string.capitalize()
print(capitalized_string)  # Output: "Hello world"

# casefold(): Returns a casefolded version of the string, suitable for case-insensitive comparisons.
original_string = "HELLO"
casefolded_string = original_string.casefold()
print(casefolded_string)  # Output: "hello"

# center(width): Returns a centered string within a specified width.
original_string = "Python"
centered_string = original_string.center(10)
print(centered_string)  # Output: "  Python  "

# count(substring): Returns the number of occurrences of a substring in the string.
original_string = "banana"
count_occurrences = original_string.count("a")
print(count_occurrences)  # Output: 3

# encode(encoding): Returns an encoded version of the string using the specified encoding.
original_string = "hello"
encoded_string = original_string.encode("utf-8")
print(encoded_string)  # Output: b'hello'

# endswith(suffix): Checks if the string ends with a specified suffix.
original_string = "world"
ends_with_ld = original_string.endswith("ld")
print(ends_with_ld)  # Output: True

# expandtabs(tabsize): Expands tabs in the string to a specified number of spaces.
original_string = "tab\texample"
expanded_string = original_string.expandtabs(4)
print(expanded_string)  # Output: "tab example"

# find(substring): Returns the lowest index of the substring in the string, or -1 if not found.
original_string = "hello"
index_of_l = original_string.find("l")
print(index_of_l)  # Output: 2

# format(*args, **kwargs): Formats the string using the supplied arguments and keyword arguments.
formatted_string = "{} {}".format("Hello", "world")
print(formatted_string)  # Output: "Hello world"

# format_map(mapping): Formats the string using a mapping of keys to values.
formatted_string = "{name} is {age} years old".format_map({"name": "Alice", "age": 30})
print(formatted_string)  # Output: "Alice is 30 years old"

# index(substring): Returns the lowest index of the substring in the string, or raises an error if not found.
original_string = "hello"
index_of_e = original_string.index("e")
print(index_of_e)  # Output: 1

# isalnum(): Checks if all characters in the string are alphanumeric.
alphanumeric_string = "abc123"
is_alnum = alphanumeric_string.isalnum()
print(is_alnum)  # Output: True

# isalpha(): Checks if all characters in the string are alphabetic.
alpha_string = "abc"
is_alpha = alpha_string.isalpha()
print(is_alpha)  # Output: True

# isascii(): Checks if all characters in the string are ASCII.
ascii_string = "hello"
is_ascii = ascii_string.isascii()
print(is_ascii)  # Output: True

# isdecimal(): Checks if all characters in the string are decimal.
decimal_string = "123"
is_decimal = decimal_string.isdecimal()
print(is_decimal)  # Output: True

# isdigit(): Checks if all characters in the string are digits.
numeric_string = "123"
is_digit = numeric_string.isdigit()
print(is_digit)  # Output: True

# isidentifier(): Checks if the string is a valid identifier.
identifier_string = "variable_name"
is_identifier = identifier_string.isidentifier()
print(is_identifier)  # Output: True

# islower(): Checks if all characters in the string are lowercase.
lowercase_string = "hello"
is_lower = lowercase_string.islower()
print(is_lower)  # Output: True

# isnumeric(): Checks if all characters in the string are numeric.
numeric_string = "123"
is_numeric = numeric_string.isnumeric()
print(is_numeric)  # Output: True

# isprintable(): Checks if all characters in the string are printable.
printable_string = "Hello\nWorld"
is_printable = printable_string.isprintable()
print(is_printable)  # Output: False

# isspace(): Checks if all characters in the string are whitespaces.
whitespace_string = "   "
is_space = whitespace_string.isspace()
print(is_space)  # Output: True

# istitle(): Checks if the string is in title case.
title_string = "Title Case"
is_title = title_string.istitle()
print(is_title)  # Output: True

# isupper(): Checks if all characters in the string are uppercase.
uppercase_string = "HELLO"
is_upper = uppercase_string.isupper()
print(is_upper)  # Output: True

# join(iterable): Joins the elements of an iterable (e.g., a list) with the string as a separator.
words = ["apple", "orange", "banana"]
joined_string = "-".join(words)
print(joined_string)  # Output: "apple-orange-banana"

# ljust(width): Left-aligns the string within a specified width.
original_string = "hello"
left_aligned_string = original_string.ljust(10)
print(left_aligned_string)  # Output: "hello     "

# lower(): Converts all characters in the string to lowercase.
original_string = "Hello"
lowercase_string = original_string.lower()
print(lowercase_string)  # Output: "hello"

# lstrip(): Removes leading whitespaces from the string.
original_string = "   hello"
left_stripped_string = original_string.lstrip()
print(left_stripped_string)  # Output: "hello"

# maketrans(x[, y[, z]]): Returns a translation table for use in translate() method.
translation_table = str.maketrans("aeiou", "12345")
original_string = "hello"
translated_string = original_string.translate(translation_table)
print(translated_string)  # Output: "h2ll4"

# partition(separator): Splits the string at the first occurrence of the separator and returns a tuple.
original_string = "apple,orange,banana"
partitioned_tuple = original_string.partition(",")
print(partitioned_tuple)  # Output: ('apple', ',', 'orange,banana')

# replace(old, new): Replaces occurrences of a specified substring with another substring.
original_string = "Hello, World!"
new_string = original_string.replace("Hello", "Hi")
print(new_string)  # Output: "Hi, World!"

# rfind(substring): Returns the highest index of the substring in the string, or -1 if not found.
original_string = "hello"
rindex_of_l = original_string.rfind("l")
print(rindex_of_l)  # Output: 3

# rindex(substring): Returns the highest index of the substring in the string, or raises an error if not found.
original_string = "hello"
rindex_of_e = original_string.rindex("e")
print(rindex_of_e)  # Output: 1

# rjust(width): Right-aligns the string within a specified width.
original_string = "hello"
right_aligned_string = original_string.rjust(10)
print(right_aligned_string)  # Output: "     hello"

# rpartition(separator): Splits the string at the last occurrence of the separator and returns a tuple.
original_string = "apple,orange,banana"
rpartitioned_tuple = original_string.rpartition(",")
print(rpartitioned_tuple)  # Output: ('apple,orange', ',', 'banana')

# rsplit([separator[, maxsplit]]): Splits the string from the right at the specified separator.
original_string = "apple orange banana"
rsplit_list = original_string.rsplit(" ", 1)
print(rsplit_list)  # Output: ['apple orange', 'banana']

# rstrip(): Removes trailing whitespaces from the string.
original_string = "hello   "
right_stripped_string = original_string.rstrip()
print(right_stripped_string)  # Output: "hello"

# split([separator[, maxsplit]]): Splits the string at the specified separator.
original_string = "apple,orange,banana"
split_list = original_string.split(",")
print(split_list)  # Output: ['apple', 'orange', 'banana']

# splitlines([keepends]): Splits the string at line breaks and returns a list of lines.
original_string = "Hello\nWorld"
split_lines_list = original_string.splitlines()
print(split_lines_list)  # Output: ['Hello', 'World']

# startswith(prefix): Checks if the string starts with a specified prefix.
original_string = "Hello, World!"
starts_with_hello = original_string.startswith("Hello")
print(starts_with_hello)  # Output: True

# strip(): Removes leading and trailing whitespaces from the string.
original_string = "   hello   "
stripped_string = original_string.strip()
print(stripped_string)  # Output: "hello"

# swapcase(): Swaps the case of all characters in the string.
original_string = "Hello, World!"
swapped_case_string = original_string.swapcase()
print(swapped_case_string)  # Output: "hELLO, wORLD!"

# title(): Converts the first character of each word to uppercase.
original_string = "hello world"
title_case_string = original_string.title()
print(title_case_string)  # Output: "Hello World"

# translate(table): Applies a translation table to the string.
translation_table = str.maketrans("aeiou", "12345")
original_string = "hello"
translated_string = original_string.translate(translation_table)
print(translated_string)  # Output: "h2ll4"

# upper(): Converts all characters in the string to uppercase.
original_string = "hello"
uppercase_string = original_string.upper()
print(uppercase_string)  # Output: "HELLO"

# zfill(width): Pads the string with zeros on the left to a specified width.
original_string = "42"
zfilled_string = original_string.zfill(5)
print(zfilled_string)  # Output: "00042"
