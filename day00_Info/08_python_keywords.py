# Creating a sample list for demonstration
sample_list = [1, 2, 3, 4, 5]

# and - A logical operator
if 3 in sample_list and 4 in sample_list:
    print("Both 3 and 4 are present in the list.")
    # Output:
    # Both 3 and 4 are present in the list.

# as - To create an alias
import math as m
print(f"The square root of 16 is {m.sqrt(16)}.")
# Output:
# The square root of 16 is 4.0.

# assert - For debugging
x = 10
assert x > 5, "x should be greater than 5"

# break - To break out of a loop
for num in sample_list:
    if num == 4:
        break
    print(num)
# Output:
# 1
# 2
# 3

# class - To define a class
class ExampleClass:
    def __init__(self, name):
        self.name = name

# continue - To continue to the next iteration of a loop
for num in sample_list:
    if num == 3:
        continue
    print(num)
# Output:
# 1
# 2
# 4
# 5

# def - To define a function
def greet(name):
    print(f"Hello, {name}!")

# del - To delete an object
sample_dict = {'a': 1, 'b': 2}
del sample_dict['a']
print(sample_dict)
# Output:
# {'b': 2}

# elif - Used in conditional statements, same as else if
value = 15
if value > 10:
    print("Value is greater than 10.")
elif value < 10:
    print("Value is less than 10.")
else:
    print("Value is 10.")
# Output:
# Value is greater than 10.

# else - Used in conditional statements
value = 5
if value > 10:
    print("Value is greater than 10.")
else:
    print("Value is less than or equal to 10.")
# Output:
# Value is less than or equal to 10.

# except - Used with exceptions, what to do when an exception occurs
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
# Output:
# Cannot divide by zero.

# False - Boolean value, result of comparison operations
print(2 > 3)  # Output: False

# finally - Used with exceptions, a block of code that will be executed no matter if there is an exception or not
try:
    print("Try block.")
except:
    print("Except block.")
finally:
    print("Finally block.")
# Output:
# Try block.
# Finally block.

# for - To create a for loop
for num in sample_list:
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5

# from - To import specific parts of a module
from math import sqrt
print(f"The square root of 25 is {sqrt(25)}.")
# Output:
# The square root of 25 is 5.0.

# global - To declare a global variable
global_var = 20
def print_global_var():
    print(global_var)
print_global_var()
# Output:
# 20

# if - To make a conditional statement
value = 8
if value > 5:
    print("Value is greater than 5.")
# Output:
# Value is greater than 5.

# import - To import a module
import random
print(f"Random number: {random.randint(1, 100)}")

# in - To check if a value is present in a list, tuple, etc.
if 2 in sample_list:
    print("2 is present in the list.")
# Output:
# 2 is present in the list.

# is - To test if two variables are equal
a = [1, 2, 3]
b = a
print(a is b)  # Output: True

# lambda - To create an anonymous function
multiply = lambda x, y: x * y
print(f"Result of multiplication: {multiply(5, 3)}")
# Output:
# Result of multiplication: 15

# None - Represents a null value
empty_variable = None
if empty_variable is None:
    print("Variable is None.")
# Output:
# Variable is None.

# nonlocal - To declare a non-local variable
def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x += 5
        print(x)
    inner_function()
outer_function()
# Output:
# 15

# not - A logical operator
value = True
if not value:
    print("Value is False.")
# Output: (no output as value is True)

# or - A logical operator
if 2 in sample_list or 6 in sample_list:
    print("Either 2 or 6 is present in the list.")
# Output: (no output as both conditions are not met)

# pass - A null statement, a statement that will do nothing
for num in sample_list:
    pass

# raise - To raise an exception
try:
    raise ValueError("This is a custom error.")
except ValueError as e:
    print(f"Caught an exception: {e}")
# Output:
# Caught an exception: This is a custom error.

# return - To exit a function and return a value
def add_numbers(x, y):
    return x + y
result = add_numbers(3, 4)
print(f"Result of addition: {result}")
# Output:
# Result of addition: 7

# True - Boolean value, result of comparison operations
print(2 < 3)  # Output: True

# try - To make a try...except statement
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
# Output:
# Cannot divide by zero.

# while - To create a while loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# with - Used to simplify exception handling
with open('example.txt', 'r') as file:
    file_content = file.read()
    print(f"File Content:\n{file_content}")

# yield - To end a function, returns a generator
def generate_numbers():
    for i in range(5):
        yield i
gen = generate_numbers()
for num in gen:
    print(num)
# Output:
# 0
# 1
# 2
# 3
# 4
