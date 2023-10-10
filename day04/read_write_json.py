import json

path = 'files/Test.json'

json_file = open(path, 'r')

dictionary = json.load(json_file)

print(dictionary)
# Output: Contents of the 'Test.json' file as a dictionary
print(type(dictionary))
# Output: <class 'dict'>

for x in dict(dictionary).keys():
    print(x)

json_file.close()

# Output: Keys of the dictionary

print('------------ Write Json file----------------------')

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

json_file = open('files/Test2.json', 'w')

json_object = json.dumps(students, indent=3)

json_file.write(json_object)

# Output: The 'Test2.json' file is created with the JSON representation of the 'students' dictionary.

"""
Web Automation:
    BeautifulSoup4
    request
    pytest
    robot

Web Development:
    Django
    FastAPI
    flask
    ...
"""
