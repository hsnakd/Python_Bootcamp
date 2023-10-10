# abs(): Returns the absolute value of a number.
abs_value = abs(-5)
print(f"abs(-5) = {abs_value}")  # Output: abs(-5) = 5

# all(): Returns True if all elements of an iterable are true.
all_true = all([True, True, True])
print(f"all([True, True, True]) = {all_true}")  # Output: all([True, True, True]) = True

# any(): Returns True if any element of an iterable is true.
any_true = any([False, True, False])
print(f"any([False, True, False]) = {any_true}")  # Output: any([False, True, False]) = True

# ascii(): Returns a string containing a printable representation of an object.
ascii_str = ascii("Hello, World!")
print(f"ascii('Hello, World!') = {ascii_str}")  # Output: ascii('Hello, World!') = 'Hello, World!'

# bin(): Converts an integer to a binary string.
binary_num = bin(10)
print(f"bin(10) = {binary_num}")  # Output: bin(10) = '0b1010'

# bool(): Converts a value to a Boolean.
bool_value = bool(0)
print(f"bool(0) = {bool_value}")  # Output: bool(0) = False

# bytearray(): Returns a bytearray object from a given iterable of numbers.
byte_array = bytearray([65, 66, 67])
print(f"bytearray([65, 66, 67]) = {byte_array}")  # Output: bytearray([65, 66, 67]) = bytearray(b'ABC')

# bytes(): Returns a bytes object.
bytes_obj = bytes([65, 66, 67])
print(f"bytes([65, 66, 67]) = {bytes_obj}")  # Output: bytes([65, 66, 67]) = b'ABC'

# callable(): Returns True if the object appears callable.
is_callable = callable(print)
print(f"callable(print) = {is_callable}")  # Output: callable(print) = True

# chr(): Returns a string representing a character whose Unicode code point is the integer.
char = chr(65)
print(f"chr(65) = {char}")  # Output: chr(65) = 'A'


# classmethod(): Converts a method into a class method.
class MyClass:
    @classmethod
    def my_method(cls):
        print("Class method called")


MyClass.my_method()  # Output: Class method called

# compile(): Compiles a source string into a code or AST object.
code = compile("print('Hello, compiled code!')", "", "exec")
exec(code)  # Output: Hello, compiled code!

# complex(): Returns a complex number with the specified real and imaginary parts.
complex_num = complex(1, 2)
print(f"complex(1, 2) = {complex_num}")  # Output: complex(1, 2) = (1+2j)


# delattr(): Deletes an attribute from an object.
class Example:
    def __init__(self):
        self.value = 42


obj = Example()
print(obj.value)  # Output: 42
delattr(obj, 'value')
# print(obj.value)  # Output: AttributeError (commented out to avoid an error)

# dict(): Returns a new dictionary with the specified keys and values.
dictionary = dict(name='John', age=30)
print(f"dict(name='John', age=30) = {dictionary}")  # Output: dict(name='John', age=30) = {'name': 'John', 'age': 30}

# dir(): Returns a list of names in the current local scope or a list of attributes of an object.
dir_list = dir(dictionary)
print(f"dir(dictionary) = {dir_list}")  # Output: dir(dictionary) = ['age', 'name']

# divmod(): Returns a pair of numbers (a tuple) consisting of their quotient and remainder.
quotient, remainder = divmod(9, 4)
print(
    f"divmod(9, 4) = Quotient: {quotient}, Remainder: {remainder}")  # Output: divmod(9, 4) = Quotient: 2, Remainder: 1

# enumerate(): Returns an enumerate object, containing pairs of index and element.
enum_obj = enumerate(['apple', 'banana', 'cherry'])
enum_list = list(enum_obj)
print(
    f"enumerate(['apple', 'banana', 'cherry']) = {enum_list}")  # Output: enumerate(['apple', 'banana', 'cherry']) = [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# eval(): Evaluates a Python expression and returns the result.
result = eval("2 + 3")
print(f"eval('2 + 3') = {result}")  # Output: eval('2 + 3') = 5

# exec(): Executes a dynamically created program, which is either a string or object code.
exec("print('Hello from exec!')")  # Output: Hello from exec!


# filter(): Constructs an iterator from elements of an iterable for which a function returns true.
def is_even(x):
    return x % 2 == 0


filtered_list = list(filter(is_even, [1, 2, 3, 4, 5]))
print(f"filter(is_even, [1, 2, 3, 4, 5]) = {filtered_list}")  # Output: filter(is_even, [1, 2, 3, 4, 5]) = [2, 4]

# float(): Returns a floating-point number from a number or a string.
float_num = float("3.14")
print(f"float('3.14') = {float_num}")  # Output: float('3.14') = 3.14

# format(): Formats a specified value using a specified format.
formatted_str = format(0.5, '%')
print(f"format(0.5, '%') = {formatted_str}")  # Output: format(0.5, '%') = '50.000000%'

