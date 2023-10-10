"""
# TODO Function

    • Grouping a series of code fragments to perform a task
    • Allows us to reuse the function rather than repeating the same set of statements
    • Improves the re-usability and efficiency of our codes

# TODO Declaring A Function

    • A function must be declared before we call it and use it
    • To create a function, we need to use the def keyword

# TODO Components of Function

    • The def keyword: indicates that the start of the function
    • The function name: Descriptive name of the function
    • The parenthesis: function/method name is always followed by a set of parenthesis, can be capable of receiving arguments

        Python Functions:
        def display_message():
            statement

        Java Methods:
            public static void method(parameter){

            }

"""

import numbers

print('----------- Example - 1 ---------------')


# TODO : Example 1: Basic Function
def display_message():
    print('Hello Cydeo')
    print('Hello World')


display_message()

# Output:
# Hello Cydeo
# Hello World

print(display_message())
# Output:
# Hello Cydeo
# Hello World
# None


print('----------- Example - 2 ---------------')


# TODO : Example 2: Function with Return Value
def value():
    return 'Python Programming'


print(value())

# Output:
# Python Programming

print('----------- Example - 3 ---------------')


# TODO : Example 3: Function with Specified Return Type
def return_int() -> int:
    return 10.0


print(return_int())

# Output:
# 10.0

print('----------- Example - 4 ---------------')


# TODO : Example 4: Function with Parameter
def square(num: int):
    return num * num


print(square(10))

# Output:
# 100

print('----------- Example - 5 ---------------')


# TODO : Example 5: Function with Mixed Type Parameters
def add(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(add(10, 20))
print(add(10.5, 20.5))

# Output:
# 30
# 31.0

print('----------- Example - 6 ---------------')


# TODO : Example 6: Function with Conditional Logic
def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(10, 20, '+'))
print(calculate(100.5, 2.5, '/'))
print(calculate(100, 2.5, '*'))
print(calculate(100.5, 2.5, '-'))

# Output:
# 30
# 40.2
# 250
# 98.0
print('----------- Example - 7 ---------------')


# TODO : Example 7: Method Overloading (Python doesn't natively support method overloading)
def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(10, 20))
print(sum(10, 20, 30))
print(sum(10, 20, 30, 40))

# Output:
# 30
# 60
# 100

print('----------- Example - 8 ---------------')


# TODO : Example 8: Function with Default and Varied Parameters
class Test:
    def method(self):
        pass


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())


concat('Cydeo', 'School')
concat('Python', 3, 2.5)
concat('Python', 3, 2.5, True)
concat('Python', 3, 2.5, True, False)

# Output:
# Cydeo School
# Python 3 2.5
# Python 3 2.5 True
# Python 3 2.5 True False


"""
1. Declaring
2. parameters
3. restricting parameter' data type
4. setting default value to parameter
5. restricting return type

Dynamic Typing
"""


# 1. Declaring: Defining a function and its parameters.
def greet(name):
    print(f"Hello, {name}!")


# Example of declaring a function
greet('James')  # Output: Hello, James!


# 2. Parameters: Variables defined in a function to accept input values.
def add_numbers(x, y):
    return x + y


# Example of parameters
result = add_numbers(5, 7)  # the result is 12


# 3. Restricting Parameter Data Type: Specifying a data type for a parameter.
def multiply(a: int, b: float) -> float:
    return a * b


# Example of restricting a parameter data type
product = multiply(3, 4.5)  # the product is 13.5


# 4. Setting Default Value to Parameter: Providing a default value for a parameter.
def power(base, exponent=2):
    return base ** exponent


# Example of setting default value to parameter
square = power(4)  # square is 16


# 5. Restricting Return Type: Specifying the data type that a function should return.
def square_root(x: float) -> float:
    return x ** 0.5


# Example of restricting a return type
root = square_root(25.0)  # root is 5.0
print(root)

# 6. Dynamic Typing: Variables don't need explicit type declaration.
age = 25  # age is an integer
name = "John"  # name is a string
