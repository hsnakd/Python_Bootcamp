"""
# TODO Arithmetic Operators

    NAME                OPERATOR        PURPOSE & NOTES                                 EXAMPLE         RESULT
    ADDITION            +               Adds one value to another                       10+5            15
    SUBTRACTION         -               Subtracts one value from another                10-5            5
    DIVISION            /               Divides two values                              10/5            2
    MULTIPLICATION      *               Multiplies two values                           10*5            50
    MODULUS             %               Divides two values and returns the remainder    10%3            1

"""

# arithmetic: +, -, *, /, %

print(10 - 2)  # 8
print(10 + 2)  # 12

print(10 * 3)  # 30

# ('/' operator always returns float number)
print(10 / 3)  # 3.3333333333333335
print(10 / 2)  # 5.0

print(10 % 3)  # 1

# integer casting
print(int(100 / 2))  # 50

print('-----------------------------------------------------------------')

"""
# Shorthand Operators
    =, +=, -=, *=, /=, %=

    NAME                            SHORTHAND OPERATOR          MEANING
    Assignment                      x = y                       x = y
    Addition Assignment             x += y                      x = x + y
    Subtraction Assignment          x -= y                      x = x – y
    Multiplication Assignment       x *= y                      x = x * y
    Division Assignment             x /= y                      x = x / y
    Remainder Assignment            x %= y                      x = x % y

"""

a = 100
a = 200
print(a)  # 200

a += 100
print(a)  # 300

a -= 50
print(a)  # 250

a /= 2
print(a)  # 125.0

print('-----------------------------------------------------------------')

"""
# Logical Operators
        OPERATOR        DESCRIPTION
        and             Logical AND
        or              Logical OR
        not             Logical NOT
        
# Membership Operators
        OPERATOR        DESCRIPTION
        in              Returns true if the specified value is presented in the object
        not in          Returns true if the specified value is not presented in the object      
        
# Identity Operators
        OPERATOR            DESCRIPTION

        is                  Returns true if both operands are the same object (equal operator in Java)
        is not              Returns true if both operands are not the same object   
"""

# logical operators: and, or, not
s = 'Hello World'

print('H' and 'W' in s)  # True

print(True and True)  # True
print(True or False)  # True
print(False or False)  # False

# True is False
result1 = True is False
print(result1)  # Output: False

# True is not False
result2 = True is not False
print(result2)  # Output: True

# and operator
result_and = True and False
print(result_and)  # Output: False

# or operator
result_or = True or False
print(result_or)  # Output: True

# not operator
result_not = not False
print(result_not)  # Output: True


s = 'Java Python C# C++'

print('Java' or 'Ruby' in s)        # Java      ?????
print('Java' or 'Python' in s)      # Java      ?????
print('Ruby' or 'Python' in s)      # Ruby      ?????
print('Ruby' or 'Cypress' in s)     # Ruby      ?????

# Example 1
x = 5
y = 10

if x > 7 or y < 20:
    print("At least one condition is True")

# Output: At least one condition is True

# Example 2
age = 25

if age < 18 or age > 65:
    print("You qualify for a special discount")

# Output: You qualify for a special discount

# Example 3
name = "Alice"

if name == "Alice" or name == "Bob":
    print("Hello, Alice or Bob!")

# Output: Hello, Alice or Bob!

print('-----------------------------------------------------------------')

"""
# Relational Operators
        OPERATOR        DESCRIPTION
        >               Greater than
        >=              Greater than or equal
        <               Less than
        <=              Less than or equal
        ==              Equal               (In Python, equal operator (==) it used as the equals() method in Java )
        !=              Not equal
"""
age = 29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'
print(f'is_eligible : {is_eligible}')

age2 = 5
citizen_ship2 = 'USA'
is_eligible2 = age2 >= 18 or citizen_ship2 == 'USA'
print(f'is_eligible2 : {is_eligible2}')

pl = 'Java Python C# C++'

# contains()
has_java = 'Java' in pl
print(has_java)  # True

has_cypress = 'Cypress' in pl
print(has_cypress)  # False

# !contains()
print('Python' not in pl)

print(not False)
print(not True)  # !

print('-----------------------------------------------------------------')

s = 'Java'
s2 = 'Java'

print(s == s2)  # True
print(s is s2)  # True ==> to heck if two variables are referencing to the same objects ( == operator of java)

# Equality Operator
result1 = 10 == 10  # True because 10 is equal to 10
print(result1)

result2 = 10 == "10"  # False because the types are different (int vs string)
print(result2)

# Greater than
result3 = 10 > 20  # False because 10 is not greater than 20
print(result3)

# Inequality
result4 = 10 != 20  # True because 10 is not equal to 20
print(result4)

# Greater than or equal to
result5 = (2 + 3) >= (4 + 1)  # True because (2 + 3) is equal to (4 + 1)
print(result5)
