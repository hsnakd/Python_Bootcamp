# Python Basics and Concepts

# 1- Indentation
# Python uses indentation to define code blocks.
if 5 > 2:
    print("5 is greater than 2")  # Output: 5 is greater than 2

# 2- Comments
# This is a single-line comment

# 3- Multiline Comments
"""
This is a
multi-line comment
"""

# 4- Creating Variables
# You can create variables in Python without specifying their data types.
x = 5
y = "Hello"

# 5- Variable Names
# Variable names must start with a letter or underscore and can contain letters, numbers, and underscores.
my_variable = "Hello"

# 6- Assign Values to Multiple Variables
a, b, c = 1, 2, 3

# 7- Output Variables
# You can use the 'print' function to display variable values.
x = "awesome"
print("Python is " + x)  # Output: Python is awesome

# 8- String Concatenation
# You can concatenate strings using the '+' operator.
a = "Hello"
b = "World"
print(a + " " + b)  # Output: Hello World

# 9- Global Variables
# Variables defined outside of functions are global.
x = "global"


def my_function():
    print("This function is using a " + x)


my_function()  # Output: This function is using a global

# 10- Built-In Data Types
# Python has several built-in data types including int, float, str, list, tuple, set, and dict.

# 11- Getting Data Type
# You can use the 'type' function to determine the data type of a variable.
x = 5
print(type(x))  # Output: <class 'int'>

# 12- Setting Data Type
# You can explicitly set the data type of a variable using type constructors.
x = str(5)

# 13- Numbers
# Python supports both integers and floating-point numbers.
# Examples for int and float data types.

# 14- Type Conversion
# You can convert between data types using type constructors.
x = int("5")

# 15- Random Number
# You can generate random numbers using the 'random' module.
import random
print(random.randint(1, 10))  # Output: A random integer between 1 and 10

# 16- Specify a Variable Type
# You can specify the data type of a variable using type constructors.
x = str("Hello")

# 17- String Literals
# Strings can be defined using single, double, or triple quotes.
single_quote = 'single'
double_quote = "double"
triple_quote = '''triple'''

# 18- Assigning a String to a Variable
greeting = "Hello"

# 19- Multiline Strings
# Triple quotes are often used for multiline strings.
multiline_string = """This is
a multiline
string"""

# 20- Strings are Arrays
# You can access individual characters in a string using indexing.
s = "Python"
print(s[1])  # Output: y

# 21- Slicing a String
# You can extract substrings using slicing.
print(s[1:4])  # Output: yth

# 22- Negative Indexing on a String
# Negative indexing allows you to count from the end of the string.
print(s[-3:-1])  # Output: ho

# 23- String Length
# You can find the length of a string using the 'len' function.
print(len(s))  # Output: 6

# 24- Check In String
# You can check if a substring exists in a string using the 'in' keyword.
print("Py" in s)  # Output: True

# 25- Format String
# You can format strings using placeholders and the 'format' method.
name = "Alice"
print("Hello, {}".format(name))  # Output: Hello, Alice

# 26- Escape Characters
# Special characters can be escaped using the backslash '\'.
print("This is a line\nbreak")  # Output: This is a line\nbreak

# 27- Boolean Values
# Python has two boolean values: True and False.
is_true = True
is_false = False

# 28- Evaluate Booleans
x = 5
y = 10
print(x > y)  # Output: False

# 29- Return Boolean Value
# You can create functions that return boolean values.
def is_even(number):
    return number % 2 == 0


print(is_even(4))  # Output: True

# 30- Operators
# Python supports various operators including arithmetic, assignment, comparison, logical, identity, membership, and bitwise operators.
# Examples for +, -, *, /, %, //, **, =, ==, !=, >, <, >=, <=, and, or, not, is, in, &, |, ^, ~

# 31- Arithmetic Operators
a = 5
b = 2
print(a + b)  # Output: 7

# 32- Assignment Operators
x = 5
x += 3

# 33- Comparison Operators
print(5 == 5)  # Output: True

# 34- Logical Operators
print(True and False)  # Output: False

# 35- Identity Operators
print(x is y)  # Output: False

# 36- Membership Operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Output: True

# 37- Bitwise Operators
a = 5
b = 3
print(a & b)  # Output: 1

# 38- Lists
# Lists are ordered, mutable collections of items.
# Examples for [], append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 39- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 40- Change List Item
numbers[1] = 5

# 41- Loop Through List Items
# You can loop through list items using a for loop.
for num in numbers:
    print(num)

# 42- List Comprehension
# List comprehensions provide a concise way to create lists.
squares = [x ** 2 for x in numbers]

# 43- Check if List Item Exists
# You can check if an item exists in a list using the 'in' keyword.
print(2 in numbers)  # Output: True

# 44- List Length
# You can find the length of a list using the 'len' function.
print(len(numbers))  # Output: 3

# 45- Add List Items
# You can add items to the end of a list using the 'append' method.
numbers.append(4)

# 46- Remove List Items
# You can remove items from a list using the 'remove' method.
# numbers.remove(2)  # Uncomment to run, currently commented to avoid altering the list

# 47- Copy a List
# You can create a copy of a list using the 'copy' method.
numbers_copy = numbers.copy()

# 48- Join Two Lists
# You can concatenate two lists using the '+' operator.
combined = numbers + squares

# 49- Tuple
# Tuples are ordered, immutable collections of items.
# Examples for (), count(), index()

# 50- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 51- Change Tuple Item
# Tuples are immutable, so you can't change individual elements.

# 52- Loop List Items
# You can loop through tuple items using a for loop.
for coord in coordinates:
    print(coord)

# 53- Check if Tuple Item Exists
# You can check if an item exists in a tuple using the 'in' keyword.
print(3 in coordinates)  # Output: True

# 54- Tuple Length
# You can find the length of a tuple using the 'len' function.
print(len(coordinates))  # Output: 2

# 55- Tuple With One Item
# A tuple with a single item must include a trailing comma.
single_item_tuple = (5,)

# 56- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements.

# 57- Join Two Tuples
# You can concatenate two tuples using the '+' operator.
combined_tuple = coordinates + single_item_tuple

# 58- Set
# Sets are unordered, mutable collections of unique items.
# Examples for {}, add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 59- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 60- Add Set Items
# You can add items to a set using the 'add' method.
fruits_set.add("orange")

# 61- Loop Set Items
# You can loop through set items using a for loop.
for fruit in fruits_set:
    print(fruit)

# 62- Check if Set Item Exists
# You can check if an item exists in a set using the 'in' keyword.
print("pear" in fruits_set)  # Output: False

# 63- Set Length
# You can find the length of a set using the 'len' function.
print(len(fruits_set))  # Output: 4

# 64- Remove Set Items
# You can remove items from a set using the 'remove' method.
fruits_set.remove("banana")

# 65- Join Two Sets
# You can concatenate two sets using the 'union' method or the '|' operator.
combined_set = fruits_set.union({"grape", "kiwi"})

# 66- Dictionary
# Dictionaries are unordered, mutable collections of key-value pairs.
# Examples for {}, keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 67- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 68- Change Dictionary Item
person["age"] = 31

# 69- Loop Dictionary Items
# You can loop through dictionary items using a for loop.
for key, value in person.items():
    print(f"{key}: {value}")

# 70- Check if Dictionary Item Exists
# You can check if a key exists in a dictionary using the 'in' keyword.
print("name" in person)  # Output: True

# 71- Dictionary Length
# You can find the length of a dictionary using the 'len' function.
print(len(person))  # Output: 2

# 72- Add Dictionary Item
# You can add a new key-value pair to a dictionary.
person["city"] = "New York"

# 73- Remove Dictionary Items
# You can remove items from a dictionary using the 'pop' method.
person.pop("age")

# 74- Copy Dictionary
# You can create a copy of a dictionary using the 'copy' method.
person_copy = person.copy()

# 75- Nested Dictionaries
# Dictionaries can contain other dictionaries.
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 76- If Statement
# The 'if' statement is used for conditional execution.
x = 10
if x > 5:
    print("x is greater than 5")

# 77- If Indentation
# Code blocks in Python are defined by indentation.
if x > 5:
    print("x is greater than 5")

# 78- Elif
# The 'elif' statement is used for additional conditions.
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 79- Else
# The 'else' statement is executed if none of the previous conditions are met.
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 80- Shorthand If
# Shorthand 'if' can be used for one-line conditionals.
print("x is greater than y") if x > y else print("x is not greater than y")

# 81- Shorthand If Else
# Shorthand 'if-else' can be used for one-line conditionals with a result.
result = "Even" if x % 2 == 0 else "Odd"

# 82- If AND
# The 'and' keyword is used for combining multiple conditions.
if x > 5 and y > 10:
    print("Both conditions are true")

# 83- If OR
# The 'or' keyword is used for combining multiple conditions.
if x > 5 or y > 10:
    print("At least one condition is true")

# 84- If NOT
# The 'not' keyword is used for negating a condition.
if not x > 5:
    print("x is not greater than 5")

# 85- Nested If
# 'if' statements can be nested to handle more complex conditions.
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 86- The pass Keyword in If
# The 'pass' keyword is a no-operation placeholder.
if x > y:
    pass
else:
    print("x is not greater than y")

# 87- While
# The 'while' loop is used for repeated execution as long as a condition is true.
i = 0
while i < 5:
    print(i)
    i += 1

# 88- While Break
# The 'break' statement is used to exit a loop prematurely.
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 89- While Continue
# The 'continue' statement is used to skip the rest of the code inside a loop.
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 90- While Else
# The 'else' block is executed when the 'while' loop condition becomes false.
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 91- For
# The 'for' loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 92- Loop Through a String
# Strings are iterable, and you can loop through them with a 'for' loop.
for char in "Python":
    print(char)

# 93- For Break
# The 'break' statement is used to exit a 'for' loop prematurely.
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 94- For Continue
# The 'continue' statement is used to skip the rest of the code inside a 'for' loop.
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 95- Looping Through a Range
# The 'range' function is used to generate a sequence of numbers that can be used in a 'for' loop.
for num in range(5):
    print(num)

# 96- For Else
# The 'else' block is executed when the 'for' loop has exhausted the items in the sequence.
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 97- Nested Loops
# 'for' loops can be nested inside each other.
for fruit in fruits:
    for char in fruit:
        print(char)

# 98- For pass
# The 'pass' keyword is a no-operation placeholder.
for fruit in fruits:
    pass

# 99- Function
# A function is a block of reusable code that performs a specific task.
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 100- Call a Function
# You can call a function multiple times with different arguments.
greet("Bob")


# 101- Function Arguments
# Functions can take parameters (or arguments) to accept input values.
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)

# 102- *args
# The '*args' syntax allows a function to accept any number of positional arguments.
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)

# 103- Keyword Arguments
# You can pass arguments by keyword, specifying the parameter names.
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)

# 104- **kwargs
# The '**kwargs' syntax allows a function to accept any number of keyword arguments.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)

# 105- Default Parameter Value
# Functions can have default parameter values.
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 106- Passing a List as an Argument
# You can pass a list (or any iterable) as an argument to a function.
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)

# 107- Function Return Value
# A function can return a value using the 'return' keyword.
def multiply(a, b):
    return a * b


result = multiply(4, 5)

# 108- The pass Statement in Functions
# The 'pass' keyword is a no-operation placeholder in a function.
def my_function():
    pass

# 109- Function Recursion
# A function can call itself, creating a recursive function.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 110- Lambda Function
# A lambda function is a small anonymous function defined with the 'lambda' keyword.
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 111- Why Use Lambda Functions
# Lambda functions are useful for short, simple operations.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 112- Array
# The 'array' module provides a way to create arrays of a specific data type.
# Examples for array.array()

# 113- What is an Array
# An array is a collection of elements, each identified by an index or a key.
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 114- Access Arrays
# You can access individual elements of an array using their index.
print(numbers_array[2])

# 115- Array Length
# The 'len' function returns the number of elements in an array.
print(len(numbers_array))

# 116- Looping Array Elements
# You can use a 'for' loop to iterate over the elements of an array.
for num in numbers_array:
    print(num)

# 117- Add Array Element
# You can add an element to the end of an array using the 'append' method.
numbers_array.append(6)

# 118- Remove Array Element
# You can remove a specific element from an array using the 'remove' method.
numbers_array.remove(3)

# 119- Array Methods
# The 'array' module provides various methods for working with arrays.
# Methods like extend(), fromlist(), tolist(), etc.

# 120- Class
# A class is a blueprint for creating objects with shared properties and behaviors.
# Examples for class definition, instantiation, and methods

# 121- Create Class
# You can define a class using the 'class' keyword.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 122- The Class init() Function
# The '__init__' method initializes the object with specified attributes.
# See the example above

# 123- Object Methods
# Objects created from a class can have methods (functions associated with them).
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 124- self
# The 'self' parameter refers to the instance of the class and is used to access its attributes.
# See the example above

