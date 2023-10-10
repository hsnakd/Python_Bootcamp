import os

# Text.txt ==> Right Click --> Copy Path/Reference --> Absolute Path
absolute_path = '/Users/HSN/PycharmProjects/Python_BootCamp/day04/files/Test.txt'
# Text.txt ==> Right Click --> Copy Path/Reference --> Path From Content Root
content_root = 'day04/files/Test.txt'

print('--------------read()--------------------')
# "r"             Read. Used to open a file for reading. Raises an error if the file does not exist.

# read() : reads the entire content of the file.
path = 'files/Test.txt'
text_file = open(path, 'r')
print(text_file.read())
# Output: Contents of the 'Test.txt' file
    # Wooden Spoon
    # Python Programming
    # Cydeo School

print('--------------readline()--------------------')

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



print('--------------write()--------------------')
# "w"             Write. Used to open a file for writing. Creates the file if it does not exist or truncates the file if it exists.

# Specify the file path
path = 'files/Test2.txt'

# Open the file in write ('w') mode
text_file2 = open(path, 'w')

# Write content to the file
text_file2.write('This is a new text file\nPython created this file')

text_file2 = open(path, 'r')
print(text_file2.read())
# Output:
    # This is a new text file
    # Python created this file




# Close the file
text_file2.close()

print('--------------remove()--------------------')

# Remove the file using os.remove()
os.remove(path)
print(f"{path} deleted successfully.")
# Output: files/Test2.txt deleted successfully.


print('--------------append()--------------------')

# "a" : Append. Used to open a file for appending. Creates the file if it does not exist.
file_path = 'files/Append.txt'
# Append to File
with open(file_path, "a") as file:
    file.write("\nThis is appended content.")
    print(f"Content of {file_path} appended.")
# Output: Content of files/Append.txt appended.


# Remove the file using os.remove()
os.remove(file_path)


print('--------------create()--------------------')
# "x" : Create. Used to create a file. Raises an error if the file already exists.

# Create File
try:
    with open(file_path, "x") as file:
        file.write("This is a newly created file.")
        print(f"{file_path} created successfully.")
except FileExistsError:
    print(f"{file_path} already exists. Cannot create the file.")
# Output: files/Append.txt created successfully.

# Remove the file using os.remove()
os.remove(file_path)