# frozenset(): Returns an immutable frozenset object.
frozen_set = frozenset([1, 2, 3])
print(f"frozenset([1, 2, 3]) = {frozen_set}")  # Output: frozenset([1, 2, 3]) = frozenset({1, 2, 3})


# getattr(): Returns the value of a named attribute of an object.
class Person:
    def __init__(self, name):
        self.name = name


person = Person("Alice")
name_value = getattr(person, 'name')
print(f"getattr(person, 'name') = {name_value}")  # Output: getattr(person, 'name') = Alice

# globals(): Returns a dictionary representing the current global symbol table.
global_symbols = globals()
print(f"globals() = {global_symbols}")  # Output: globals() = {...}

# hasattr(): Returns True if the object has the given named attribute, False otherwise.
has_attribute = hasattr(person, 'age')
print(f"hasattr(person, 'age') = {has_attribute}")  # Output: hasattr(person, 'age') = False

# hash(): Returns the hash value of an object if it has one.
hash_value = hash("Hello, hash!")
print(f"hash('Hello, hash!') = {hash_value}")  # Output: hash('Hello, hash!') = -3673643349208231779

# help(): Invokes the built-in help system.
# Uncomment the next line to see the built-in help system in action
# help(print)

# hex(): Converts an integer to a lowercase hexadecimal string.
hex_value = hex(255)
print(f"hex(255) = {hex_value}")  # Output: hex(255) = '0xff'

# id(): Returns the identity of an object.
id_value = id(person)
print(f"id(person) = {id_value}")  # Output: id(person) = <some number>

# input(): Reads a line from input and returns it as a string.
# Uncomment the next line to take user input
# user_input = input("Enter something: ")
# print(f"You entered: {user_input}")

# int(): Returns an integer object from a number or a string.
int_value = int("42")
print(f"int('42') = {int_value}")  # Output: int('42') = 42

# isinstance(): Returns True if the object is an instance of the specified type(s).
is_instance = isinstance(person, Person)
print(f"isinstance(person, Person) = {is_instance}")  # Output: isinstance(person, Person) = True

# issubclass(): Returns True if a class is a subclass of a specified class.
is_subclass = issubclass(type(person), object)
print(f"issubclass(type(person), object) = {is_subclass}")  # Output: issubclass(type(person), object) = True

# iter(): Returns an iterator object for an iterable.
iter_obj = iter([1, 2, 3])
next_value = next(iter_obj)
print(f"iter([1, 2, 3]), next(iter_obj) = {next_value}")  # Output: iter([1, 2, 3]), next(iter_obj) = 1

# len(): Returns the number of items in an object (length).
length = len([1, 2, 3])
print(f"len([1, 2, 3]) = {length}")  # Output: len([1, 2, 3]) = 3

# list(): Returns a list from the given iterable.
list_from_tuple = list((1, 2, 3))
print(f"list((1, 2, 3)) = {list_from_tuple}")  # Output: list((1, 2, 3)) = [1, 2, 3]

# locals(): Updates and returns a dictionary representing the current local symbol table.
local_symbols = locals()
print(f"locals() = {local_symbols}")  # Output: locals() = {...}


# map(): Applies a function to all items in an input list (or any iterable) and returns an iterator.
def square(x):
    return x ** 2


squared_list = list(map(square, [1, 2, 3]))
print(f"map(square, [1, 2, 3]) = {squared_list}")  # Output: map(square, [1, 2, 3]) = [1, 4, 9]

# max(): Returns the largest item in an iterable or the largest of two or more arguments.
max_value = max([1, 2, 3, 4, 5])
print(f"max([1, 2, 3, 4, 5]) = {max_value}")  # Output: max([1, 2, 3, 4, 5]) = 5

# memoryview(): Returns a memory view object of the given argument.
memory_view = memoryview(b"Hello")
print(f"memoryview(b'Hello') = {memory_view}")  # Output: memoryview(b'Hello') = <memory at ...>

# min(): Returns the smallest item in an iterable or the smallest of two or more arguments.
min_value = min([1, 2, 3, 4, 5])
print(f"min([1, 2, 3, 4, 5]) = {min_value}")  # Output: min([1, 2, 3, 4, 5]) = 1

# next(): Retrieves the next item from the iterator by calling its __next__() method.
next_value = next(iter([1, 2, 3]))
print(f"next(iter([1, 2, 3])) = {next_value}")  # Output: next(iter([1, 2, 3])) = 1

# object(): Returns a new featureless object (a new instance of the object class).
new_object = object()
print(f"object() = {new_object}")  # Output: object() = <object object at ...>

# oct(): Converts an integer to an octal string.
octal_value = oct(8)
print(f"oct(8) = {octal_value}")  # Output: oct(8) = '0o10'