# 125- Modify Object Properties
# You can modify the properties of an object by accessing them through the instance.
my_dog.age = 4

# 126- Delete Object Properties
# You can delete properties of an object using the 'del' keyword.
del my_dog.age

# 127- Delete Object
# To delete an entire object, use the 'del' keyword followed by the object name.
del my_dog

# 128- Class pass Statement
# The 'pass' statement is a placeholder for future code.
class MyClass:
    pass

# 129- Create Parent Class
# You can create a parent class with common attributes and methods.
class Animal:
    def __init__(self, name):
        self.name = name

# 130- Create Child Class
# Child classes inherit attributes and methods from their parent class.
class Dog(Animal):
    def bark(self):
        print("Woof!")

# 131- Create the init() Function
# The 'init' method in the child class should call the parent class's 'init' method using 'super()'.
# See the example above

# 132- super() Function
# The 'super()' function is used to call a method from the parent class.
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

# 133- Add Class Properties
# You can add properties specific to the child class.
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

# 134- Add Class Methods
# Child classes can have their own methods.
class Fish(Animal):
    def swim(self):
        print("Swimming")

# 135- Iterators
# Examples for iter() and next()
# 136- Iterator vs Iterable
# An iterator is an object that can be iterated (looped) over.
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 137- Loop Through an Iterator
# You can loop through an iterator using a 'for' loop.
for num in numbers_iter:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# 138- Create an Iterator
# To create a custom iterator, define '__iter__' and '__next__' methods in a class.
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration

my_iter = MyIterator()

# 139- StopIteration
# The 'StopIteration' exception is raised when there are no more items to be returned by an iterator.
# See the example above

# 140- Global Scope
# Variables defined outside of functions have global scope and can be accessed from anywhere.
global_var = "I am global"

# 141- Global Keyword
# The 'global' keyword is used to declare a global variable inside a function.
def my_function():
    global global_var
    print(global_var)

my_function()
# Output:
# I am global

# 142- Create a Module
# A module is a Python script that can be imported and used in other Python programs.
# See the example for creating a Python script and importing functions/classes from it

# 143- Variables in Modules
# Variables defined in a module can be accessed using dot notation (module.variable).
# See the example above

# 144- Renaming a Module
# You can rename a module using the 'as' keyword when importing it.
# See the example above

# 145- Built-in Modules
# Python provides many built-in modules for various tasks.
import math

# 146- Using the dir() Function
# The 'dir()' function lists all the names in a module.
print(dir(math))

# 147- Import From Module
# You can import specific functions or variables from a module.
from math import sqrt

# 148- Datetime Module
# The 'datetime' module provides functions and classes for working with dates and times.
import datetime

# 149- Date Output
# The 'date' class in the 'datetime' module represents dates in the format YYYY-MM-DD.
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 150- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 151- Parse JSON
# You can parse JSON data into a Python dictionary using 'json.loads()'.
import json
json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 152- Convert into JSON
# You can convert a Python dictionary into JSON data using 'json.dumps()'.
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 153- Format JSON
# You can format JSON data with indentation for readability using 'json.dumps()' with 'indent' parameter.
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 154- Sort JSON
# You can sort the keys of a JSON object when formatting it using 'sort_keys' parameter.
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 155- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 156- RegEx Functions
# The 're' module provides functions for working with regular expressions.
import re
text = "The quick brown fox"
result = re.search(r"fox", text)

# 157- Metacharacters in RegEx
# Regular expressions use metacharacters to specify patterns.
pattern = r"^The.*fox$"

# 158- RegEx Special Sequences
# Special sequences in regular expressions have predefined meanings.
pattern = r"\bword\b"

# 159- RegEx Sets
# Square brackets are used to specify a set of characters in a regular expression.
pattern = r"[aeiou]"

# 160- RegEx Match Object
# The 'search' function returns a match object if there is a match.
pattern = r"\b(\w+)\b"

# 161- Install PIP
# PIP (Package Installer for Python) is a tool to install Python packages.
# Instructions to install PIP

# 162- PIP Packages
# You can install external Python packages using the 'pip install' command.
# Examples for installing and using packages

# 163- PIP Remove Package
# To remove a package, use the 'pip uninstall' command.
# Instructions to remove a package

# 164- Error Handling
# Examples for try, except, else, finally, raise

# 165- Handle Many Exceptions
# You can handle multiple exceptions in a single 'except' block.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero

# 166- Try Else
# The 'else' block is executed if no exceptions occur in the 'try' block.
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred

# 167- Try Finally
# The 'finally' block is always executed, whether an exception occurs or not.
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute

# 168- raise
# The 'raise' keyword is used to raise an exception.
x = -1
if x < 0:
    raise ValueError("Value must be non-negative")

# 169- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 170- Access List Items
# You can access items in a list using index notation.
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 171- Change List Item
# You can change the value of a list item using index notation.
numbers[1] = 5

# 172- Loop Through List Items
# You can loop through the items in a list using a 'for' loop.
for num in numbers:
    print(num)

# 173- List Comprehension
# List comprehension is a concise way to create lists.
squares = [x ** 2 for x in numbers]

# 174- Check if List Item Exists
# You can check if an item exists in a list using the 'in' keyword.
print(2 in numbers)  # Output: False

# 175- List Length
# The 'len' function returns the number of items in a list.
print(len(numbers))  # Output: 3

# 176- Add List Items
# You can add items to the end of a list using the 'append' method.
numbers.append(4)

# 177- Remove List Items
# You can remove a specific item from a list using the 'remove' method.
numbers.remove(2)

# 178- Copy a List
# You can create a copy of a list using the 'copy' method.
numbers_copy = numbers.copy()

# 179- Join Two Lists
# You can concatenate two lists using the '+' operator.
combined = numbers + squares

# 180- Tuple Methods
# Examples for count(), index()

# 181- Access Tuple Items
# You can access items in a tuple using index notation.
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 182- Check if Tuple Item Exists
# You can check if an item exists in a tuple using the 'in' keyword.
print(3 in coordinates)  # Output: True

# 183- Tuple Length
# The 'len' function returns the number of items in a tuple.
print(len(coordinates))  # Output: 2

# 184- Tuple With One Item
# A tuple with a single item must include a trailing comma.
single_item_tuple = (5,)

# 185- Remove Tuple Items
# Tuples are immutable, so you cannot remove individual items.
# To remove a tuple, you can use the 'del' statement.

# 186- Join Two Tuples
# You can concatenate two tuples using the '+' operator.
combined_tuple = coordinates + single_item_tuple

# 187- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 188- Access Set Items
# You can check if an item exists in a set using the 'in' keyword.
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 189- Loop Set Items
# You can loop through the items in a set using a 'for' loop.
for fruit in fruits_set:
    print(fruit)

# 190- Check if Set Item Exists
# You can check if an item exists in a set using the 'in' keyword.
print("pear" in fruits_set)  # Output: False

# 191- Set Length
# The 'len' function returns the number of items in a set.
print(len(fruits_set))  # Output: 3

# 192- Remove Set Items
# You can remove a specific item from a set using the 'remove' method.
fruits_set.remove("banana")

# 193- Join Two Sets
# You can concatenate two sets using the 'union' method or the '|' operator.
combined_set = fruits_set.union({"grape", "kiwi"})

# 194- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 195- Access Dictionary Items
# You can access the value of a specific key in a dictionary.
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 196- Loop Dictionary Items
# You can loop through the items in a dictionary using a 'for' loop.
for key, value in person.items():
    print(f"{key}: {value}")

# 197- Check if Dictionary Item Exists
# You can check if a key exists in a dictionary using the 'in' keyword.
print("name" in person)  # Output: True

# 198- Dictionary Length
# The 'len' function returns the number of key-value pairs in a dictionary.
print(len(person))  # Output: 2

# 199- Add Dictionary Item
# You can add a new key-value pair to a dictionary.
person["city"] = "New York"

# 200- Remove Dictionary Items
# You can remove a specific key-value pair from a dictionary using the 'pop' method.
person.pop("age")

# 201- Copy Dictionary
# You can create a copy of a dictionary using the 'copy' method.
person_copy = person.copy()

# 202- Nested Dictionaries
# You can create nested dictionaries where values are dictionaries themselves.
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 203- If Statement
# The 'if' statement is used to execute a block of code if a condition is true.
x = 10
if x > 5:
    print("x is greater than 5")

# 204- If Indentation
# Proper indentation is crucial in Python. Indentation is used to define code blocks.
# See the example above for proper indentation within an 'if' block.

# 205- Elif
# The 'elif' statement is used for additional conditions when the 'if' condition is not met.
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 206- Else
# The 'else' statement is used to define code that executes when the 'if' condition is not met.
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 207- Shorthand If
# You can use a shorthand 'if' statement for concise single-line conditions.
print("x is greater than y") if x > y else print("x is not greater than y")

# 208- Shorthand If Else
# You can use a shorthand 'if-else' statement for concise single-line conditions with results.
result = "Even" if x % 2 == 0 else "Odd"

# 209- If AND
# The 'and' operator is used to combine multiple conditions, and all must be true for the block to execute.
if x > 5 and y > 10:
    print("Both conditions are true")

# 210- If OR
# The 'or' operator is used to combine multiple conditions, and at least one must be true for the block to execute.
if x > 5 or y > 10:
    print("At least one condition is true")

# 211- If NOT
# The 'not' operator is used to negate a condition.
if not x > 5:
    print("x is not greater than 5")

# 212- Nested If
# You can nest 'if' statements within other 'if' statements for complex conditions.
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 213- The pass Keyword in If
# The 'pass' keyword is a placeholder for future code and is used when you need an empty 'if' block.
if x > y:
    pass
else:
    print("x is not greater than y")

# 214- While
# The 'while' loop is used to repeatedly execute a block of code while a condition is true.
i = 0
while i < 5:
    print(i)
    i += 1

# 215- While Break
# The 'break' statement is used to exit a loop prematurely when a certain condition is met.
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 216- While Continue
# The 'continue' statement is used to skip the current iteration of a loop and continue to the next one.
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 217- While Else
# The 'else' block in a 'while' loop is executed when the loop condition becomes false.
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 218- For
# The 'for' loop is used to iterate over a sequence (list, tuple, string, etc.).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 219- Loop Through a String
# You can use a 'for' loop to iterate through the characters of a string.
for char in "Python":
    print(char)

# 220- For Break
# The 'break' statement can be used in a 'for' loop to exit it prematurely when a certain condition is met.
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 221- For Continue
# The 'continue' statement can be used in a 'for' loop to skip the current iteration and continue to the next one.
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 222- Looping Through a Range
# You can use the 'range' function to generate a sequence of numbers for looping.
for num in range(5):
    print(num)

# 223- For Else
# The 'else' block in a 'for' loop is executed when the loop completes without encountering a 'break'.
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 224- Nested Loops
# You can nest 'for' loops to iterate through multiple sequences.
for fruit in fruits:
    for char in fruit:
        print(char)

# 225- For pass
# The 'pass' statement is a placeholder for future code and can be used in a 'for' loop.
for fruit in fruits:
    pass

# 226- Function
# Functions are reusable blocks of code that can be called with specific arguments.
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

# 227- Call a Function
# You can call a function by using its name followed by parentheses.
greet("Bob")

# 228- Function Arguments
# Functions can accept arguments (parameters) that are passed when calling the function.
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)

# 229- *args
# The '*args' syntax allows a function to accept a variable number of positional arguments.
def add_all(*args):
    return sum(args)

result = add_all(1, 2, 3)

# 230- Keyword Arguments
# You can pass arguments to a function using keyword-argument pairs.
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet_person(name="Alice", age=25)

# 231- **kwargs
# The '**kwargs' syntax allows a function to accept a variable number of keyword arguments.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30)

# 232- Default Parameter Value
# Functions can have default parameter values, which are used when an argument is not provided.
def greet_default(name="User"):
    print(f"Hello, {name}!")

greet_default()

# 233- Passing a List as an Argument
# You can pass a list as an argument to a function.
numbers = [1, 2, 3]

def print_numbers(nums):
    for num in nums:
        print(num)

print_numbers(numbers)

# 234- Function Return Value
# Functions can return values using the 'return' statement.
def multiply(a, b):
    return a * b

result = multiply(4, 5)

# 235- The pass Statement in Functions
# The 'pass' statement can be used as a placeholder in function definitions.
def my_function():
    pass

# 236- Function Recursion
# Recursion is when a function calls itself. It's useful for solving problems that can be broken down into simpler subproblems.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)

# 237- Lambda Function
# A lambda function is a concise way to create small, anonymous functions.
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 238- Why Use Lambda Functions
# Lambda functions are handy for short, one-time operations.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 239- Array
# The 'array' module provides a way to work with arrays in Python.
# Examples for array.array()

