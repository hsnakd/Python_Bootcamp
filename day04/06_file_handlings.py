import os

# read() : reads the entire content of the file.
path = 'files/Test.txt'
text_file = open(path, 'r')
print(text_file.read())
# Output: Contents of the 'Test.txt' file
# Wooden Spoon
# Python Programming
# Cydeo School

print('----------------------------------')

# readline() reads a single line from the file.
text_file = open(path, 'r')

print(text_file.readline())
# Output: Wooden Spoon

print(text_file.readline())
# Output: Python Programming

print(text_file.readline())
# Output: Python Programming

# close() : is used to close the file. It's a good practice to close the file after you've finished working with it.
text_file.close()



print('----------------------------------')

# Specify the file path
path = 'files/Test2.txt'

# Open the file in write ('w') mode
text_file2 = open(path, 'w')

# Write content to the file
text_file2.write('This is a new text file\nPython created this file')

# Close the file
text_file2.close()

print('----------------------------------')

# Remove the file using os.remove()
os.remove(path)