# open(): Opens a file and returns a corresponding file object.
# Uncomment the next lines to demonstrate file handling
# with open('example.txt', 'w') as file:
#     file.write('Hello, file!')
# with open('example.txt', 'r') as file:
#     file_content = file.read()
#     print(f"open('example.txt', 'r') = {file_content}")

# ord(): Returns an integer representing the Unicode character.
unicode_value = ord('A')
print(f"ord('A') = {unicode_value}")  # Output: ord('A') = 65

# pow(): Returns the value of x to the power of y.
power_value = pow(2, 3)
print(f"pow(2, 3) = {power_value}")  # Output: pow(2, 3) = 8

# print(): Prints the specified message to the screen.
print("Hello, print!")  # Output: Hello, print!


# property(): Gets, sets, or deletes a property of an object.
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height


rect = Rectangle(4, 5)
print(f"rect.area = {rect.area}")  # Output: rect.area = 20

# range(): Returns an object with numbers from start (inclusive) to stop (exclusive) by step.
range_sequence = list(range(5))
print(f"range(5) = {range_sequence}")  # Output: range(5) = [0, 1, 2, 3, 4]

# repr(): Returns a string containing a printable representation of an object.
repr_str = repr("Hello, repr!")
print(f"repr('Hello, repr!') = {repr_str}")  # Output: repr('Hello, repr!') = "'Hello, repr!'"

# reversed(): Returns a reversed iterator of a sequence.
reversed_list = list(reversed([1, 2, 3]))
print(f"reversed([1, 2, 3]) = {reversed_list}")  # Output: reversed([1, 2, 3]) = [3, 2, 1]

# round(): Returns a floating-point number rounded to the specified number of decimals.
rounded_num = round(3.14159, 2)
print(f"round(3.14159, 2) = {rounded_num}")  # Output: round(3.14159, 2) = 3.14

# set(): Returns a new set object, optionally with elements taken from an iterable.
set_from_list = set([1, 2, 3, 3, 4])
print(f"set([1, 2, 3, 3, 4]) = {set_from_list}")  # Output: set([1, 2, 3, 3, 4]) = {1, 2, 3, 4}

# setattr(): Sets the value of a named attribute of an object.
setattr(rect, '_width', 6)
print(f"setattr(rect, '_width', 6), rect.area = {rect.area}")  # Output: setattr(rect, '_width', 6), rect.area = 30

# slice(): Returns a slice object representing the set of indices specified by range(start, stop, step).
sliced_list = [1, 2, 3, 4, 5][1:4]
print(f"[1, 2, 3, 4, 5][1:4] = {sliced_list}")  # Output: [1, 2, 3, 4, 5][1:4] = [2, 3, 4]

# sorted(): Returns a sorted list from the specified iterable.
sorted_list = sorted([3, 1, 4, 1, 5, 9, 2])
print(f"sorted([3, 1, 4, 1, 5, 9, 2]) = {sorted_list}")  # Output: sorted([3, 1, 4, 1, 5, 9, 2]) = [1, 1, 2, 3, 4, 5, 9]


# staticmethod(): Returns a static method for a function.
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y


result = MathOperations.add(3, 4)
print(f"MathOperations.add(3, 4) = {result}")  # Output: MathOperations.add(3, 4) = 7

# str(): Returns a string version of an object.
str_value = str(42)
print(f"str(42) = {str_value}")  # Output: str(42) = '42'

# sum(): Sums the items of an iterable from left to right and returns the total.
sum_result = sum([1, 2, 3, 4, 5])
print(f"sum([1, 2, 3, 4, 5]) = {sum_result}")  # Output: sum([1, 2, 3, 4, 5]) = 15


# super(): Returns a temporary object of the superclass, allowing access to its methods.
class ChildRectangle(Rectangle):
    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color


child_rect = ChildRectangle(2, 3, 'red')
print(f"child_rect.area = {child_rect.area}")  # Output: child_rect.area = 6

# tuple(): Returns a tuple from the given iterable.
tuple_from_list = tuple([1, 2, 3])
print(f"tuple([1, 2, 3]) = {tuple_from_list}")  # Output: tuple([1, 2, 3]) = (1, 2, 3)

# type(): Returns the type of an object or creates a new type object.
type_of_object = type("Hello, type!")
print(f"type('Hello, type!') = {type_of_object}")  # Output: type('Hello, type!') = <class 'str'>

# vars(): Returns the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
vars_dict = vars(rect)
print(f"vars(rect) = {vars_dict}")  # Output: vars(rect) = {'_width': 6, '_height': 5}

# zip(): Returns an iterator of tuples, where the first item in each passed iterator is paired together.
zipped_iter = zip([1, 2, 3], ['a', 'b', 'c'])
zipped_list = list(zipped_iter)
print(
    f"zip([1, 2, 3], ['a', 'b', 'c']) = {zipped_list}")  # Output: zip([1, 2, 3], ['a', 'b', 'c']) = [(1, 'a'), (2, 'b'), (3, 'c')]