# 240- What is an Array
# An array is a collection of items stored at contiguous memory locations.
import array
numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 241- Access Arrays
# You can access elements of an array using indexing.
print(numbers_array[2])

# 242- Array Length
# The 'len' function can be used to find the length of an array.
print(len(numbers_array))

# 243- Looping Array Elements
# You can use a 'for' loop to iterate over the elements of an array.
for num in numbers_array:
    print(num)

# 244- Add Array Element
# You can add elements to the end of an array using the 'append' method.
numbers_array.append(6)

# 245- Remove Array Element
# You can remove a specific element from an array using the 'remove' method.
numbers_array.remove(3)

# 246- Array Methods
# The 'array' module provides various methods for working with arrays.
# Examples include methods like extend(), fromlist(), tolist(), etc.

# 247- Class
# Classes are used to create objects, which bundle data and functionality.
# Examples for class definition, instantiation, and methods

# 248- Create Class
# A class is defined using the 'class' keyword, and it may contain attributes (variables) and methods (functions).
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 249- The Class init() Function
# The '__init__' method initializes the object when it is created.
# It is called automatically when an object is instantiated from the class.
# See the example above for the '__init__' method.

# 250- Object Methods
# Objects have methods, which are functions defined within the class.
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 251- self
# The 'self' parameter refers to the instance of the object and is used to access variables that belong to the class.
# See the example above for the use of 'self'.

# 252- Modify Object Properties
# You can modify the properties of an object by accessing them through the instance.
my_dog.age = 4

# 253- Delete Object Properties
# You can delete properties of an object using the 'del' keyword.
del my_dog.age

# 254- Delete Object
# You can delete an entire object using the 'del' keyword.
del my_dog

# 255- Class pass Statement
# The 'pass' statement can be used as a placeholder in class definitions.
class MyClass:
    pass

# 256- Create Parent Class
# Inheritance allows a new class to inherit attributes and methods from an existing class.
class Animal:
    def __init__(self, name):
        self.name = name

# 257- Create Child Class
# A child class is created by specifying the parent class in parentheses.
class Dog(Animal):
    def bark(self):
        print("Woof!")

# 258- Create the init() Function
# When a child class has an '__init__' method, it should call the '__init__' method of the parent class using 'super()'.
# See the example above for the use of 'super()'.

# 259- super() Function
# The 'super()' function is used to call a method from the parent class.
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

# 260- Add Class Properties
# A class can have attributes (properties) that define its characteristics.
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

# 261- Add Class Methods
# A class can have methods that define its behavior.
class Fish(Animal):
    def swim(self):
        print("Swimming")

# 262- Iterators
# Iterators are objects that can be iterated (looped) over.
# Examples for iter() and next()

# 263- Iterator vs Iterable
# An iterable is an object capable of returning an iterator.
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 264- Loop Through an Iterator
# You can use a 'for' loop to iterate through the elements of an iterator.
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 265- Create an Iterator
# To create an iterator, you need to implement the '__iter__' and '__next__' methods.
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration

my_iter = MyIterator()

# 266- StopIteration
# The 'StopIteration' exception is raised to signal the end of the iteration.
# See the example above for the use of 'StopIteration'.

# 267- Global Scope
# Variables defined outside any function or class have a global scope.
global_var = "I am global"

# 268- Global Keyword
# The 'global' keyword is used to indicate that a variable refers to the global scope within a function.
def my_function():
    global global_var
    print(global_var)

my_function()
# Output:
# I am global

# 269- Create a Module
# A module is a Python script that can be imported into other scripts.
# See the example for creating a Python script and importing functions/classes from it.

# 270- Variables in Modules
# Variables defined in a module can be accessed in other scripts that import the module.
# See the example above for using variables in modules.

# 271- Renaming a Module
# You can use the 'as' keyword to rename a module when importing it.
# See the example above for renaming a module.

# 272- Built-in Modules
# Python has many built-in modules that provide additional functionality.
import math

# 273- Using the dir() Function
# The 'dir()' function can be used to get a list of names defined in a module.
print(dir(math))

# 274- Import From Module
# You can import specific names from a module using the 'from...import' statement.
from math import sqrt

# 275- Datetime Module
# The 'datetime' module provides functions to work with dates and times.
import datetime

# 276- Date Output
# You can use the 'date.today()' method to get the current date.
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 277- JSON
# The 'json' module provides functions for working with JSON data.
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 278- Parse JSON
# The 'json.loads()' function is used to parse a JSON-formatted string into a Python object.
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 279- Convert into JSON
# The 'json.dumps()' function is used to convert a Python object into a JSON-formatted string.
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 280- Format JSON
# The 'indent' parameter of 'json.dumps()' can be used to specify the indentation level for the JSON output.
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 281- Sort JSON
# The 'sort_keys' parameter of 'json.dumps()' can be used to sort the keys of the JSON output.
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 282- RegEx Module
# The 're' module provides functions for working with regular expressions.
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 283- RegEx Functions
# The 're.search()' function is used to search for a pattern in a string.
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 284- Metacharacters in RegEx
# Metacharacters in regular expressions have special meanings.
pattern = r"^The.*fox$"

# 285- RegEx Special Sequences
# Special sequences in regular expressions have specific meanings.
pattern = r"\bword\b"

# 286- RegEx Sets
# Sets in regular expressions are used to match any one of the characters inside the brackets.
pattern = r"[aeiou]"

# 287- RegEx Match Object
# The result of 're.search()' is a match object that provides information about the match.
pattern = r"\b(\w+)\b"

# 288- Install PIP
# PIP is a package manager for Python. You can install it by following the instructions for your operating system.

# 289- PIP Packages
# You can use PIP to install external packages, expanding the capabilities of your Python environment.
# Examples for installing and using packages

# 290- PIP Remove Package
# You can use PIP to remove a package from your Python environment.
# Instructions to remove a package

# 291- Error Handling
# Error handling is essential to deal with exceptions and prevent program crashes.
# Examples for try, except, else, finally, raise

# 292- Handle Many Exceptions
# You can handle multiple exceptions by using multiple 'except' blocks.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero

# 293- Try Else
# The 'else' block in a 'try' statement is executed if no exceptions occur.
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred

# 294- Try Finally
# The 'finally' block in a 'try' statement is always executed, regardless of whether an exception occurs or not.
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute

# 295- raise
# The 'raise' statement is used to raise an exception manually.
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list

# 296- List Methods
# Lists are mutable sequences, and they have various methods for manipulation.
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 297- Access List Items
# You can access elements of a list using indexing.
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 298- Change List Item
# You can change the value of a specific element in a list by assigning a new value.
numbers[1] = 5

# 299- Loop Through List Items
# You can use a 'for' loop to iterate through the elements of a list.
for num in numbers:
    print(num)

# 300- List Comprehension
# List comprehension is a concise way to create lists.
squares = [x ** 2 for x in numbers]
# 301- Check if List Item Exists
# You can check if an item exists in a list using the 'in' keyword.
print(2 in numbers)  # Output: False

# 302- List Length
# Find the length of a list using the 'len()' function.
print(len(numbers))  # Output: 3

# 303- Add List Items
# Append an item to the end of a list using the 'append()' method.
numbers.append(4)

# 304- Remove List Items
# To remove an item from a list, use the 'remove()' method.
# numbers.remove(2)

# 305- Copy a List
# Create a copy of a list using the 'copy()' method.
numbers_copy = numbers.copy()

# 306- Join Two Lists
# Combine two lists using the '+' operator.
combined = numbers + squares

# 307- Tuple Methods
# Examples for count(), index()

# 308- Access Tuple Items
# Access elements in a tuple using indexing.
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 309- Check if Tuple Item Exists
# Use the 'in' keyword to check if an item exists in a tuple.
print(3 in coordinates)  # Output: True

# 310- Tuple Length
# Determine the length of a tuple using 'len()'.
print(len(coordinates))  # Output: 2

# 311- Tuple With One Item
# If a tuple has only one item, include a trailing comma.
single_item_tuple = (5,)

# 312- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements.

# 313- Join Two Tuples
# Concatenate two tuples using the '+' operator.
combined_tuple = coordinates + single_item_tuple

# 314- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 315- Access Set Items
# Use the 'in' keyword to check if an item exists in a set.
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 316- Loop Set Items
# Iterate through set elements using a 'for' loop.
for fruit in fruits_set:
    print(fruit)

# 317- Check if Set Item Exists
# Check if an item exists in a set using the 'in' keyword.
print("pear" in fruits_set)  # Output: False

# 318- Set Length
# Get the number of elements in a set using 'len()'.
print(len(fruits_set))  # Output: 4

# 319- Remove Set Items
# Remove an item from a set using the 'remove()' method.
fruits_set.remove("banana")

# 320- Join Two Sets
# Combine two sets using the 'union()' method.
combined_set = fruits_set.union({"grape", "kiwi"})

# 321- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 322- Access Dictionary Items
# Access values in a dictionary using keys.
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 323- Loop Dictionary Items
# Iterate through dictionary items using a 'for' loop.
for key, value in person.items():
    print(f"{key}: {value}")

# 324- Check if Dictionary Item Exists
# Check if a key exists in a dictionary using the 'in' keyword.
print("name" in person)  # Output: True

# 325- Dictionary Length
# Find the number of key-value pairs in a dictionary using 'len()'.
print(len(person))  # Output: 2

# 326- Add Dictionary Item
# Add a new key-value pair to a dictionary.
person["city"] = "New York"

# 327- Remove Dictionary Items
# Remove a key-value pair from a dictionary using 'pop()'.
person.pop("age")

# 328- Copy Dictionary
# Create a copy of a dictionary using the 'copy()' method.
person_copy = person.copy()

# 329- Nested Dictionaries
# Create dictionaries within a dictionary for nesting.
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 330- If Statement
# Use 'if' to conditionally execute code.
x = 10
if x > 5:
    print("x is greater than 5")

# 331- If Indentation
# Proper indentation is crucial for code blocks in Python.
if x > 5:
    print("x is greater than 5")

# 332- Elif
# Use 'elif' for additional conditions in an 'if' statement.
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 333- Else
# 'else' is executed when none of the preceding conditions are true.
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 334- Shorthand If
# A concise form of 'if' for one-line statements.
print("x is greater than y") if x > y else print("x is not greater than y")

# 335- Shorthand If Else
# Use a conditional expression for a concise 'if-else'.
result = "Even" if x % 2 == 0 else "Odd"

# 336- If AND
# 'and' combines conditions, and both must be true.
if x > 5 and y > 10:
    print("Both conditions are true")

# 337- If OR
# 'or' checks if at least one condition is true.
if x > 5 or y > 10:
    print("At least one condition is true")

# 338- If NOT
# 'not' negates the condition.
if not x > 5:
    print("x is not greater than 5")

# 339- Nested If
# Nest 'if' statements for complex conditions.
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 340- The pass Keyword in If
# 'pass' is a no-operation statement when a block is syntactically required.
if x > y:
    pass
else:
    print("x is not greater than y")

# 341- While
# 'while' executes a block of code while a condition is true.
i = 0
while i < 5:
    print(i)
    i += 1

# 342- While Break
# 'break' exits the 'while' loop prematurely.
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 343- While Continue
# 'continue' skips the rest of the loop and goes to the next iteration.
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 344- While Else
# 'else' is executed when the 'while' loop condition becomes false.
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 345- For
# 'for' iterates over a sequence (e.g., a list).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 346- Loop Through a String
# Iterate through characters in a string using 'for'.
for char in "Python":
    print(char)

# 347- For Break
# 'break' exits the 'for' loop prematurely.
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 348- For Continue
# 'continue' skips the rest of the loop and goes to the next iteration.
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 349- Looping Through a Range
# 'range()' generates a sequence of numbers for looping.
for num in range(5):
    print(num)

# 350- For Else
# 'else' is executed when the 'for' loop completes without 'break'.
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 351- Nested Loops
# Nest 'for' loops for multiple iterations.
for fruit in fruits:
    for char in fruit:
        print(char)

# 352- For pass
# 'pass' is a no-operation statement when a block is syntactically required.
for fruit in fruits:
    pass

# 353- Function
# Define and call functions for reusable code.
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

# 354- Call a Function
# Call a function with arguments.
greet("Bob")

# 355- Function Arguments
# Functions can accept parameters.
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)

# 356- *args
# Use '*args' to pass a variable number of arguments to a function.
def add_all(*args):
    return sum(args)

result = add_all(1, 2, 3)

# 357- Keyword Arguments
# Provide arguments by name in a function call.
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet_person(name="Alice", age=25)

# 358- **kwargs
# Use '**kwargs' to pass a variable number of keyword arguments.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30)

# 359- Default Parameter Value
# Assign default values to function parameters.
def greet_default(name="User"):
    print(f"Hello, {name}!")

greet_default()

# 360- Passing a List as an Argument
# Pass a list as an argument to a function.
numbers = [1, 2, 3]
def print_numbers(nums):
    for num in nums:
        print(num)

