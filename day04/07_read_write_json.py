import json

# Read data from Test.json
file_path = 'files/Test.json'
with open(file_path, 'r') as json_file:
    data_dict = json.load(json_file)

# Print the loaded dictionary
print(data_dict)
# Output:
    # {'name': 'John Doe', 'age': 43, 'address': {'street': '10 Downing Street', 'city': 'London'}, 'phones': ['+44 1234567', '+44 2345678']}

# Print the type of the loaded dictionary
print(type(data_dict))
# Output: <class 'dict'>

# Print keys of the dictionary
for key in data_dict.keys():
    print(key)
# Output:
    # name
    # age
    # address
    # phones

# Modify data in the dictionary
data_dict['name'] = 'Aaron King'
data_dict['age'] = 45

# Print the modified dictionary
print(data_dict)
# Output:
    # {'name': 'Aaron King', 'age': 45, 'address': {'street': '10 Downing Street', 'city': 'London'}, 'phones': ['+44 1234567', '+44 2345678']}

# Close the initial file
json_file.close()

# Write data to Test2.json
output_file_path = 'files/Test2.json'
with open(output_file_path, 'w') as json_file2:
    # Convert dictionary to JSON string with indentation
    json_object = json.dumps(data_dict, indent=3) # indent parameter ensures that the content in the file is formatted with an indentation of number (3) of spaces.

    # Write the JSON string to the file
    json_file2.write(json_object)

# Print a message indicating that the JSON file has been written
print('------------ Write Json file----------------------')

# Define a dictionary of students
students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Math', 'Physics']
    },
    'A02': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subjects': ['Biology', 'Programming']
    },
    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subjects': ['Chemistry', 'Programming']
    }
}

# Write the students dictionary to Test2.json with indentation
with open(output_file_path, 'w') as json_file:
    json_object = json.dumps(students, indent=3)
    json_file.write(json_object)

# Print the JSON representation of the students dictionary
print(json_object)
# Output:
    # {
    #    "A01": {
    #       "name": "James",
    #       "gender": "Male",
    #       "gpa": 3.5,
    #       "subjects": [
    #          "Math",
    #          "Physics"
    #       ]
    #    },
    #    "A02": {
    #       "name": "Hazel",
    #       "gender": "Female",
    #       "gpa": 3.8,
    #       "subjects": [
    #          "Biology",
    #          "Programming"
    #       ]
    #    },
    #    "A03": {
    #       "name": "Yulia",
    #       "gender": "Female",
    #       "gpa": 4,
    #       "subjects": [
    #          "Chemistry",
    #          "Programming"
    #       ]
    #    }
    # }