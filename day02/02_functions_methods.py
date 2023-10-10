"""
In Python, both functions and methods are blocks of reusable code, but there are subtle differences between them:

# Definition:
    Function: A function is a block of code that performs a specific task and is defined using the def keyword.
    Method: A method is a function that belongs to an object. It is called on an object and can access the data within that object.

# Invocation:
    Function: Functions are called by their names.
    Method: Methods are called on objects using the dot notation (object.method()).

# Scope:
    Function: Functions are standalone blocks of code and can be defined independently of any class or object.
    Method: Methods are associated with objects or classes and operate on the data within them.

# First Parameter (usually):
    Function: The first parameter is typically the data the function operates on.
    Method: The first parameter is usually the instance itself (self in the case of instance methods).

"""


# Here's a simple example to illustrate the difference:

# TODO : Function
def square(x):
    return x ** 2


result = square(5)  # Function call
print(result)           # Output : 25


# TODO : Method
class MathOperations:
    def square(self, x):
        return x ** 2


math_obj = MathOperations()
result = math_obj.square(5)  # Method call
print(result)           # Output : 25

"""

In this example, square is a function, and square within the MathOperations class is a method. The function is called directly, while the method is called on an instance of the class.

In Python, the distinction between functions and methods is not always strict, and the terms are sometimes used interchangeably. It's essential to understand the context in which they are used.

"""