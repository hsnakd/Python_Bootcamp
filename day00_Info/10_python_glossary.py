# 1- Indentation
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
x = 5
y = "Hello"

# 5- Variable Names
my_variable = "Hello"

# 6- Assign Values to Multiple Variables
a, b, c = 1, 2, 3

# 7- Output Variables
x = "awesome"
print("Python is " + x)  # Output: Python is awesome

# 8- String Concatenation
a = "Hello"
b = "World"
print(a + " " + b)  # Output: Hello World

# 9- Global Variables
x = "global"


def my_function():
    print("This function is using a " + x)


my_function()  # Output: This function is using a global

# 10- Built-In Data Types
# Examples for int, float, str, list, tuple, set, dict

# 11- Getting Data Type
x = 5
print(type(x))  # Output: <class 'int'>

# 12- Setting Data Type
x = str(5)

# 13- Numbers
# Examples for int, float

# 14- Type Conversion
x = int("5")

# 15- Random Number
import random

print(random.randint(1, 10))

# 16- Specify a Variable Type
x = str("Hello")

# 17- String Literals
single_quote = 'single'
double_quote = "double"
triple_quote = '''triple'''

# 18- Assigning a String to a Variable
greeting = "Hello"

# 19- Multiline Strings
multiline_string = """This is
a multiline
string"""

# 20- Strings are Arrays
s = "Python"
print(s[1])  # Output: y

# 21- Slicing a String
print(s[1:4])  # Output: yth

# 22- Negative Indexing on a String
print(s[-3:-1])  # Output: ho

# 23- String Length
print(len(s))  # Output: 6

# 24- Check In String
print("Py" in s)  # Output: True

# 25- Format String
name = "Alice"
print("Hello, {}".format(name))  # Output: Hello, Alice

# 26- Escape Characters
print("This is a line\nbreak")  # Output: This is a line
#         break

# 27- Boolean Values
is_true = True
is_false = False

# 28- Evaluate Booleans
x = 5
y = 10
print(x > y)  # Output: False


# 29- Return Boolean Value
def is_even(number):
    return number % 2 == 0


print(is_even(4))  # Output: True

# 30- Operators
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
# Examples for [], append(), remove(), pop(), clear(), copy(), extend(), count(), index(), sort(), reverse()

# 39- Access List Items
numbers = [1, 2, 3]
print(numbers[1])  # Output: 2

# 40- Change List Item
numbers[1] = 5

# 41- Loop Through List Items
for num in numbers:
    print(num)

# 42- List Comprehension
squares = [x ** 2 for x in numbers]

# 43- Check if List Item Exists
print(2 in numbers)  # Output: False

# 44- List Length
print(len(numbers))  # Output: 3

# 45- Add List Items
numbers.append(4)

# 46- Remove List Items
# numbers.remove(2)

# 47- Copy a List
numbers_copy = numbers.copy()

# 48- Join Two Lists
combined = numbers + squares

# 49- Tuple
# Examples for (), count(), index()

# 50- Access Tuple Items
coordinates = (3, 4)
print(coordinates[1])  # Output: 4

# 51- Change Tuple Item
# Tuples are immutable, so you can't change individual elements

# 52- Loop List Items
for coord in coordinates:
    print(coord)

# 53- Check if Tuple Item Exists
print(3 in coordinates)  # Output: True

# 54- Tuple Length
print(len(coordinates))  # Output: 2

# 55- Tuple With One Item
single_item_tuple = (5,)

# 56- Remove Tuple Items
# Tuples are immutable, so you can't remove individual elements

# 57- Join Two Tuples
combined_tuple = coordinates + single_item_tuple

# 58- Set
# Examples for {}, add(), remove(), discard(), pop(), clear(), copy(), difference(), union(), intersection(), issubset(), issuperset(), symmetric_difference()

# 59- Access Set Items
fruits_set = {"apple", "banana", "cherry"}
print("apple" in fruits_set)  # Output: True

# 60- Add Set Items
fruits_set.add("orange")

# 61- Loop Set Items
for fruit in fruits_set:
    print(fruit)

# 62- Check if Set Item Exists
print("pear" in fruits_set)  # Output: False

# 63- Set Length
print(len(fruits_set))  # Output: 4

# 64- Remove Set Items
fruits_set.remove("banana")

# 65- Join Two Sets
combined_set = fruits_set.union({"grape", "kiwi"})

# 66- Dictionary
# Examples for {}, keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()

# 67- Access Dictionary Items
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John

# 68- Change Dictionary Item
person["age"] = 31

# 69- Loop Dictionary Items
for key, value in person.items():
    print(f"{key}: {value}")

# 70- Check if Dictionary Item Exists
print("name" in person)  # Output: True

# 71- Dictionary Length
print(len(person))  # Output: 2

# 72- Add Dictionary Item
person["city"] = "New York"

# 73- Remove Dictionary Items
person.pop("age")

# 74- Copy Dictionary
person_copy = person.copy()

# 75- Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# 76- If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 77- If Indentation
if x > 5:
    print("x is greater than 5")

# 78- Elif
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# 79- Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# 80- Shorthand If
print("x is greater than y") if x > y else print("x is not greater than y")

# 81- Shorthand If Else
result = "Even" if x % 2 == 0 else "Odd"

# 82- If AND
if x > 5 and y > 10:
    print("Both conditions are true")

# 83- If OR
if x > 5 or y > 10:
    print("At least one condition is true")

# 84- If NOT
if not x > 5:
    print("x is not greater than 5")

# 85- Nested If
if x > 5:
    if y > 10:
        print("Nested condition is true")

# 86- The pass Keyword in If
if x > y:
    pass