print_numbers(numbers)

# 361- Function Return Value
# Functions can return values.
def multiply(a, b):
    return a * b

result = multiply(4, 5)

# 362- The pass Statement in Functions
# 'pass' is a no-operation statement when a block is syntactically required.
def my_function():
    pass

# 363- Function Recursion
# A function can call itself (recursion).
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)

# 364- Lambda Function
# Define small anonymous functions using 'lambda'.
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 365- Why Use Lambda Functions
# Use 'lambda' with functions like 'map()' for conciseness.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 366- Array
# Examples for array.array()

# 367- What is an Array
# Import the 'array' module to work with arrays.
import array
numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 368- Access Arrays
# Access elements in an array using indexing.
print(numbers_array[2])

# 369- Array Length
# Determine the length of an array using 'len()'.
print(len(numbers_array))

# 370- Looping Array Elements
# Iterate through array elements using a 'for' loop.
for num in numbers_array:
    print(num)

# 371- Add Array Element
# Add an element to the end of an array using 'append()'.
numbers_array.append(6)

# 372- Remove Array Element
# Remove a specific element from an array using 'remove()'.
numbers_array.remove(3)

# 373- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 374- Class
# Examples for class definition, instantiation, and methods

# 375- Create Class
# Define a class to create objects with attributes and methods.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 376- The Class init() Function
# The '__init__' method initializes object properties.
# See the example above

# 377- Object Methods
# Objects can have methods (functions associated with them).
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 378- self
# 'self' represents the instance of the class.
# Refer to the example above

# 379- Modify Object Properties
# Modify object properties by reassigning values.
my_dog.age = 4

# 380- Delete Object Properties
# Use 'del' to delete object properties.
del my_dog.age

# 381- Delete Object
# Use 'del' to delete an entire object.
del my_dog

# 382- Class pass Statement
# 'pass' is a no-operation statement when a block is syntactically required.
class MyClass:
    pass

# 383- Create Parent Class
# Create a parent class with shared attributes and methods.
class Animal:
    def __init__(self, name):
        self.name = name

# 384- Create Child Class
# Create a child class that inherits from a parent class.
class Dog(Animal):
    def bark(self):
        print("Woof!")

# 385- Create the init() Function
# The '__init__' method initializes object properties.
# See the example above

# 386- super() Function
# Use 'super()' to call a method from the parent class.
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

# 387- Add Class Properties
# Add additional properties to a class.
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

# 388- Add Class Methods
# Add methods to a class for functionality.
class Fish(Animal):
    def swim(self):
        print("Swimming")

# 389- Iterators
# Examples for iter() and next()

# 390- Iterator vs Iterable
# An iterator is an object that can be iterated (looped) over.
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 391- Loop Through an Iterator
# Iterate through an iterator using a 'for' loop.
for num in numbers_iter:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# 392- Create an Iterator
# Create a custom iterator using '__iter__' and '__next__' methods.
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration

my_iter = MyIterator()

# 393- StopIteration
# 'StopIteration' signals the end of the iterator.
# See the example above

# 394- Global Scope
# Variables declared outside functions have global scope.
global_var = "I am global"

# 395- Global Keyword
# Use 'global' to indicate a variable is a global variable.
def my_function():
    global global_var
    print(global_var)

my_function()
# Output:
# I am global

# 396- Create a Module
# Organize code by creating a module (Python script).
# See the example for creating a Python script and importing functions/classes from it

# 397- Variables in Modules
# Variables defined in a module are accessible when the module is imported.
# See the example above

# 398- Renaming a Module
# Use 'as' to give a module a different alias when importing.
# See the example above

# 399- Built-in Modules
# Use built-in modules like 'math' for additional functionality.
import math

# 400- Using the dir() Function
# 'dir()' lists the names in a module.
print(dir(math))

# 401- Import From Module
# You can import specific functions or objects from a module using the 'from ... import ...' syntax.
from math import sqrt

# 402- Datetime Module
# You can use the 'datetime' module to work with date and time data.
import datetime

# 403- Date Output
# You can get the current date using 'datetime.date.today()' and print it in the format YYYY-MM-DD.
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 404- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 405- Parse JSON
# You can parse a JSON-formatted string into a Python dictionary using 'json.loads()'.
import json
json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 406- Convert into JSON
# You can convert a Python dictionary into a JSON-formatted string using 'json.dumps()'.
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 407- Format JSON
# You can format a JSON-formatted string with an indentation for readability using 'json.dumps()' with the 'indent' parameter.
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 408- Sort JSON
# You can sort the keys of a JSON-formatted string using 'json.dumps()' with the 'sort_keys' parameter.
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 409- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 410- RegEx Functions
# You can use functions from the 're' module to work with regular expressions.
import re
text = "The quick brown fox"
result = re.search(r"fox", text)

# 411- Metacharacters in RegEx
# You can use metacharacters in regular expressions to match specific patterns.
pattern = r"^The.*fox$"

# 412- RegEx Special Sequences
# Regular expressions support special sequences for matching specific types of characters or positions.
pattern = r"\bword\b"

# 413- RegEx Sets
# You can use character sets in regular expressions to match any character from the set.
pattern = r"[aeiou]"

# 414- RegEx Match Object
# When you use 're.search()', it returns a match object that contains information about the match.
pattern = r"\b(\w+)\b"

# 415- Install PIP
# To install Python packages, you can use the 'pip' tool. Instructions can vary depending on your system.

# 416- PIP Packages
# Examples for installing and using packages
# To install a package, you can use 'pip install package_name'.

# 417- PIP Remove Package
# Instructions to remove a package
# To remove a package, you can use 'pip uninstall package_name'.

# 418- Error Handling
# Examples for try, except, else, finally, raise

# 419- Handle Many Exceptions
# You can use 'try' and 'except' blocks to handle exceptions in your code.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero

# 420- Try Else
# You can use 'try' and 'else' blocks to execute code when no exceptions occur.
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred

# 421- Try Finally
# You can use 'try' and 'finally' blocks to ensure that certain code always runs.
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute

# 422- raise
# You can use the 'raise' keyword to raise an exception when a specific condition is met.
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list

# 423- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 424- Access List Items
# You can access elements in a list by their index.
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 425- Change List Item
# You can change the value of a list item by assigning a new value.
numbers[1] = 5

# 426- Loop Through List Items
# You can use a 'for' loop to iterate through the items in a list.
for num in numbers:
    print(num)

# 427- List Comprehension
# List comprehensions allow you to create new lists based on existing ones.
squares = [x ** 2 for x in numbers]

# 428- Check if List Item Exists
# You can use the 'in' keyword to check if an item exists in a list.
print(2 in numbers)  # Output: False

# 429- List Length
# You can use 'len()' to find the number of items in a list.
print(len(numbers))  # Output: 3

# 430- Add List Items
# You can add items to the end of a list using the 'append()' method.
numbers.append(4)

# 431- Remove List Items
# You can remove items from a list using the 'remove()' method.

# 432- Copy a List
# You can create a copy of a list using the 'copy()' method.
numbers_copy = numbers.copy()

# 433- Join Two Lists
# You can combine two lists using the '+' operator.
combined = numbers + squares

# 434- Tuple Methods
# Examples for count(), index()

# 435- Access Tuple Items
# You can access elements in a tuple by their index.
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 436- Check if Tuple Item Exists
# You can use the 'in' keyword to check if an item exists in a tuple.
print(3 in coordinates)  # Output: True

# 437- Tuple Length
# You can use 'len()' to find the number of items in a tuple.
print(len(coordinates))  # Output: 2

# 438- Tuple With One Item
# To create a tuple with a single item, include a trailing comma.
single_item_tuple = (5,)

# 439- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements.

# 440- Join Two Tuples
# You can combine two tuples using the '+' operator.
combined_tuple = coordinates + single_item_tuple

# 441- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 442- Access Set Items
# You can check if an item is in a set using the 'in' keyword.
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 443- Loop Set Items
# You can use a 'for' loop to iterate through the items in a set.
for fruit in fruits_set:
    print(fruit)

# 444- Check if Set Item Exists
# You can use the 'in' keyword to check if an item exists in a set.
print("pear" in fruits_set)  # Output: False

# 445- Set Length
# You can use 'len()' to find the number of items in a set.
print(len(fruits_set))  # Output: 4

# 446- Remove Set Items
# You can remove an item from a set using the 'remove()' method.

# 447- Join Two Sets
# You can combine two sets using the 'union()' method.
combined_set = fruits_set.union({"grape", "kiwi"})

# 448- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 449- Access Dictionary Items
# You can access the value associated with a key in a dictionary.
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 450- Loop Dictionary Items
# You can use a 'for' loop to iterate through key-value pairs in a dictionary.
for key, value in person.items():
    print(f"{key}: {value}")

# 451- Check if Dictionary Item Exists
# You can use the 'in' keyword to check if a key exists in a dictionary.
print("name" in person)  # Output: True

# 452- Dictionary Length
# You can use 'len()' to find the number of key-value pairs in a dictionary.
print(len(person))  # Output: 2

# 453- Add Dictionary Item
# You can add a new key-value pair to a dictionary.
person["city"] = "New York"

# 454- Remove Dictionary Items
# You can remove a key-value pair from a dictionary using 'pop()' or 'del'.

# 455- Copy Dictionary
# You can create a copy of a dictionary using the 'copy()' method.
person_copy = person.copy()

# 456- Nested Dictionaries
# You can have dictionaries within dictionaries to create nested data structures.
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 457- If Statement
# You can use 'if' statements to conditionally execute code.
x = 10
if x > 5:
    print("x is greater than 5")

# 458- If Indentation
# Indentation is important in Python and is used to define code blocks.
if x > 5:
    print("x is greater than 5")

# 459- Elif
# You can use 'elif' to check additional conditions if the previous ones are not met.
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 460- Else
# 'else' is used to define code that runs when none of the previous conditions are true.
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 461- Shorthand If
# You can use a shorthand form of 'if' for concise one-liners.
print("x is greater than y") if x > y else print("x is not greater than y")

# 462- Shorthand If Else
# You can use a shorthand form of 'if-else' for concise one-liners.
result = "Even" if x % 2 == 0 else "Odd"

# 463- If AND
# You can use 'and' to combine multiple conditions in an 'if' statement.
if x > 5 and y > 10:
    print("Both conditions are true")

# 464- If OR
# You can use 'or' to check if at least one condition is true in an 'if' statement.
if x > 5 or y > 10:
    print("At least one condition is true")

# 465- If NOT
# You can use 'not' to negate a condition in an 'if' statement.
if not x > 5:
    print("x is not greater than 5")

# 466- Nested If
# You can have 'if' statements inside other 'if' statements.
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 467- The pass Keyword in If
# 'pass' is a no-operation statement used as a placeholder where syntactically some code is required.
if x > y:
    pass
else:
    print("x is not greater than y")

# 468- While
# You can use 'while' loops to repeatedly execute a block of code as long as a condition is true.
i = 0
while i < 5:
    print(i)
    i += 1

# 469- While Break
# You can use 'break' to exit a 'while' loop prematurely.
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 470- While Continue
# You can use 'continue' to skip the rest of the code in a 'while' loop and continue with the next iteration.
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 471- While Else
# You can use 'else' with a 'while' loop to specify code that should run when the loop condition becomes false.
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 472- For
# 'for' loops are used for iterating over a sequence (that is either a list, tuple, dictionary, set, or string).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 473- Loop Through a String
# You can use 'for' loops to iterate through the characters of a string.
for char in "Python":
    print(char)

# 474- For Break
# You can use 'break' to exit a 'for' loop prematurely.
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 475- For Continue
# You can use 'continue' to skip the rest of the code in a 'for' loop and continue with the next iteration.
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 476- Looping Through a Range
# You can use the 'range()' function to generate a sequence of numbers and iterate through them.
for num in range(5):
    print(num)

# 477- For Else
# You can use 'else' with a 'for' loop to specify code that should run when the loop completes without hitting a 'break'.
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 478- Nested Loops
# You can have 'for' loops inside other 'for' loops.
for fruit in fruits:
    for char in fruit:
        print(char)

# 479- For pass
# 'pass' can be used as a placeholder where syntactically some code is required but you don't want to execute any statements.
for fruit in fruits:
    pass

# 480- Function
# You can define a function using the 'def' keyword.
def greet(name):
    print("Hello, " + name + "!")

# 481- Call a Function
# You can call a function by using its name followed by parentheses and passing arguments if required.
greet("Alice")

# 482- Function Arguments
# Functions can take parameters (or arguments) that allow you to pass values to the function.
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)

# 483- *args
# You can use '*args' to pass a variable number of arguments to a function.
def add_all(*args):
    return sum(args)

result = add_all(1, 2, 3)

# 484- Keyword Arguments
# You can pass arguments to a function by specifying the parameter names.
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet_person(name="Alice", age=25)

