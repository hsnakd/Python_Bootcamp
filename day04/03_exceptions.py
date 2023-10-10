try:
    num = 10 / 0
    print(num)
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('finally block')

print('Test Completed')

# Output:
# Something went wrong
# finally block
# Test Completed

print('---------------------------------------------')

tuple1 = (10, 20, 30, 40)

try:
    print(tuple1[2])
except IndexError:
    print('The index number is too large')
else:
    print('The index number is valid')

# Output:
# 30
# The index number is valid

print('---------------------------------------------')

try:
    raise FileNotFoundError('No such a file')
except SyntaxError:
    print("It is a syntax error")
except OSError as e:
    print('It is an operating system error')
except ArithmeticError:
    print('It is an arithmetic error')
finally:
    print('Finally block')

# Output:
# It is an operating system error
# Finally block

print('---------------------------------------------')


def print_sum(num1, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('Inputs to the print_sum function must be ints')
    print(num1 + num2)


print_sum(1, 2)
# Output: 3

try:
    print_sum(1, 'hi')
except Exception as e:
    print(f'Something went wrong: {e}')

# Output:
# Something went wrong: Inputs to the print_sum function must be ints

print('---------------------------------------------')

raise LookupError('Invalid entry')

# Output:
# Traceback (most recent call last):
#   File "<path-to-script>", line 52, in <module>
#     raise LookupError('Invalid entry')
# LookupError: Invalid entry


"""
Java
    throw: used for manually throwing exception
        public void someMethod() {
            // ...
            if (someCondition) {
                throw new SomeException("This is a custom exception message");
            }
            // ...
        }

    throws: for exception handling (in method signature)
        public void someMethod() throws SomeException, AnotherException {
            // ...
        }

"""
