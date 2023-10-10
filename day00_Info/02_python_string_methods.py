# capitalize(): Returns a copy of the string with its first character capitalized.
string = "hello world"
capitalized = string.capitalize()
print(f"capitalize(): {capitalized}")  # Output: Capitalize(): Hello world

# casefold(): Returns a casefolded copy of the string, suitable for case-insensitive comparisons.
string = "HELLO World"
casefolded = string.casefold()
print(f"casefold(): {casefolded}")  # Output: casefold(): hello world

# center(width, fillchar): Returns a centered string of a specified width, padded with a specified character.
string = "hello"
centered = string.center(10, '*')
print(f"center(): {centered}")  # Output: center(): **hello***

# count(substring, start, end): Returns the number of occurrences of a substring in the given range.
string = "apple, banana, cherry, banana"
count = string.count("banana")
print(f"count(): {count}")  # Output: count(): 2

# encode(encoding='utf-8', errors='strict'): Returns an encoded version of the string.
string = "hello"
encoded = string.encode()
print(f"encode(): {encoded}")  # Output: encode(): b'hello'

# endswith(suffix, start, end): Returns True if the string ends with the specified suffix; False otherwise.
string = "Hello, World!"
ends_with = string.endswith("World!")
print(f"endswith(): {ends_with}")  # Output: endswith(): True

# expandtabs(tabsize=8): Returns a copy of the string with tab characters expanded using spaces.
string = "hello\tworld"
expanded = string.expandtabs(4)
print(f"expandtabs(): {expanded}")  # Output: expandtabs(): hello   world

# find(substring, start, end): Returns the lowest index of the substring in the string; -1 if not found.
string = "Hello, World!"
position = string.find("World")
print(f"find(): {position}")  # Output: find(): 7

# format(*args, **kwargs): Formats the string using positional and keyword arguments.
name = "John"
age = 30
formatted_string = "My name is {} and I am {} years old".format(name, age)
print(f"format(): {formatted_string}")  # Output: format(): My name is John and I am 30 years old

# format_map(mapping): Formats the string using a mapping of keys to values.
person = {'name': 'Alice', 'age': 25}
formatted_string = "My name is {name} and I am {age} years old".format_map(person)
print(f"format_map(): {formatted_string}")  # Output: format_map(): My name is Alice and I am 25 years old

# index(substring, start, end): Returns the lowest index of the substring in the string; raises ValueError if not found.
string = "Hello, World!"
position = string.index("World")
print(f"index(): {position}")  # Output: index(): 7

# isalnum(): Returns True if all characters in the string are alphanumeric; False otherwise.
alphanumeric = "abc123"
is_alnum = alphanumeric.isalnum()
print(f"isalnum(): {is_alnum}")  # Output: isalnum(): True

# isalpha(): Returns True if all characters in the string are alphabetic; False otherwise.
alphabetical = "abc"
is_alpha = alphabetical.isalpha()
print(f"isalpha(): {is_alpha}")  # Output: isalpha(): True

# isascii(): Returns True if all characters in the string are ASCII; False otherwise.
ascii_string = "Hello"
is_ascii = ascii_string.isascii()
print(f"isascii(): {is_ascii}")  # Output: isascii(): True

# isdecimal(): Returns True if all characters in the string are decimals; False otherwise.
decimal_string = "12345"
is_decimal = decimal_string.isdecimal()
print(f"isdecimal(): {is_decimal}")  # Output: isdecimal(): True

# isdigit(): Returns True if all characters in the string are digits; False otherwise.
digit_string = "123"
is_digit = digit_string.isdigit()
print(f"isdigit(): {is_digit}")  # Output: isdigit(): True

# isidentifier(): Returns True if the string is a valid identifier; False otherwise.
identifier = "variable_name"
is_identifier = identifier.isidentifier()
print(f"isidentifier(): {is_identifier}")  # Output: isidentifier(): True

# islower(): Returns True if all characters in the string are lowercase; False otherwise.
lower_case = "hello"
is_lower = lower_case.islower()
print(f"islower(): {is_lower}")  # Output: islower(): True

# isnumeric(): Returns True if all characters in the string are numeric; False otherwise.
numeric_string = "123"
is_numeric = numeric_string.isnumeric()
print(f"isnumeric(): {is_numeric}")  # Output: isnumeric(): True

# isprintable(): Returns True if all characters in the string are printable; False otherwise.
printable_string = "Hello, World!"
is_printable = printable_string.isprintable()
print(f"isprintable(): {is_printable}")  # Output: isprintable(): True

# isspace(): Returns True if all characters in the string are whitespaces; False otherwise.
space_string = "   "
is_space = space_string.isspace()
print(f"isspace(): {is_space}")  # Output: isspace(): True

# istitle(): Returns True if the string is a titlecased string; False otherwise.
title_string = "This Is A Title"
is_title = title_string.istitle()
print(f"istitle(): {is_title}")  # Output: istitle(): True

# isupper(): Returns True if all characters in the string are uppercase; False otherwise.
upper_case = "HELLO"
is_upper = upper_case.isupper()
print(f"isupper(): {is_upper}")  # Output: isupper(): True