# 485- **kwargs
# You can use '**kwargs' to pass a variable number of keyword arguments to a function.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30)

# 486- Default Parameter Value
# You can set default values for parameters in a function.
def greet_default(name="User"):
    print(f"Hello, {name}!")

greet_default()

# 487- Passing a List as an Argument
# You can pass a list as an argument to a function.
numbers = [1, 2, 3]
def print_numbers(nums):
    for num in nums:
        print(num)

print_numbers(numbers)

# 488- Function Return Value
# A function can return a value using the 'return' keyword.
def multiply(a, b):
    return a * b

result = multiply(4, 5)

# 489- The pass Statement in Functions
# 'pass' is used as a placeholder where syntactically some code is required but you don't want to execute any statements.
def my_function():
    pass

# 490- Function Recursion
# A function can call itself, creating a recursive function.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)

# 491- Lambda Function
# Lambda functions are anonymous functions defined using the 'lambda' keyword.
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 492- Why Use Lambda Functions
# Lambda functions are useful for short, simple operations, often used with functions like 'map()' or 'filter()'.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 493- Array
# Examples for array.array()

# 494- What is an Array
# An array is a collection of elements of the same data type stored in contiguous memory locations.
import array
numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 495- Access Arrays
# You can access elements in an array by their index.
print(numbers_array[2])

# 496- Array Length
# You can find the number of elements in an array using 'len()'.
print(len(numbers_array))

# 497- Looping Array Elements
# You can use a 'for' loop to iterate through the elements of an array.
for num in numbers_array:
    print(num)

# 498- Add Array Element
# You can add an element to the end of an array using the 'append()' method.
numbers_array.append(6)

# 499- Remove Array Element
# You can remove an element from an array using the 'remove()' method.

# 500- Array Methods
# Arrays have methods like 'extend()', 'fromlist()', 'tolist()', etc.

# 501- Class
# Examples for class definition, instantiation, and methods

# 502- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 503- The Class init() Function
# See the example above

# 504- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 505- self
# Refer to the example above

# 506- Modify Object Properties
my_dog.age = 4

# 507- Delete Object Properties
del my_dog.age

# 508- Delete Object
del my_dog


# 509- Class pass Statement
class MyClass:
    pass


# 510- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 511- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 512- Create the init() Function
# See the example above

# 513- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 514- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 515- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 516- Iterators
# Examples for iter() and next()
# 517- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 518- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 519- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 520- StopIteration
# See the example above

# 521- Global Scope
global_var = "I am global"


# 522- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 523- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 524- Variables in Modules
# See the example above

# 525- Renaming a Module
# See the example above

# 526- Built-in Modules
import math

# 527- Using the dir() Function
print(dir(math))

# 528- Import From Module
from math import sqrt

# 529- Datetime Module
import datetime

# 530- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 531- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 532- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 533- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 534- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 535- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 536- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 537- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 538- Metacharacters in RegEx
pattern = r"^The.*fox$"

# 539- RegEx Special Sequences
pattern = r"\bword\b"

# 540- RegEx Sets
pattern = r"[aeiou]"

# 541- RegEx Match Object
pattern = r"\b(\w+)\b"

# 542- Install PIP
# Instructions to install PIP

# 543- PIP Packages
# Examples for installing and using packages

# 544- PIP Remove Package
# Instructions to remove a package

# 545- Error Handling
# Examples for try, except, else, finally, raise

# 546- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 547- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 548- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 549- raise
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list

# 550- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 551- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 552- Change List Item
numbers[1] = 5

# 553- Loop Through List Items
for num in numbers:
    print(num)

# 554- List Comprehension
squares = [x ** 2 for x in numbers]

# 555- Check if List Item Exists
print(2 in numbers)  # Output: False

# 556- List Length
print(len(numbers))  # Output: 3

# 557- Add List Items
numbers.append(4)

# 558- Remove List Items
# numbers.remove(2)

# 559- Copy a List
numbers_copy = numbers.copy()

# 560- Join Two Lists
combined = numbers + squares

# 561- Tuple Methods
# Examples for count(), index()

# 562- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 563- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 564- Tuple Length
print(len(coordinates))  # Output: 2

# 565- Tuple With One Item
single_item_tuple = (5,)

# 566- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 567- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 568- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 569- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 570- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 571- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 572- Set Length
print(len(fruits_set))  # Output: 4

# 573- Remove Set Items
fruits_set.remove("banana")

# 574- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 575- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 576- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 577- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 578- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 579- Dictionary Length
print(len(person))  # Output: 2

# 580- Add Dictionary Item
person["city"] = "New York"

# 581- Remove Dictionary Items
person.pop("age")

# 582- Copy Dictionary
person_copy = person.copy()

# 583- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 584- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 585- If Indentation
if x > 5:
    print("x is greater than 5")

# 586- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 587- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 588- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 589- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 590- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 591- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 592- If NOT
if not x > 5:
    print("x is not greater than 5")

# 593- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 594- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 595- While
i = 0
while i < 5:
    print(i)
    i += 1

# 596- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 597- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 598- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 599- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 600- Loop Through a String
for char in "Python":
    print(char)

# 601- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 602- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 603- Looping Through a Range
for num in range(5):
    print(num)

# 604- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 605- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 606- For pass
for fruit in fruits:
    pass


# 607- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 608- Call a Function
greet("Bob")


# 609- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 610- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 611- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 612- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 613- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 614- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 615- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 616- The pass Statement in Functions
def my_function():
    pass


# 617- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 618- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 619- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 620- Array
# Examples for array.array()

# 621- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 622- Access Arrays
print(numbers_array[2])

# 623- Array Length
print(len(numbers_array))

# 624- Looping Array Elements
for num in numbers_array:
    print(num)

# 625- Add Array Element
numbers_array.append(6)

# 626- Remove Array Element
numbers_array.remove(3)


# 627- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 628- Class
# Examples for class definition, instantiation, and methods

# 629- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 630- The Class init() Function
# See the example above

# 631- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 632- self
# Refer to the example above

# 633- Modify Object Properties
my_dog.age = 4

# 634- Delete Object Properties
del my_dog.age

# 635- Delete Object
del my_dog


# 636- Class pass Statement
class MyClass:
    pass


# 637- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 638- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 639- Create the init() Function
# See the example above

# 640- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 641- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 642- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 643- Iterators
# Examples for iter() and next()
# 644- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 645- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 646- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 647- StopIteration
# See the example above

# 648- Global Scope
global_var = "I am global"


# 649- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 650- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 651- Variables in Modules
# See the example above

# 652- Renaming a Module
# See the example above

# 653- Built-in Modules
import math

# 654- Using the dir() Function
print(dir(math))

# 655- Import From Module
from math import sqrt

# 656- Datetime Module
import datetime

# 657- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 658- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 659- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 660- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 661- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 662- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 663- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 664- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 665- Metacharacters in RegEx
pattern = r"^The.*fox$"

# 666- RegEx Special Sequences
pattern = r"\bword\b"

# 667- RegEx Sets
pattern = r"[aeiou]"

# 668- RegEx Match Object
pattern = r"\b(\w+)\b"

# 669- Install PIP
# Instructions to install PIP

# 670- PIP Packages
# Examples for installing and using packages

# 671- PIP Remove Package
# Instructions to remove a package

# 672- Error Handling
# Examples for try, except, else, finally, raise

# 673- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 674- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 675- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 676- raise
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list

# 677- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 678- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 679- Change List Item
numbers[1] = 5

# 680- Loop Through List Items
for num in numbers:
    print(num)

# 681- List Comprehension
squares = [x ** 2 for x in numbers]

# 682- Check if List Item Exists
print(2 in numbers)  # Output: False

# 683- List Length
print(len(numbers))  # Output: 3

# 684- Add List Items
numbers.append(4)

# 685- Remove List Items
# numbers.remove(2)

# 686- Copy a List
numbers_copy = numbers.copy()

# 687- Join Two Lists
combined = numbers + squares

# 688- Tuple Methods
# Examples for count(), index()

# 689- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 690- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 691- Tuple Length
print(len(coordinates))  # Output: 2

# 692- Tuple With One Item
single_item_tuple = (5,)

# 693- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 694- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 695- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 696- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 697- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 698- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 699- Set Length
print(len(fruits_set))  # Output: 4

# 700- Remove Set Items
fruits_set.remove("banana")

# 701- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 702- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 703- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 704- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 705- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 706- Dictionary Length
print(len(person))  # Output: 2

# 707- Add Dictionary Item
person["city"] = "New York"

# 708- Remove Dictionary Items
person.pop("age")

# 709- Copy Dictionary
person_copy = person.copy()

# 710- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 711- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 712- If Indentation
if x > 5:
    print("x is greater than 5")

# 713- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 714- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 715- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 716- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 717- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 718- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 719- If NOT
if not x > 5:
    print("x is not greater than 5")

# 720- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 721- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 722- While
i = 0
while i < 5:
    print(i)
    i += 1

# 723- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 724- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 725- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 726- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 727- Loop Through a String
for char in "Python":
    print(char)

# 728- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 729- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 730- Looping Through a Range
for num in range(5):
    print(num)

# 731- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 732- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 733- For pass
for fruit in fruits:
    pass


# 734- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 735- Call a Function
greet("Bob")


# 736- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 737- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 738- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 739- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 740- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 741- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 742- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 743- The pass Statement in Functions
def my_function():
    pass


# 744- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 745- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 746- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 747- Array
# Examples for array.array()

# 748- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 749- Access Arrays
print(numbers_array[2])

# 750- Array Length
print(len(numbers_array))

# 751- Looping Array Elements
for num in numbers_array:
    print(num)

# 752- Add Array Element
numbers_array.append(6)

# 753- Remove Array Element
numbers_array.remove(3)


# 754- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 755- Class
# Examples for class definition, instantiation, and methods

# 756- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 757- The Class init() Function
# See the example above

# 758- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 759- self
# Refer to the example above

# 760- Modify Object Properties
my_dog.age = 4

# 761- Delete Object Properties
del my_dog.age

# 762- Delete Object
del my_dog


# 763- Class pass Statement
class MyClass:
    pass


# 764- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 765- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 766- Create the init() Function
# See the example above

# 767- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 768- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 769- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 770- Iterators
# Examples for iter() and next()
# 771- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 772- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 773- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 774- StopIteration
# See the example above

# 775- Global Scope
global_var = "I am global"


# 776- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 777- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 778- Variables in Modules
# See the example above

# 779- Renaming a Module
# See the example above

# 780- Built-in Modules
import math

# 781- Using the dir() Function
print(dir(math))

# 782- Import From Module
from math import sqrt

# 783- Datetime Module
import datetime

# 784- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 785- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 786- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 787- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 788- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 789- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 790- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 791- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 792- Metacharacters in RegEx
pattern = r"^The.*fox$"

# 793- RegEx Special Sequences
pattern = r"\bword\b"

# 794- RegEx Sets
pattern = r"[aeiou]"

# 795- RegEx Match Object
pattern = r"\b(\w+)\b"

# 796- Install PIP
# Instructions to install PIP

# 797- PIP Packages
# Examples for installing and using packages

# 798- PIP Remove Package
# Instructions to remove a package

# 799- Error Handling
# Examples for try, except, else, finally, raise

# 800- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 801- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 802- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 803- raise
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list

# 804- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 805- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 806- Change List Item
numbers[1] = 5

# 807- Loop Through List Items
for num in numbers:
    print(num)

# 808- List Comprehension
squares = [x ** 2 for x in numbers]

# 809- Check if List Item Exists
print(2 in numbers)  # Output: False

# 810- List Length
print(len(numbers))  # Output: 3

# 811- Add List Items
numbers.append(4)

# 812- Remove List Items
# numbers.remove(2)

# 813- Copy a List
numbers_copy = numbers.copy()

# 814- Join Two Lists
combined = numbers + squares

# 815- Tuple Methods
# Examples for count(), index()

# 816- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 817- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 818- Tuple Length
print(len(coordinates))  # Output: 2

# 819- Tuple With One Item
single_item_tuple = (5,)

# 820- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 821- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 822- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 823- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 824- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 825- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 826- Set Length
print(len(fruits_set))  # Output: 4

# 827- Remove Set Items
fruits_set.remove("banana")

# 828- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 829- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 830- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 831- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 832- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 833- Dictionary Length
print(len(person))  # Output: 2

# 834- Add Dictionary Item
person["city"] = "New York"

# 835- Remove Dictionary Items
person.pop("age")

# 836- Copy Dictionary
person_copy = person.copy()

# 837- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 838- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 839- If Indentation
if x > 5:
    print("x is greater than 5")

# 840- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 841- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 842- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 843- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 844- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 845- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 846- If NOT
if not x > 5:
    print("x is not greater than 5")

# 847- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 848- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 849- While
i = 0
while i < 5:
    print(i)
    i += 1

# 850- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 851- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 852- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 853- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 854- Loop Through a String
for char in "Python":
    print(char)

