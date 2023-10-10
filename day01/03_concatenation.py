"""
# TODO Concatenation with + operator (nor recommended in python)

    • The action of linking two strings together
    • The two values on both right and left side of the + operator must be strings
"""


name = 'James'
age = 26

print('My name is ' + name)
# print('My age is' + age) # it gives error ==> IndentationError: unexpected indent



"""
# Concatenation with {} operator
    • The action of linking string and other types together
    • The format() need to be called in order to pass different types into a string, it can easily be done by adding the character f before the opening double quote of the string
"""


print('My age is ' + str(age))
print('My age is {}'.format(age))

print('My name is {} and I am {} years old'.format(name, age))
print(f'My name is {name} and I am {age} years old')

print('Python', 3, 'is awesome :', True)