# TODO: String Methods

# lower() : Converts a string to lowercase.
original_string = "Hello World"
lowercase_string = original_string.lower()
print(lowercase_string)  # Output: "hello world"

# upper() : Converts a string to uppercase.
original_string = "Hello World"
uppercase_string = original_string.upper()
print(uppercase_string)  # Output: "HELLO WORLD"

# capitalize() : Capitalizes the first letter of a string.
original_string = "hello world"
capitalized_string = original_string.capitalize()
print(capitalized_string)  # Output: "Hello world"

# title() : Capitalizes the first letter of each word in a string.
original_string = "hello world"
title_case_string = original_string.title()
print(title_case_string)  # Output: "Hello World"

# strip() : Removes leading and trailing white-spaces from a string.
original_string = "   Hello World   "
stripped_string = original_string.strip()
print(stripped_string)  # Output: "Hello World"

# index() : Returns the index of the first occurrence of a substring.
original_string = "Hello World"
index_of_lo = original_string.index("lo")
print(index_of_lo)  # Output: 3

# rindex() : Returns the highest index of a substring.
original_string = "Hello World"
rindex_of_lo = original_string.rindex("lo")
print(rindex_of_lo)  # Output: 3

# replace() : Replaces occurrences of a substring with another string.
original_string = "Hello World"
new_string = original_string.replace("World", "Universe")
print(new_string)  # Output: "Hello Universe"

# count() : Counts the occurrences of a substring in a string.
original_string = "hello world, hello universe"
count_occurrences = original_string.count("hello")
print(count_occurrences)  # Output: 2

# swapcase() : Swaps the case of each letter in a string.
original_string = "Hello World"
swapped_case_string = original_string.swapcase()
print(swapped_case_string)  # Output: "hELLO wORLD"

# startswith() : Checks if a string starts with a specified prefix.
original_string = "Hello World"
starts_with_hello = original_string.startswith("Hello")
print(starts_with_hello)  # Output: True

# endswith() : Checks if a string ends with a specified suffix.
original_string = "Hello World"
ends_with_world = original_string.endswith("World")
print(ends_with_world)  # Output: True

# islower() : Checks if all letters in a string are lowercase.
lowercase_string = "hello world"
is_lower = lowercase_string.islower()
print(is_lower)  # Output: True

# isupper() : Checks if all letters in a string are uppercase.
uppercase_string = "HELLO WORLD"
is_upper = uppercase_string.isupper()
print(is_upper)  # Output: True

# isdigit() : Checks if all characters in a string are digits.
numeric_string = "12345"
is_digit = numeric_string.isdigit()
print(is_digit)  # Output: True

# isalpha() : Checks if all characters in a string are alphabetic.
alpha_string = "abc"
is_alpha = alpha_string.isalpha()
print(is_alpha)  # Output: True

# istitle() : Checks if a string is title cased.
title_case_string = "Hello World"
is_title = title_case_string.istitle()
print(is_title)  # Output: True

# Todo String Intro
# • A string is an object that represents sequences of characters
# • A string object is immutable, Once it is created it can’t be altered
# • String objects are surrounded by either single quotes or double quotes

# Creating a string
my_string = "Hello, World!"

# Checking the type of the object
print(type(my_string))  # Output: <class 'str'>

# Strings are immutable
# Trying to change a character will result in an error
# my_string[0] = 'h'  # This line will raise a TypeError


# TODO String: Sequences of characters
# • Strings are ordered sequences of characters, and each character has two index numbers:
# * Forward Index: starts from 0 (first character) and increases by 1 for each next character to the right
# * Reverse Index: starts from -1 (last character) and decreases by 1 for each next character to the left

# Forward Index
first_char = my_string[0]  # H
second_char = my_string[1]  # e

# Reverse Index
last_char = my_string[-1]  # !
second_last_char = my_string[-2]  # d

# TODO String: Indexing
# • Indexing allows us to access individual characters of string by using brackets [ ]

# Accessing individual characters using indexing
print(my_string[7])  # Output: W

# TODO Slicing Strings: Start & End Indexes
# • Creates a range of characters (substring) by using the slice syntax [ start : end ]
# • We can specify the start index and end index (excluded), separated by a colon, to create the substring

# Creating a substring from index 7 to 12 (excluding 12)
substring = my_string[7:12]  # World

# TODO Slicing Strings: Slice From the Start
# • By not giving the start index, the slicing starts from first character [ : end ]

# Slicing starts from the beginning to index 5 (excluding 5)
substring_start = my_string[:5]  # Hello

# TODO Slicing Strings: Slice to the End
# • By not giving the end index, the slicing starts from the start index to the end of the string [ start : ]

# Slicing starts from index 7 to the end
substring_end = my_string[7:]  # World!

print('----------- Part -1 ---------------')

# Part 1
name = 'Python'
print(len(name))  # Output: 6
print(name[0])  # Output: P
print(name[len(name) - 1])  # Output: n
print(name[-1])  # Output: n
print(name[-2])  # Output: o

print('----------- Part - 2 ---------------')