# 855- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 856- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 857- Looping Through a Range
for num in range(5):
    print(num)

# 858- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 859- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 860- For pass
for fruit in fruits:
    pass


# 861- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 862- Call a Function
greet("Bob")


# 863- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 864- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 865- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 866- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 867- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 868- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 869- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 870- The pass Statement in Functions
def my_function():
    pass


# 871- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 872- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 873- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 874- Array
# Examples for array.array()

# 875- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 876- Access Arrays
print(numbers_array[2])

# 877- Array Length
print(len(numbers_array))

# 878- Looping Array Elements
for num in numbers_array:
    print(num)

# 879- Add Array Element
numbers_array.append(6)

# 880- Remove Array Element
numbers_array.remove(3)


# 881- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 882- Class
# Examples for class definition, instantiation, and methods

# 883- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 884- The Class init() Function
# See the example above

# 885- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 886- self
# Refer to the example above

# 887- Modify Object Properties
my_dog.age = 4

# 888- Delete Object Properties
del my_dog.age

# 889- Delete Object
del my_dog


# 890- Class pass Statement
class MyClass:
    pass


# 891- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 892- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 893- Create the init() Function
# See the example above

# 894- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 895- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 896- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 897- Iterators
# Examples for iter() and next()
# 898- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 899- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 900- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 901- StopIteration
# See the example above

# 902- Global Scope
global_var = "I am global"


# 903- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 904- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 905- Variables in Modules
# See the example above

# 906- Renaming a Module
# See the example above

# 907- Built-in Modules
import math

# 908- Using the dir() Function
print(dir(math))

# 909- Import From Module
from math import sqrt

# 910- Datetime Module
import datetime

# 911- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 912- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 913- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 914- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 915- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 916- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 917- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 918- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 919- RegEx Metacharacters
pattern = r"^The.*fox$"

# 920- RegEx Special Sequences
pattern = r"\bword\b"

# 921- RegEx Sets
pattern = r"[aeiou]"

# 922- RegEx Match Object
pattern = r"\b(\w+)\b"

# 923- Install PIP
# Instructions to install PIP

# 924- PIP Packages
# Examples for installing and using packages

# 925- PIP Remove Package
# Instructions to remove a package

# 926- Error Handling
# Examples for try, except, else, finally, raise

# 927- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 928- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 929- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 930- raise
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list

# 931- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 932- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 933- Change List Item
numbers[1] = 5

# 934- Loop Through List Items
for num in numbers:
    print(num)

# 935- List Comprehension
squares = [x ** 2 for x in numbers]

# 936- Check if List Item Exists
print(2 in numbers)  # Output: False

# 937- List Length
print(len(numbers))  # Output: 3

# 938- Add List Items
numbers.append(4)

# 939- Remove List Items
# numbers.remove(2)

# 940- Copy a List
numbers_copy = numbers.copy()

# 941- Join Two Lists
combined = numbers + squares

# 942- Tuple Methods
# Examples for count(), index()

# 943- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 944- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 945- Tuple Length
print(len(coordinates))  # Output: 2

# 946- Tuple With One Item
single_item_tuple = (5,)

# 947- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 948- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 949- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 950- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 951- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 952- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 953- Set Length
print(len(fruits_set))  # Output: 4

# 954- Remove Set Items
fruits_set.remove("banana")

# 955- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 956- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 957- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 958- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 959- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 960- Dictionary Length
print(len(person))  # Output: 2

# 961- Add Dictionary Item
person["city"] = "New York"

# 962- Remove Dictionary Items
person.pop("age")

# 963- Copy Dictionary
person_copy = person.copy()

# 964- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 965- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 966- If Indentation
if x > 5:
    print("x is greater than 5")

# 967- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 968- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 969- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 970- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 971- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 972- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 973- If NOT
if not x > 5:
    print("x is not greater than 5")

# 974- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 975- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 976- While
i = 0
while i < 5:
    print(i)
    i += 1

# 977- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 978- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 979- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 980- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 981- Loop Through a String
for char in "Python":
    print(char)

# 982- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 983- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 984- Looping Through a Range
for num in range(5):
    print(num)

# 985- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 986- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 987- For pass
for fruit in fruits:
    pass


# 988- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 989- Call a Function
greet("Bob")


# 990- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 991- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 992- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 993- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 994- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 995- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 996- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 997- The pass Statement in Functions
def my_function():
    pass


# 998- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 999- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 1000- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 1001- Array
# Examples for array.array()

# 1002- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 1003- Access Arrays
print(numbers_array[2])

# 1004- Array Length
print(len(numbers_array))

# 1005- Looping Array Elements
for num in numbers_array:
    print(num)

# 1006- Add Array Element
numbers_array.append(6)

# 1007- Remove Array Element
numbers_array.remove(3)


# 1008- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 1009- Class
# Examples for class definition, instantiation, and methods

# 1010- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1011- The Class init() Function
# See the example above

# 1012- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 1013- self
# Refer to the example above

# 1014- Modify Object Properties
my_dog.age = 4

# 1015- Delete Object Properties
del my_dog.age

# 1016- Delete Object
del my_dog


# 1017- Class pass Statement
class MyClass:
    pass


# 1018- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 1019- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 1020- Create the init() Function
# See the example above

# 1021- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 1022- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 1023- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 1024- Iterators
# Examples for iter() and next()
# 1025- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 1026- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 1027- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 1028- StopIteration
# See the example above

# 1029- Global Scope
global_var = "I am global"


# 1030- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 1031- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 1032- Variables in Modules
# See the example above

# 1033- Renaming a Module
# See the example above

# 1034- Built-in Modules
import math

# 1035- Using the dir() Function
print(dir(math))

# 1036- Import From Module
from math import sqrt

# 1037- Datetime Module
import datetime

# 1038- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 1039- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 1040- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 1041- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 1042- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 1043- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 1044- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 1045- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 1046- RegEx Metacharacters
pattern = r"^The.*fox$"

# 1047- RegEx Special Sequences
pattern = r"\bword\b"

# 1048- RegEx Sets
pattern = r"[aeiou]"

# 1049- RegEx Match Object
pattern = r"\b(\w+)\b"

# 1050- Install PIP
# Instructions to install PIP

# 1051- PIP Packages
# Examples for installing and using packages

# 1052- PIP Remove Package
# Instructions to remove a package

# 1053- Error Handling
# Examples for try, except, else, finally, raise

# 1054- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 1055- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 1056- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 1057- raise
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list

# 1058- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 1059- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 1060- Change List Item
numbers[1] = 5

# 1061- Loop Through List Items
for num in numbers:
    print(num)

# 1062- List Comprehension
squares = [x ** 2 for x in numbers]

# 1063- Check if List Item Exists
print(2 in numbers)  # Output: False

# 1064- List Length
print(len(numbers))  # Output: 3

# 1065- Add List Items
numbers.append(4)

# 1066- Remove List Items
# numbers.remove(2)

# 1067- Copy a List
numbers_copy = numbers.copy()

# 1068- Join Two Lists
combined = numbers + squares

# 1069- Tuple Methods
# Examples for count(), index()

# 1070- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 1071- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 1072- Tuple Length
print(len(coordinates))  # Output: 2

# 1073- Tuple With One Item
single_item_tuple = (5,)

# 1074- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 1075- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 1076- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 1077- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 1078- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 1079- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 1080- Set Length
print(len(fruits_set))  # Output: 4

# 1081- Remove Set Items
fruits_set.remove("banana")

# 1082- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 1083- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 1084- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 1085- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 1086- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 1087- Dictionary Length
print(len(person))  # Output: 2

# 1088- Add Dictionary Item
person["city"] = "New York"

# 1089- Remove Dictionary Items
person.pop("age")

# 1090- Copy Dictionary
person_copy = person.copy()

# 1091- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 1092- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 1093- If Indentation
if x > 5:
    print("x is greater than 5")

# 1094- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 1095- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 1096- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 1097- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 1098- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 1099- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 1100- If NOT
if not x > 5:
    print("x is not greater than 5")

# 1101- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 1102- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 1103- While
i = 0
while i < 5:
    print(i)
    i += 1

# 1104- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 1105- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 1106- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 1107- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 1108- Loop Through a String
for char in "Python":
    print(char)

# 1109- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 1110- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 1111- Looping Through a Range
for num in range(5):
    print(num)

# 1112- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 1113- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 1114- For pass
for fruit in fruits:
    pass


# 1115- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 1116- Call a Function
greet("Bob")


# 1117- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 1118- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 1119- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 1120- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 1121- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 1122- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 1123- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 1124- The pass Statement in Functions
def my_function():
    pass


# 1125- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 1126- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 1127- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 1128- Array
# Examples for array.array()

# 1129- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 1130- Access Arrays
print(numbers_array[2])

# 1131- Array Length
print(len(numbers_array))

# 1132- Looping Array Elements
for num in numbers_array:
    print(num)

# 1133- Add Array Element
numbers_array.append(6)

# 1134- Remove Array Element
numbers_array.remove(3)


# 1135- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 1136- Class
# Examples for class definition, instantiation, and methods

# 1137- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1138- The Class init() Function
# See the example above

# 1139- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 1140- self
# Refer to the example above

# 1141- Modify Object Properties
my_dog.age = 4

# 1142- Delete Object Properties
del my_dog.age

# 1143- Delete Object
del my_dog


# 1144- Class pass Statement
class MyClass:
    pass


# 1145- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 1146- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 1147- Create the init() Function
# See the example above

# 1148- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 1149- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 1150- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 1151- Iterators
# Examples for iter() and next()
# 1152- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 1153- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 1154- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 1155- StopIteration
# See the example above

# 1156- Global Scope
global_var = "I am global"


# 1157- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 1158- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 1159- Variables in Modules
# See the example above

# 1160- Renaming a Module
# See the example above

# 1161- Built-in Modules
import math

# 1162- Using the dir() Function
print(dir(math))

# 1163- Import From Module
from math import sqrt

# 1164- Datetime Module
import datetime

# 1165- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 1166- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 1167- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 1168- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 1169- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 1170- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 1171- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 1172- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 1173- RegEx Metacharacters
pattern = r"^The.*fox$"

# 1174- RegEx Special Sequences
pattern = r"\bword\b"

# 1175- RegEx Sets
pattern = r"[aeiou]"

# 1176- RegEx Match Object
pattern = r"\b(\w+)\b"

# 1177- Install PIP
# Instructions to install PIP

# 1178- PIP Packages
# Examples for installing and using packages

# 1179- PIP Remove Package
# Instructions to remove a package

# 1180- Error Handling
# Examples for try, except, else, finally, raise

# 1181- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 1182- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 1183- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 1184- raise
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list

# 1185- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 1186- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 1187- Change List Item
numbers[1] = 5

# 1188- Loop Through List Items
for num in numbers:
    print(num)

# 1189- List Comprehension
squares = [x ** 2 for x in numbers]

# 1190- Check if List Item Exists
print(2 in numbers)  # Output: False

# 1191- List Length
print(len(numbers))  # Output: 3

# 1192- Add List Items
numbers.append(4)

# 1193- Remove List Items
# numbers.remove(2)

# 1194- Copy a List
numbers_copy = numbers.copy()

# 1195- Join Two Lists
combined = numbers + squares

# 1196- Tuple Methods
# Examples for count(), index()

# 1197- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 1198- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 1199- Tuple Length
print(len(coordinates))  # Output: 2

# 1200- Tuple With One Item
single_item_tuple = (5,)

# 1201- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 1202- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 1203- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 1204- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 1205- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 1206- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 1207- Set Length
print(len(fruits_set))  # Output: 4

# 1208- Remove Set Items
fruits_set.remove("banana")

# 1209- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 1210- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 1211- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 1212- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 1213- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 1214- Dictionary Length
print(len(person))  # Output: 2

# 1215- Add Dictionary Item
person["city"] = "New York"

# 1216- Remove Dictionary Items
person.pop("age")

# 1217- Copy Dictionary
person_copy = person.copy()

# 1218- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 1219- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 1220- If Indentation
if x > 5:
    print("x is greater than 5")

# 1221- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 1222- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 1223- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 1224- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 1225- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 1226- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 1227- If NOT
if not x > 5:
    print("x is not greater than 5")

# 1228- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 1229- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 1230- While
i = 0
while i < 5:
    print(i)
    i += 1

# 1231- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 1232- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 1233- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 1234- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 1235- Loop Through a String
for char in "Python":
    print(char)

# 1236- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 1237- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 1238- Looping Through a Range
for num in range(5):
    print(num)

# 1239- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 1240- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 1241- For pass
for fruit in fruits:
    pass


# 1242- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 1243- Call a Function
greet("Bob")


# 1244- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 1245- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 1246- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 1247- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 1248- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 1249- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 1250- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 1251- The pass Statement in Functions
def my_function():
    pass


