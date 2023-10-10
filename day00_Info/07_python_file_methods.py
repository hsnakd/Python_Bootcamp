# FileMethodsExample.py

# Creating a sample text file for demonstration
with open('example.txt', 'w') as file:
    file.write("Hello, this is a sample file.\nSecond line.\nThird line.")

# close(): Closes the file. You can't perform any file operations after closing it.
with open('example.txt', 'r') as file:
    file_content = file.read()
    print(f"Original Content:\n{file_content}")
# Output :
    # Original Content:
    # Hello, this is a sample file.
    # Second line.
    # Third line.

# Note: You can't perform any file operations after closing it.

# fileno(): Returns the file descriptor for the file.
with open('example.txt', 'r') as file:
    file_number = file.fileno()
    print(f"File Number: {file_number}")
# Output:
    # File Number: <file_descriptor>

# flush(): Flushes the write buffer to the file immediately.
with open('example.txt', 'a') as file:
    file.write("\nFourth line.")
    file.flush()

with open('example.txt', 'r') as file:
    updated_content = file.read()
    print(f"Updated Content after flush:\n{updated_content}")
# Output:
    # Updated Content after flush:
    # Hello, this is a sample file.
    # Second line.
    # Third line.
    # Fourth line.

# isatty(): Returns True if the file is associated with a terminal-like device.
with open('example.txt', 'r') as file:
    is_interactive = file.isatty()
    print(f"Is Interactive? {is_interactive}")
# Output:
    # Is Interactive? False

# readable(): Returns True if the file can be read.
with open('example.txt', 'r') as file:
    is_readable = file.readable()
    print(f"Is Readable? {is_readable}")
# Output:
    # Is Readable? True

# readline(): Reads one line from the file.
with open('example.txt', 'r') as file:
    first_line = file.readline()
    print(f"First Line: {first_line}")
# Output:
    # First Line: Hello, this is a sample file.

# readlines(): Reads all lines from the file and returns a list.
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(f"All Lines: {lines}")
# Output:
    # All Lines: ['Hello, this is a sample file.\n', 'Second line.\n', 'Third line.\n', 'Fourth line.']

# seek() and tell(): Move the file cursor and tell the current position.
with open('example.txt', 'r') as file:
    file.seek(7)
    current_position = file.tell()
    print(f"After seeking to position 7, Current Position: {current_position}")
    content_after_seek = file.read()
    print(f"Content after seek:\n{content_after_seek}")
# Output:
    # After seeking to position 7, Current Position: 7
    # Content after seek:
    # this is a sample file.
    # Second line.
    # Third line.
    # Fourth line.

# seekable(): Returns True if the file supports random access (i.e., seek() and tell() are available).
with open('example.txt', 'r') as file:
    is_seekable = file.seekable()
    print(f"Is Seekable? {is_seekable}")
# Output:
    # Is Seekable? True

# truncate(): Resizes the file to the specified size.
with open('example.txt', 'a+') as file:
    file.seek(0, 2)  # Move to the end before truncating
    file.truncate(20)
    file.seek(0)
    truncated_content = file.read()
    print(f"Truncated Content:\n{truncated_content}")
# Output:
    # Truncated Content:
    # Hello, this is a samp

# writable(): Returns True if the file can be written.
with open('file_methods.txt', 'a') as file:
    is_writable = file.writable()
    print(f"Is Writable? {is_writable}")
# Output:
    # Is Writable? True

# write(): Writes a string to the file.
with open('example.txt', 'a') as file:
    file.write("\nFifth line added by write()")

# writelines(): Writes a list of lines to the file.
with open('example.txt', 'a') as file:
    lines_to_write = ["\nSixth line.", "Seventh line."]
    file.writelines(lines_to_write)

# Displaying final content
with open('example.txt', 'r') as file:
    final_content = file.read()
    print(f"Final Content:\n{final_content}")
# Output:
    # Final Content:
    # Hello, this is a sam
    # Fifth line added by write()
    # Sixth line.Seventh line.
