# Open Files

# The built-in method open() is used for file handling. It returns a file object.
# The method takes two arguments: open(file_path, mode)
# File handling is determined by the second argument (mode) passed to the method.

# Open File Modes

# Syntax: open(file_path, mode)
# Modes           Descriptions
# "r"             Read. Used to open a file for reading. Raises an error if the file does not exist.
# "w"             Write. Used to open a file for writing. Creates the file if it does not exist or truncates the file if it exists.
# "a"             Append. Used to open a file for appending. Creates the file if it does not exist.
# "x"             Create. Used to create a file. Raises an error if the file already exists.

import os

# Define file paths
file_path = "06_open_files.txt"
file_path2 = "06_open_files_2.txt"
file_path3 = "06_open_files_3.txt"

# Check if the file exists and delete it
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted successfully.")
else:
    print(f"{file_path} does not exist.")
# Output: 06_open_files.txt does not exist.

# Create and Write to File
with open(file_path, "w") as file:
    file.write("Hello, this is the initial content.")
# Output: # Hello, this is the initial content.


# Read File
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(f"Content of {file_path}:\n{content}")
except FileNotFoundError:
    print(f"{file_path} does not exist.")
# Output: Content of 06_open_files.txt:


# Write to File
with open(file_path, "w") as file:
    file.write("This is new content.")
    print(f"Content of {file_path} overwritten with new content.")
# Output: Content of 06_open_files.txt overwritten with new content.


# Append to File
with open(file_path, "a") as file:
    file.write("\nThis is appended content.")
    print(f"Content of {file_path} appended.")
# Output: Content of 06_open_files.txt appended.


# Create File
try:
    with open(file_path2, "x") as file:
        file.write("This is a newly created file.")
        print(f"{file_path2} created successfully.")
except FileExistsError:
    print(f"{file_path2} already exists. Cannot create the file.")
# Output: [Expected Output Comment]


# Delete File
os.remove(file_path)
print(f"{file_path} deleted successfully.")
# Output: 06_open_files.txt deleted successfully.


# Delete File
os.remove(file_path2)
print(f"{file_path2} deleted successfully.")
# Output: 06_open_files.txt deleted successfully.