# Part 2
s = 'Java Programming Language'
s2 = s[5:16]
print(s2)  # Output: Programming

s3 = s[:4]
print(s3)  # Output: Java

s4 = s[::-1]  # reverses the string after slicing
print(s4)  # Output: egaugnaL gnimmargorP avaJ

print('----------- Part - 3 ---------------')

# Part 3
s = 'Python Programming'
s5 = reversed(s)
print(s5)  # <reversed object at .........> (Note: a reversed object won't be directly printed)
print(type(s5))  # Output: <class 'reversed'>

s5 = str(reversed(s))
print(type(s5))  # Output: <class 'str'>
reversed(s5)  # This line does not affect the output

print(s5)  # Output: <reversed object at ...> (Note: a reversed object won't be directly printed)

s55 = ''.join(reversed(s))
print(s55)  # Output: gnimmargorP nohtyP

s5 = s[::-1]
print(s5)  # Output: gnimmargorP nohtyP

s5 = 'python Programming'
s6 = s5[7:]  # by default, it slices the string from index 7 to the last character
print(s6)  # Output: Programming

print('----------- Part - 4 ---------------')

# Part 4
s7 = 'CYDEO SCHOOL'
# str(reversed(s7))
# The above line is commented out, so it won't produce any output

print('----------- Part - 5 ---------------')

# Part 5

# print( help(str))
# The above line is commented out, so it won't produce any output

print('----------- Part - 6 ---------------')

# Part 6
s = 'python programming language'
s = s.capitalize()  # Capitalizes the first character of the string
print('capitalize() : ' + s)  # Output: Capitalizes the first character: Python programming language

s = s.title()  # Capitalizes the first character of each word in the string.
print('title() : ' + s)  # Output: Capitalizes the first character of each word: Python Programming Language

s1 = "            Python           "
s1 = s1.strip()
print('strip() : ' + s1)  # Output: strip() : "Python"

s2 = "            Programming           "
s2 = s2.lstrip()
print('lstrip() : ' + s2)  # Output: lstrip() : "Programming           "

s3 = "            Language           "
s3 = s3.rstrip()
print('rstrip() : ' + s3)  # Output: rstrip() : "             Language"

print('----------- Part - 7 ---------------')

# Part 7
s = 'JAVA'
print(s.index('A'))  # Output: 1     # index() method in Java
print(s.rindex('A'))  # Output: 3     # lastIndex() method in Java

s = 'Java Java'
s = s.replace('Java', 'Python')
print(s)  # Output: Python Python

s = 'Java Java'
s = s.replace('Java', 'Python', 1)
print(s)  # Output: Python Java

s = 'C# C# Python'
s = s.replace(' C#', ' Java')
print(s)  # Output: C# Java Python

print('----------- Part - 8 ---------------')

# Part 8  count()
s = 'Java jAVA java JAVA Python Python'
count_java = s.lower().count('java')
count_python = s.count('Python')
print(count_java)  # Output: 4
print(count_python)  # Output: 2

print('----------- Part - 9 ---------------')

# Part 9  ==> ignore case
s1 = 'java'
s2 = 'JAVA'
print(s1.lower() == s2.lower())  # Output: True

print('----------- Part - 10 ---------------')

# Part 10
s = 'Java'
print(s[0].islower())  # Output: False
print(s[0].isupper())  # Output: True

print('----------- Part - 11 ---------------')

# Part 11
s = 'a'
print(s.isalpha())  # Output: True

print('----------- Part - 12 ---------------')

# Part 12
s = '1'
print(s.isdigit())  # Output: True

print('----------- Part - 13 ---------------')

# Part 13
s = 'Cydeo School'
print(s.istitle())  # Output: True

print('----------- Part - 14 ---------------')

# Part 14 reversed

# Example with a string
original_string = "Hello, Python!"
reversed_string = ''.join(reversed(original_string))

print("Original String:", original_string)  # Output: Original String: Hello, Python!
print("Reversed String:", reversed_string)  # Output: Reversed String: !nohtyP ,olleH

# Example with a list
original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list))

print("Original List:", original_list)  # Output: Original List: [1, 2, 3, 4, 5]
print("Reversed List:", reversed_list)  # Output: Reversed List: [5, 4, 3, 2, 1]

# Example with a range
original_range = range(1, 6)
reversed_range = list(reversed(original_range))

print("Original Range:", list(original_range))  # Output: Original Range: [1, 2, 3, 4, 5]
print("Reversed Range:", reversed_range)  # Output: Reversed Range: [5, 4, 3, 2, 1]

print('----------- Part - 15 ---------------')

# Part 15 # startswith(prefix): Checks if the string starts with a specified prefix.
original_string = "Hello, World!"
starts_with_hello = original_string.startswith("Hello")
print(starts_with_hello)  # Output: True

print('----------- Part - 16 ---------------')
# Part 16 # endswith(suffix): Checks if the string ends with a specified suffix.
original_string = "world"
ends_with_ld = original_string.endswith("ld")
print(ends_with_ld)  # Output: True
