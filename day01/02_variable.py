"""
In Java: Static Typing
    DataType var = Data

In Python: Dynamic Typing
    var = Data

# TODO Variable

    • Improves the re-usability of the data
    • Variables must be declared before use
    • The Value stored in a variable can be changed during the program execution

                        Python – Data Types

       * Numeric                    * Boolean            * Set            * Dictionary           * Sequence

        - Complex Number                                                                            - Tuple
        - Integer                                                                                   - List
        - Float                                                                                     - String


"""

name = None
print(name)

print()

name = 'James'
print(name)
print(type(name))           # <class 'str'>

print()

age = 25
print(age)
print(type(age))            # <class 'int'>

print()

gpa = 3.5
print(gpa)
print(type(gpa))            # <class 'float'>

is_employed = True
print(is_employed)
print(type(is_employed))    # <class 'bool'>

print('--------------------------------------------------')


"""
# Type Casting
    * Casting is done by using constructor functions:
    * Allows us to convert one type of value to another type
        • int(): constructs an integer number from a literal (int, float, or string literals)
        • float(): constructs a float number from a literal (int, or float, or string literals)
        • str(): constructs a string from a literal (int, float, or string literals)
"""

n = 25
print(n * 5)        # 125

s = str(n)
print(s * 5)        # 2525252525


s = '25'
print(s * 5)        # 2525252525

# str(s)
s = int(s)
print(s * 5)        # 125