# 1252- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 1253- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 1254- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 1255- Array
# Examples for array.array()

# 1256- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 1257- Access Arrays
print(numbers_array[2])

# 1258- Array Length
print(len(numbers_array))

# 1259- Looping Array Elements
for num in numbers_array:
    print(num)

# 1260- Add Array Element
numbers_array.append(6)

# 1261- Remove Array Element
numbers_array.remove(3)


# 1262- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 1263- Class
# Examples for class definition, instantiation, and methods

# 1264- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1265- The Class init() Function
# See the example above

# 1266- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 1267- self
# Refer to the example above

# 1268- Modify Object Properties
my_dog.age = 4

# 1269- Delete Object Properties
del my_dog.age

# 1270- Delete Object
del my_dog


# 1271- Class pass Statement
class MyClass:
    pass


# 1272- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 1273- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 1274- Create the init() Function
# See the example above

# 1275- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 1276- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 1277- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 1278- Iterators
# Examples for iter() and next()
# 1279- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 1280- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 1281- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 1282- StopIteration
# See the example above

# 1283- Global Scope
global_var = "I am global"


# 1284- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 1285- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 1286- Variables in Modules
# See the example above

# 1287- Renaming a Module
# See the example above

# 1288- Built-in Modules
import math

# 1289- Using the dir() Function
print(dir(math))

# 1290- Import From Module
from math import sqrt

# 1291- Datetime Module
import datetime

# 1292- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 1293- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 1294- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 1295- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 1296- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 1297- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 1298- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 1299- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 1300- RegEx Metacharacters
pattern = r"^The.*fox$"

# 1301- RegEx Special Sequences
pattern = r"\bword\b"

# 1302- RegEx Sets
pattern = r"[aeiou]"

# 1303- RegEx Match Object
pattern = r"\b(\w+)\b"

# 1304- Install PIP
# Instructions to install PIP

# 1305- PIP Packages
# Examples for installing and using packages

# 1306- PIP Remove Package
# Instructions to remove a package

# 1307- Error Handling
# Examples for try, except, else, finally, raise

# 1308- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 1309- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 1310- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 1311- raise
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list

# 1312- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 1313- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 1314- Change List Item
numbers[1] = 5

# 1315- Loop Through List Items
for num in numbers:
    print(num)

# 1316- List Comprehension
squares = [x ** 2 for x in numbers]

# 1317- Check if List Item Exists
print(2 in numbers)  # Output: False

# 1318- List Length
print(len(numbers))  # Output: 3

# 1319- Add List Items
numbers.append(4)

# 1320- Remove List Items
# numbers.remove(2)

# 1321- Copy a List
numbers_copy = numbers.copy()

# 1322- Join Two Lists
combined = numbers + squares

# 1323- Tuple Methods
# Examples for count(), index()

# 1324- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 1325- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 1326- Tuple Length
print(len(coordinates))  # Output: 2

# 1327- Tuple With One Item
single_item_tuple = (5,)

# 1328- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 1329- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 1330- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 1331- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 1332- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 1333- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 1334- Set Length
print(len(fruits_set))  # Output: 4

# 1335- Remove Set Items
fruits_set.remove("banana")

# 1336- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 1337- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 1338- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 1339- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 1340- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 1341- Dictionary Length
print(len(person))  # Output: 2

# 1342- Add Dictionary Item
person["city"] = "New York"

# 1343- Remove Dictionary Items
person.pop("age")

# 1344- Copy Dictionary
person_copy = person.copy()

# 1345- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 1346- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 1347- If Indentation
if x > 5:
    print("x is greater than 5")

# 1348- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 1349- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 1350- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 1351- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 1352- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 1353- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 1354- If NOT
if not x > 5:
    print("x is not greater than 5")

# 1355- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 1356- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 1357- While
i = 0
while i < 5:
    print(i)
    i += 1

# 1358- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 1359- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 1360- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 1361- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 1362- Loop Through a String
for char in "Python":
    print(char)

# 1363- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 1364- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 1365- Looping Through a Range
for num in range(5):
    print(num)

# 1366- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 1367- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 1368- For pass
for fruit in fruits:
    pass


# 1369- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 1370- Call a Function
greet("Bob")


# 1371- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 1372- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 1373- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 1374- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 1375- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 1376- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 1377- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 1378- The pass Statement in Functions
def my_function():
    pass


# 1379- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 1380- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 1381- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 1382- Array
# Examples for array.array()

# 1383- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 1384- Access Arrays
print(numbers_array[2])

# 1385- Array Length
print(len(numbers_array))

# 1386- Looping Array Elements
for num in numbers_array:
    print(num)

# 1387- Add Array Element
numbers_array.append(6)

# 1388- Remove Array Element
numbers_array.remove(3)


# 1389- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 1390- Class
# Examples for class definition, instantiation, and methods

# 1391- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1392- The Class init() Function
# See the example above

# 1393- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 1394- self
# Refer to the example above

# 1395- Modify Object Properties
my_dog.age = 4

# 1396- Delete Object Properties
del my_dog.age

# 1397- Delete Object
del my_dog


# 1398- Class pass Statement
class MyClass:
    pass


# 1399- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 1400- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 1401- Create the init() Function
# See the example above

# 1402- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 1403- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 1404- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 1405- Iterators
# Examples for iter() and next()
# 1406- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 1407- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 1408- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 1409- StopIteration
# See the example above

# 1410- Global Scope
global_var = "I am global"


# 1411- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 1412- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 1413- Variables in Modules
# See the example above

# 1414- Renaming a Module
# See the example above

# 1415- Built-in Modules
import math

# 1416- Using the dir() Function
print(dir(math))

# 1417- Import From Module
from math import sqrt

# 1418- Datetime Module
import datetime

# 1419- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 1420- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 1421- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 1422- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 1423- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 1424- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 1425- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 1426- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 1427- RegEx Metacharacters
pattern = r"^The.*fox$"

# 1428- RegEx Special Sequences
pattern = r"\bword\b"

# 1429- RegEx Sets
pattern = r"[aeiou]"

# 1430- RegEx Match Object
pattern = r"\b(\w+)\b"

# 1431- Install PIP
# Instructions to install PIP

# 1432- PIP Packages
# Examples for installing and using packages

# 1433- PIP Remove Package
# Instructions to remove a package

# 1434- Error Handling
# Examples for try, except, else, finally, raise

# 1435- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 1436- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 1437- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 1438- raise
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list

# 1439- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 1440- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 1441- Change List Item
numbers[1] = 5

# 1442- Loop Through List Items
for num in numbers:
    print(num)

# 1443- List Comprehension
squares = [x ** 2 for x in numbers]

# 1444- Check if List Item Exists
print(2 in numbers)  # Output: False

# 1445- List Length
print(len(numbers))  # Output: 3

# 1446- Add List Items
numbers.append(4)

# 1447- Remove List Items
# numbers.remove(2)

# 1448- Copy a List
numbers_copy = numbers.copy()

# 1449- Join Two Lists
combined = numbers + squares

# 1450- Tuple Methods
# Examples for count(), index()

# 1451- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 1452- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 1453- Tuple Length
print(len(coordinates))  # Output: 2

# 1454- Tuple With One Item
single_item_tuple = (5,)

# 1455- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 1456- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 1457- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 1458- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 1459- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 1460- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 1461- Set Length
print(len(fruits_set))  # Output: 4

# 1462- Remove Set Items
fruits_set.remove("banana")

# 1463- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 1464- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 1465- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 1466- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 1467- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 1468- Dictionary Length
print(len(person))  # Output: 2

# 1469- Add Dictionary Item
person["city"] = "New York"

# 1470- Remove Dictionary Items
person.pop("age")

# 1471- Copy Dictionary
person_copy = person.copy()

# 1472- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 1473- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 1474- If Indentation
if x > 5:
    print("x is greater than 5")

# 1475- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 1476- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 1477- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 1478- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 1479- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 1480- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 1481- If NOT
if not x > 5:
    print("x is not greater than 5")

# 1482- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 1483- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 1484- While
i = 0
while i < 5:
    print(i)
    i += 1

# 1485- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 1486- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 1487- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 1488- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 1489- Loop Through a String
for char in "Python":
    print(char)

# 1490- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 1491- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 1492- Looping Through a Range
for num in range(5):
    print(num)

# 1493- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 1494- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 1495- For pass
for fruit in fruits:
    pass


# 1496- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 1497- Call a Function
greet("Bob")


# 1498- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 1499- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 1500- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 1501- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 1502- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 1503- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 1504- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 1505- The pass Statement in Functions
def my_function():
    pass


# 1506- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 1507- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 1508- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 1509- Array
# Examples for array.array()

# 1510- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 1511- Access Arrays
print(numbers_array[2])

# 1512- Array Length
print(len(numbers_array))

# 1513- Looping Array Elements
for num in numbers_array:
    print(num)

# 1514- Add Array Element
numbers_array.append(6)

# 1515- Remove Array Element
numbers_array.remove(3)


# 1516- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 1517- Class
# Examples for class definition, instantiation, and methods

# 1518- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1519- The Class init() Function
# See the example above

# 1520- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 1521- self
# Refer to the example above

# 1522- Modify Object Properties
my_dog.age = 4

# 1523- Delete Object Properties
del my_dog.age

# 1524- Delete Object
del my_dog


# 1525- Class pass Statement
class MyClass:
    pass


# 1526- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 1527- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 1528- Create the init() Function
# See the example above

# 1529- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 1530- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 1531- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 1532- Iterators
# Examples for iter() and next()
# 1533- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 1534- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 1535- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 1536- StopIteration
# See the example above

# 1537- Global Scope
global_var = "I am global"


# 1538- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 1539- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 1540- Variables in Modules
# See the example above

# 1541- Renaming a Module
# See the example above

# 1542- Built-in Modules
import math

# 1543- Using the dir() Function
print(dir(math))

# 1544- Import From Module
from math import sqrt

# 1545- Datetime Module
import datetime

# 1546- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 1547- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 1548- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 1549- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 1550- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 1551- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 1552- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 1553- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 1554- RegEx Metacharacters
pattern = r"^The.*fox$"

# 1555- RegEx Special Sequences
pattern = r"\bword\b"

# 1556- RegEx Sets
pattern = r"[aeiou]"

# 1557- RegEx Match Object
pattern = r"\b(\w+)\b"

# 1558- Install PIP
# Instructions to install PIP

# 1559- PIP Packages
# Examples for installing and using packages

# 1560- PIP Remove Package
# Instructions to remove a package

# 1561- Error Handling
# Examples for try, except, else, finally, raise

# 1562- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 1563- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 1564- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 1565- raise
x = -1
if x < 0:
    raise ValueError("x cannot be negative")
# Output:
# ValueError: x cannot be negative

# 1566- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 1567- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 1568- Change List Item
numbers[1] = 5

# 1569- Loop Through List Items
for num in numbers:
    print(num)

# 1570- List Comprehension
squares = [x ** 2 for x in numbers]

# 1571- Check if List Item Exists
print(2 in numbers)  # Output: False

# 1572- List Length
print(len(numbers))  # Output: 3

# 1573- Add List Items
numbers.append(4)

# 1574- Remove List Items
# numbers.remove(2)

# 1575- Copy a List
numbers_copy = numbers.copy()

# 1576- Join Two Lists
combined = numbers + squares

# 1577- Tuple Methods
# Examples for count(), index()

# 1578- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 1579- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 1580- Tuple Length
print(len(coordinates))  # Output: 2

# 1581- Tuple With One Item
single_item_tuple = (5,)

# 1582- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 1583- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 1584- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 1585- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 1586- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 1587- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 1588- Set Length
print(len(fruits_set))  # Output: 4

# 1589- Remove Set Items
fruits_set.remove("banana")

# 1590- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 1591- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 1592- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 1593- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 1594- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 1595- Dictionary Length
print(len(person))  # Output: 2

# 1596- Add Dictionary Item
person["city"] = "New York"

# 1597- Remove Dictionary Items
person.pop("age")

# 1598- Copy Dictionary
person_copy = person.copy()

# 1599- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 1600- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 1601- If Indentation
if x > 5:
    print("x is greater than 5")

# 1602- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 1603- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 1604- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 1605- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 1606- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 1607- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 1608- If NOT
if not x > 5:
    print("x is not greater than 5")

# 1609- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 1610- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 1611- While
i = 0
while i < 5:
    print(i)
    i += 1

# 1612- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 1613- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 1614- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 1615- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 1616- Loop Through a String
for char in "Python":
    print(char)

# 1617- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 1618- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 1619- Looping Through a Range
for num in range(5):
    print(num)

# 1620- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 1621- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 1622- For pass
for fruit in fruits:
    pass


# 1623- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 1624- Call a Function
greet("Bob")


# 1625- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 1626- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 1627- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 1628- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 1629- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 1630- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 1631- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 1632- The pass Statement in Functions
def my_function():
    pass


