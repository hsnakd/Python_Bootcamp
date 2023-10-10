"""

# TODO: Break Statement

    • Causes the termination of the loop
    • Tells the interpreter to go on to the next statement of code outside of the loop

# TODO: Continue Statement

    • Skips the current iteration of the loop
    • Tells the interpreter to jump to the next iteration

# TODO: Pass Statement

    • Used as a placeholder in a loop/function/class
    • Nothing happens when the pass is executed
    • Results in no operation

"""


for i in range(1, 6):
    print(i)
    if i == 3:
        break  # exits the loop

# Output:
# 1
# 2
# 3
# (Loop exits)

print('-------------')

for i in range(1, 6):
    if i == 3 or i == 4:
        continue  # skips to the next iteration
    print(i)

# Output:
# 1
# 2
# 5
# (Skips printing 3 and 4)

print('-------------')

for i in range(1, 6):
    if i == 3 or i == 4:
        pass  # doesn't do anything in this context ==> Used as a placeholder in a loop/function/class
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

def function():
    pass

if True:
    pass

class Class:

    def method(self):
        pass

    pass
