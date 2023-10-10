"""
# User Input

    • We can ask the user for input by using the input() method
    • It waits until the user provides input and returns it as a string
"""

"""
# print(  help(input)  )

        input(prompt='', /)
            Read a string from standard input.  The trailing newline is stripped.
            
            The prompt string, if given, is printed to standard output without a
            trailing newline before reading input.
            
            If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
            On *nix systems, readline is used if available.
        
        None

"""


name = input('Enter your name:\n')              # default str
age = int(input('Enter your age:\n'))
gpa = float(input('Enter your gpa:\n'))
boolean_value = bool(input('Enter True or False:\n'))

print(name)
print( type(name) )

print()

print( age )
print( type(age) )

print()

print(gpa)
print( type(gpa))

print()

print(boolean_value)
print( type(boolean_value))