else:
    print("x is not greater than y")

# 87- While
i = 0
while i < 5:
    print(i)
    i += 1

# 88- While Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# 89- While Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 90- While Else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# 91- For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 92- Loop Through a String
for char in "Python":
    print(char)

# 93- For Break
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# 94- For Continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 95- Looping Through a Range
for num in range(5):
    print(num)

# 96- For Else
for fruit in fruits:
    print(fruit)
else:
    print("No more fruits")

# 97- Nested Loops
for fruit in fruits:
    for char in fruit:
        print(char)

# 98- For pass
for fruit in fruits:
    pass


# 99- Function
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")

# 100- Call a Function
greet("Bob")


# 101- Function Arguments
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)


# 102- *args
def add_all(*args):
    return sum(args)


result = add_all(1, 2, 3)


# 103- Keyword Arguments
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet_person(name="Alice", age=25)


# 104- **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30)


# 105- Default Parameter Value
def greet_default(name="User"):
    print(f"Hello, {name}!")


greet_default()

# 106- Passing a List as an Argument
numbers = [1, 2, 3]


def print_numbers(nums):
    for num in nums:
        print(num)


print_numbers(numbers)


# 107- Function Return Value
def multiply(a, b):
    return a * b


result = multiply(4, 5)


# 108- The pass Statement in Functions
def my_function():
    pass


# 109- Function Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

# 110- Lambda Function
multiply = lambda x, y: x * y
result = multiply(3, 4)

# 111- Why Use Lambda Functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 112- Array
# Examples for array.array()

# 113- What is an Array
import array

numbers_array = array.array("i", [1, 2, 3, 4, 5])

# 114- Access Arrays
print(numbers_array[2])

# 115- Array Length
print(len(numbers_array))

# 116- Looping Array Elements
for num in numbers_array:
    print(num)

# 117- Add Array Element
numbers_array.append(6)

# 118- Remove Array Element
numbers_array.remove(3)


# 119- Array Methods
# Methods like extend(), fromlist(), tolist(), etc.

# 120- Class
# Examples for class definition, instantiation, and methods

# 121- Create Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 122- The Class init() Function
# See the example above

# 123- Object Methods
my_dog = Dog("Buddy", 3)
print(my_dog.name)

# 124- self
# Refer to the example above

# 125- Modify Object Properties
my_dog.age = 4

# 126- Delete Object Properties
del my_dog.age

# 127- Delete Object
del my_dog


# 128- Class pass Statement
class MyClass:
    pass


# 129- Create Parent Class
class Animal:
    def __init__(self, name):
        self.name = name


# 130- Create Child Class
class Dog(Animal):
    def bark(self):
        print("Woof!")


# 131- Create the init() Function
# See the example above

# 132- super() Function
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# 133- Add Class Properties
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species


# 134- Add Class Methods
class Fish(Animal):
    def swim(self):
        print("Swimming")


# 135- Iterators
# Examples for iter() and next()
# 136- Iterator vs Iterable
numbers_list = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers_list)

# 137- Loop Through an Iterator
for num in numbers_iter:
    print(num)


# Output:
# 1
# 2
# 3
# 4
# 5

# 138- Create an Iterator
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
# See the example above

# 140- Global Scope
global_var = "I am global"


# 141- Global Keyword
def my_function():
    global global_var
    print(global_var)


my_function()
# Output:
# I am global


# 142- Create a Module
# See the example for creating a Python script and importing functions/classes from it

# 143- Variables in Modules
# See the example above

# 144- Renaming a Module
# See the example above

# 145- Built-in Modules
import math

# 146- Using the dir() Function
print(dir(math))

# 147- Import From Module
from math import sqrt

# 148- Datetime Module
import datetime

# 149- Date Output
today = datetime.date.today()
print(today)  # Output: YYYY-MM-DD

# 150- JSON
# Examples for json.loads(), json.dumps(), json.load(), json.dump()

# 151- Parse JSON
import json

json_data = '{"name": "John", "age": 30}'
python_dict = json.loads(json_data)

# 152- Convert into JSON
python_dict = {"name": "Alice", "age": 25}
json_data = json.dumps(python_dict)

# 153- Format JSON
python_dict = {"name": "Bob", "age": 35}
json_data = json.dumps(python_dict, indent=4)

# 154- Sort JSON
python_dict = {"name": "Charlie", "age": 40}
json_data = json.dumps(python_dict, indent=4, sort_keys=True)

# 155- RegEx Module
# Examples for re.search(), re.findall(), re.sub(), re.split()

# 156- RegEx Functions
import re

text = "The quick brown fox"
result = re.search(r"fox", text)

# 157- Metacharacters in RegEx
pattern = r"^The.*fox$"

# 158- RegEx Special Sequences
pattern = r"\bword\b"

# 159- RegEx Sets
pattern = r"[aeiou]"

# 160- RegEx Match Object
pattern = r"\b(\w+)\b"

# 161- Install PIP
# Instructions to install PIP

# 162- PIP Packages
# Examples for installing and using packages

# 163- PIP Remove Package
# Instructions to remove a package

# 164- Error Handling
# Examples for try, except, else, finally, raise

# 165- Handle Many Exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError):
    print("Type or value error")

# Output:
# Cannot divide by zero


# 166- Try Else
try:
    x = 5
except:
    print("An error occurred")
else:
    print("No error occurred")
# Output:
# No error occurred


# 167- Try Finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
# Output:
# This will always execute


# 168- raise
x = -1
if 2 in numbers:
    numbers.remove(2)
else:
    print("2 is not in the list")
# Output:
# 2 is not in the list
