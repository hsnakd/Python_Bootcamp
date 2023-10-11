# json.dump() Method:
    # The json.dump() method is used to serialize Python objects into a JSON formatted string and write it to a file-like object (such as a file).
    # It takes two main parameters:
    # obj: The Python object to be serialized.
    # fp: A file-like object (e.g., a file or a io.StringIO object) where the serialized JSON string will be written.


import json
import os

data = {'name': 'John', 'age': 30, 'city': 'New York'}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# In this example, the dictionary data is serialized and written to a file named 'data.json'.

# json.load() Method:
    # The json.load() method is used to deserialize a JSON document from a file-like object and convert it back to a Python object.
    # It takes one parameter:
    # fp: A file-like object (e.g., a file or a io.StringIO object) containing a JSON document.


# import json

with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)

print(loaded_data)
# Output:
    # {'name': 'John', 'age': 30, 'city': 'New York'}

# In this example, the content of the 'data.json' file is loaded and converted back into a Python object (loaded_data).
# These methods make it easy to save Python data structures to a file in a JSON format and then later load that data back into a Python program.

# Remove the file using os.remove()
os.remove('data.json')
print(f"{'data.json'} deleted successfully.")