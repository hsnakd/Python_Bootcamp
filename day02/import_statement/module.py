"""
# Import Statement

    • Allows us to reuse the functions/features of one python file (.py) in another
    • We need to import the python file in order to use its properties in other python files
"""

# module.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("This is a module. Run it as a script.")



"""
# Define Alias for Import Statement
    • We can create an alias name by using the as keyword when we import a python file
"""

# main.py
import module as m

message = m.greet("Alice")
print(message)



"""
# From Keyword
    • The "from" keyword allows us to import only parts of python files properties
"""