# join(iterable): Concatenates the elements of an iterable with the string as a separator.
words = ["Hello", "World"]
joined_string = " ".join(words)
print(f"join(): {joined_string}")  # Output: join(): Hello World

# ljust(width, fillchar): Returns a left-justified version of the string, padded with a specified character.
string = "hello"
left_justified = string.ljust(10, '*')
print(f"ljust(): {left_justified}")  # Output: ljust(): hello*****

# lower(): Returns a copy of the string converted to lowercase.
string = "Hello, World!"
lowered = string.lower()
print(f"lower(): {lowered}")  # Output: lower(): hello, world!

# lstrip(chars): Returns a left-stripped version of the string, removing specified leading characters.
string = "   hello"
left_stripped = string.lstrip()
print(f"lstrip(): {left_stripped}")  # Output: lstrip(): hello

# maketrans(x[, y[, z]]): Returns a translation table for use in str.translate().
intab = "aeiou"
outtab = "12345"
trans = str.maketrans(intab, outtab)
string = "hello"
translated = string.translate(trans)
print(f"translate(): {translated}")  # Output: translate(): h2ll4

# partition(separator): Returns a tuple containing the string before the first occurrence of the separator,
# the separator itself, and the string after the separator.
string = "apple, banana, cherry"
partitioned = string.partition(", ")
print(f"partition(): {partitioned}")  # Output: partition(): ('apple', ', ', 'banana, cherry')

# replace(old, new, count): Returns a copy of the string with occurrences of a substring replaced by another substring.
string = "Hello, World!"
replaced = string.replace("World", "Universe")
print(f"replace(): {replaced}")  # Output: replace(): Hello, Universe!

# rfind(substring, start, end): Returns the highest index of the substring in the string; -1 if not found.
string = "apple, banana, cherry, banana"
position = string.rfind("banana")
print(f"rfind(): {position}")  # Output: rfind(): 18

# rindex(substring, start, end): Returns the highest index of the substring in the string; raises ValueError if not found.
string = "apple, banana, cherry, banana"
position = string.rindex("banana")
print(f"rindex(): {position}")  # Output: rindex(): 18

# rjust(width, fillchar): Returns a right-justified version of the string, padded with a specified character.
string = "hello"
right_justified = string.rjust(10, '*')
print(f"rjust(): {right_justified}")  # Output: rjust(): *****hello

# rpartition(separator): Returns a tuple containing the string before the last occurrence of the separator,
# the separator itself, and the string after the separator.
string = "apple, banana, cherry"
partitioned = string.rpartition(", ")
print(f"rpartition(): {partitioned}")  # Output: rpartition(): ('apple, banana', ', ', 'cherry')

# rsplit(separator, maxsplit): Returns a list of the words in the string, using the specified separator as the delimiter.
string = "apple, banana, cherry"
split_list = string.rsplit(", ")
print(f"rsplit(): {split_list}")  # Output: rsplit(): ['apple', 'banana', 'cherry']

# rstrip(chars): Returns a right-stripped version of the string, removing specified trailing characters.
string = "hello   "
right_stripped = string.rstrip()
print(f"rstrip(): {right_stripped}")  # Output: rstrip(): hello

# split(separator, maxsplit): Returns a list of the words in the string, using the specified separator as the delimiter.
string = "apple, banana, cherry"
split_list = string.split(", ")
print(f"split(): {split_list}")  # Output: split(): ['apple', 'banana', 'cherry']

# splitlines(keepends): Returns a list of the lines in the string, breaking at line boundaries.
multiline_string = "Hello\nWorld\nHow are you?"
split_lines = multiline_string.splitlines()
print(f"splitlines(): {split_lines}")  # Output: splitlines(): ['Hello', 'World', 'How are you?']

# startswith(prefix, start, end): Returns True if the string starts with the specified prefix; False otherwise.
string = "Hello, World!"
starts_with = string.startswith("Hello")
print(f"startswith(): {starts_with}")  # Output: startswith(): True

# strip(chars): Returns a stripped version of the string, removing specified leading and trailing characters.
string = "   hello   "
stripped = string.strip()
print(f"strip(): {stripped}")  # Output: strip(): hello

# swapcase(): Returns a copy of the string with uppercase characters converted to lowercase and vice versa.
string = "Hello, World!"
swapped_case = string.swapcase()
print(f"swapcase(): {swapped_case}")  # Output: swapcase(): hELLO, wORLD!

# title(): Returns a titlecased version of the string, where words start with an uppercase character.
string = "this is a title"
titled = string.title()
print(f"title(): {titled}")  # Output: title(): This Is A Title

# upper(): Returns a copy of the string converted to uppercase.
string = "hello, world!"
uppered = string.upper()
print(f"upper(): {uppered}")  # Output: upper(): HELLO, WORLD!

# zfill(width): Returns a copy of the string padded with zeros on the left to make a specified width.
number = "42"
zero_filled = number.zfill(5)
print(f"zfill(): {zero_filled}")  # Output: zfill(): 00042
