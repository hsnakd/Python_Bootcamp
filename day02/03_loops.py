s = 'Python Programming'

# Iterate over each character in the string and print it
for each in s:
    print(each)

# Output:
# P
# y
# t
# h
# o
# n
# (and so on)

print('-----------------------')

# Print each character using indexing
for i in range(0, len(s)):
    print(s[i])

# Output:
# P
# y
# t
# h
# o
# n
# (and so on)

print('-----------------------')

# Print each character in reverse using negative indexing
for i in range(-len(s), 0):
    print(s[i])

# Output:
# P
# y
# t
# h
# o
# n
# (and so on)

print('-----------------------')

# Print each character in reverse using reversed and range
for i in reversed(range(0, len(s))):
    print(s[i])

# Output:
# g
# n
# i
# m
# m
# a
# r
# g
# o
# r
# P
# (and so on)

print('-----------------------')

# Reverse the string and print
result = ''
for x in s[::-1]:
    result += x
print(result)

# Output:
# gnimmargorP nohtyP

print('-----------------------')

# Print "Hello World" 10 times
for x in range(1, 11):
    print('Hello World')

# Output:
# Hello World
# Hello World
# Hello World
# (and so on seven times)

print('-----------------------')

# Take a positive number as input and ensure it's positive
num = int(input('Enter a positive number:\n'))
while num <= 0:
    num = int(input('Enter a positive number:\n'))
print(f'You have entered {num}')

# Output:
# Enter a positive number:
# (User input)
# (If the input is not positive, it will prompt again)
# You have entered (user input)

print('-----------------------')

# Take "yes" or "no" as input and ensure it's one of them
answer = input('Enter yes or no:\n')
while not (answer.lower() == 'yes' or answer.lower() == 'no'):
    answer = input('Enter yes or no:\n')
print(f'You have entered {answer}')

# Output:
# Enter yes or no:
# (User input)
# (If the input is neither 'yes' nor 'no', it will prompt again)
# You have entered (user input)