# 1633- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 1634- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 1635- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 1636- Array
# Examples for array.array()

# 1637- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 1638- Access Arrays
print(numbers_array[2])

# 1639- Array Length
print(len(numbers_array))

# 1640- Looping Array Elements
for num in numbers_array:
    print(num)

# 1641- Add Array Element
numbers_array.append(6)

# 1642- Remove Array Element
numbers_array.remove(3)


# 1643- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 1644- Class
# Examples for class definition, instantiation, and methods

# 1645- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1646- The Class init() Function
# See the example above

# 1647- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 1648- self
# Refer to the example above

# 1649- Modify Object Properties
my_dog.age = 4

# 1650- Delete Object Properties
del my_dog.age

# 1651- Delete Object
del my_dog


# 1652- Class pass Statement
class MyClass:
    pass


# 1653- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 1654- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 1655- Create the init() Function
# See the example above

# 1656- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 1657- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 1658- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 1659- Iterators
# Examples for iter() and next()
# 1660- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 1661- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 1662- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 1663- StopIteration
# See the example above

# 1664- Global Scope
global_var = "I am global"


# 1665- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 1666- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 1667- Variables in Modules
# See the example above

# 1668- Renaming a Module
# See the example above

# 1669- Built-in Modules
import math

# 1670- Using the dir() Function
print(dir(math))

# 1671- Import From Module
from math import sqrt

# 1672- Datetime Module
import datetime

# 1673- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 1674- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 1675- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 1676- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 1677- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 1678- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 1679- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 1680- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 1681- RegEx Metacharacters
pattern = r"^The.*fox$"

# 1682- RegEx Special Sequences
pattern = r"\bword\b"

# 1683- RegEx Sets
pattern = r"[aeiou]"

# 1684- RegEx Match Object
pattern = r"\b(\w+)\b"

# 1685- Install PIP
# Instructions to install PIP

# 1686- PIP Packages
# Examples for installing and using packages

# 1687- PIP Remove Package
# Instructions to remove a package

# 1688- Error Handling
# Examples for try, except, else, finally, raise

# 1689- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 1690- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 1691- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 1692- raise
x = -1
if x < 0:
    raise ValueError("x cannot be negative")
# Output:
# ValueError: x cannot be negative

# 1693- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 1694- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 1695- Change List Item
numbers[1] = 5

# 1696- Loop Through List Items
for num in numbers:
    print(num)

# 1697- List Comprehension
squares = [x ** 2 for x in numbers]

# 1698- Check if List Item Exists
print(2 in numbers)  # Output: False

# 1699- List Length
print(len(numbers))  # Output: 3

# 1700- Add List Items
numbers.append(4)

# 1701- Remove List Items
# numbers.remove(2)

# 1702- Copy a List
numbers_copy = numbers.copy()

# 1703- Join Two Lists
combined = numbers + squares

# 1704- Tuple Methods
# Examples for count(), index()

# 1705- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 1706- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 1707- Tuple Length
print(len(coordinates))  # Output: 2

# 1708- Tuple With One Item
single_item_tuple = (5,)

# 1709- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 1710- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 1711- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 1712- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 1713- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 1714- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 1715- Set Length
print(len(fruits_set))  # Output: 4

# 1716- Remove Set Items
fruits_set.remove("banana")

# 1717- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 1718- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 1719- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 1720- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 1721- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 1722- Dictionary Length
print(len(person))  # Output: 2

# 1723- Add Dictionary Item
person["city"] = "New York"

# 1724- Remove Dictionary Items
person.pop("age")

# 1725- Copy Dictionary
person_copy = person.copy()

# 1726- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 1727- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 1728- If Indentation
if x > 5:
    print("x is greater than 5")

# 1729- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 1730- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 1731- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 1732- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 1733- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 1734- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 1735- If NOT
if not x > 5:
    print("x is not greater than 5")

# 1736- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 1737- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 1738- While
i = 0
while i < 5:
    print(i)
    i += 1

# 1739- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 1740- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 1741- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 1742- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 1743- Loop Through a String
for char in "Python":
    print(char)

# 1744- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 1745- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 1746- Looping Through a Range
for num in range(5):
    print(num)

# 1747- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 1748- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 1749- For pass
for fruit in fruits:
    pass


# 1750- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 1751- Call a Function
greet("Bob")


# 1752- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 1753- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 1754- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 1755- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 1756- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 1757- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 1758- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 1759- The pass Statement in Functions
def my_function():
    pass


# 1760- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 1761- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 1762- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 1763- Array
# Examples for array.array()

# 1764- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 1765- Access Arrays
print(numbers_array[2])

# 1766- Array Length
print(len(numbers_array))

# 1767- Looping Array Elements
for num in numbers_array:
    print(num)

# 1768- Add Array Element
numbers_array.append(6)

# 1769- Remove Array Element
numbers_array.remove(3)


# 1770- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 1771- Class
# Examples for class definition, instantiation, and methods

# 1772- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1773- The Class init() Function
# See the example above

# 1774- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 1775- self
# Refer to the example above

# 1776- Modify Object Properties
my_dog.age = 4

# 1777- Delete Object Properties
del my_dog.age

# 1778- Delete Object
del my_dog


# 1779- Class pass Statement
class MyClass:
    pass


# 1780- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 1781- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 1782- Create the init() Function
# See the example above

# 1783- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 1784- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 1785- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 1786- Iterators
# Examples for iter() and next()
# 1787- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 1788- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 1789- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 1790- StopIteration
# See the example above

# 1791- Global Scope
global_var = "I am global"


# 1792- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 1793- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 1794- Variables in Modules
# See the example above

# 1795- Renaming a Module
# See the example above

# 1796- Built-in Modules
import math

# 1797- Using the dir() Function
print(dir(math))

# 1798- Import From Module
from math import sqrt

# 1799- Datetime Module
import datetime

# 1800- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 1801- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 1802- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 1803- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 1804- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 1805- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 1806- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 1807- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 1808- RegEx Metacharacters
pattern = r"^The.*fox$"

# 1809- RegEx Special Sequences
pattern = r"\bword\b"

# 1810- RegEx Sets
pattern = r"[aeiou]"

# 1811- RegEx Match Object
pattern = r"\b(\w+)\b"

# 1812- Install PIP
# Instructions to install PIP

# 1813- PIP Packages
# Examples for installing and using packages

# 1814- PIP Remove Package
# Instructions to remove a package

# 1815- Error Handling
# Examples for try, except, else, finally, raise

# 1816- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 1817- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 1818- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 1819- raise
x = -1
if x < 0:
    raise ValueError("x cannot be negative")
# Output:
# ValueError: x cannot be negative

# 1820- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 1821- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 1822- Change List Item
numbers[1] = 5

# 1823- Loop Through List Items
for num in numbers:
    print(num)

# 1824- List Comprehension
squares = [x ** 2 for x in numbers]

# 1825- Check if List Item Exists
print(2 in numbers)  # Output: False

# 1826- List Length
print(len(numbers))  # Output: 3

# 1827- Add List Items
numbers.append(4)

# 1828- Remove List Items
# numbers.remove(2)

# 1829- Copy a List
numbers_copy = numbers.copy()

# 1830- Join Two Lists
combined = numbers + squares

# 1831- Tuple Methods
# Examples for count(), index()

# 1832- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 1833- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 1834- Tuple Length
print(len(coordinates))  # Output: 2

# 1835- Tuple With One Item
single_item_tuple = (5,)

# 1836- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 1837- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 1838- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 1839- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 1840- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 1841- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 1842- Set Length
print(len(fruits_set))  # Output: 4

# 1843- Remove Set Items
fruits_set.remove("banana")

# 1844- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 1845- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 1846- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 1847- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 1848- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 1849- Dictionary Length
print(len(person))  # Output: 2

# 1850- Add Dictionary Item
person["city"] = "New York"

# 1851- Remove Dictionary Items
person.pop("age")

# 1852- Copy Dictionary
person_copy = person.copy()

# 1853- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 1854- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 1855- If Indentation
if x > 5:
    print("x is greater than 5")

# 1856- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 1857- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 1858- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 1859- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 1860- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 1861- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 1862- If NOT
if not x > 5:
    print("x is not greater than 5")

# 1863- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 1864- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 1865- While
i = 0
while i < 5:
    print(i)
    i += 1

# 1866- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 1867- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 1868- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 1869- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 1870- Loop Through a String
for char in "Python":
    print(char)

# 1871- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 1872- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 1873- Looping Through a Range
for num in range(5):
    print(num)

# 1874- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 1875- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 1876- For pass
for fruit in fruits:
    pass


# 1877- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 1878- Call a Function
greet("Bob")


# 1879- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 1880- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 1881- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 1882- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 1883- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 1884- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 1885- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 1886- The pass Statement in Functions
def my_function():
    pass


# 1887- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 1888- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 1889- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 1890- Array
# Examples for array.array()

# 1891- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 1892- Access Arrays
print(numbers_array[2])

# 1893- Array Length
print(len(numbers_array))

# 1894- Looping Array Elements
for num in numbers_array:
    print(num)

# 1895- Add Array Element
numbers_array.append(6)

# 1896- Remove Array Element
numbers_array.remove(3)


# 1897- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 1898- Class
# Examples for class definition, instantiation, and methods

# 1899- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1900- The Class init() Function
# See the example above

# 1901- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 1902- self
# Refer to the example above

# 1903- Modify Object Properties
my_dog.age = 4

# 1904- Delete Object Properties
del my_dog.age

# 1905- Delete Object
del my_dog


# 1906- Class pass Statement
class MyClass:
    pass


# 1907- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 1908- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 1909- Create the init() Function
# See the example above

# 1910- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 1911- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 1912- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 1913- Iterators
# Examples for iter() and next()
# 1914- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 1915- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 1916- Create an Iterator
class MyIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < 5:
            result = self.index
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator()

# 1917- StopIteration
# See the example above

# 1918- Global Scope
global_var = "I am global"


# 1919- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 1920- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 1921- Variables in Modules
# See the example above

# 1922- Renaming a Module
# See the example above

# 1923- Built-in Modules
import math

# 1924- Using the dir() Function
print(dir(math))

# 1925- Import From Module
from math import sqrt

# 1926- Datetime Module
import datetime

# 1927- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 1928- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 1929- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 1930- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 1931- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 1932- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 1933- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 1934- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 1935- RegEx Metacharacters
pattern = r"^The.*fox$"

# 1936- RegEx Special Sequences
pattern = r"\bword\b"

# 1937- RegEx Sets
pattern = r"[aeiou]"

# 1938- RegEx Match Object
pattern = r"\b(\w+)\b"

# 1939- Install PIP
# Instructions to install PIP

# 1940- PIP Packages
# Examples for installing and using packages

# 1941- PIP Remove Package
# Instructions to remove a package

# 1942- Error Handling
# Examples for try, except, else, finally, raise

# 1943- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 1944- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 1945- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 1946- raise
x = -1
if x < 0:
    raise ValueError("x cannot be negative")
# Output:
# ValueError: x cannot be negative

# 1947- List Methods
# Examples for append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 1948- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 1949- Change List Item
numbers[1] = 5

# 1950- Loop Through List Items
for num in numbers:
    print(num)

# 1951- List Comprehension
squares = [x ** 2 for x in numbers]

# 1952- Check if List Item Exists
print(2 in numbers)  # Output: False

# 1953- List Length
print(len(numbers))  # Output: 3

# 1954- Add List Items
numbers.append(4)

# 1955- Remove List Items
# numbers.remove(2)

# 1956- Copy a List
numbers_copy = numbers.copy()

# 1957- Join Two Lists
combined = numbers + squares

# 1958- Tuple Methods
# Examples for count(), index()

# 1959- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 1960- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 1961- Tuple Length
print(len(coordinates))  # Output: 2

# 1962- Tuple With One Item
single_item_tuple = (5,)

# 1963- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 1964- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 1965- Set Methods
# Examples for add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 1966- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 1967- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 1968- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 1969- Set Length
print(len(fruits_set))  # Output: 4

# 1970- Remove Set Items
fruits_set.remove("banana")

# 1971- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 1972- Dictionary Methods
# Examples for keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 1973- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 1974- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 1975- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 1976- Dictionary Length
print(len(person))  # Output: 2

# 1977- Add Dictionary Item
person["city"] = "New York"

# 1978- Remove Dictionary Items
person.pop("age")

# 1979- Copy Dictionary
person_copy = person.copy()

# 1980- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 1981- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 1982- If Indentation
if x > 5:
    print("x is greater than 5")

# 1983- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 1984- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 1985- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 1986- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 1987- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 1988- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 1989- If NOT
if not x > 5:
    print("x is not greater than 5")

# 1990- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 1991- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 1992- While
i = 0
while i < 5:
    print(i)
    i += 1

# 1993- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 1994- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 1995- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 1996- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 1997- Loop Through a String
for char in "Python":
    print(char)

# 1998- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break
