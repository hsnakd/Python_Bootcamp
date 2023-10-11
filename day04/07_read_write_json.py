
"""
{
    "name": "John Doe",
    "age": 43,
    "address": {
        "street": "10 Downing Street",
        "city": "London"
    },
    "phones": [
        "+44 1234567",
        "+44 2345678"
    ]
}

"""

import json

path = 'files/Test.json'

json_file = open(path, 'r')

dictionary = json.load(json_file)

print(dictionary)
# Output: {'name': 'John Doe', 'age': 43, 'address': {'street': '10 Downing Street', 'city': 'London'}, 'phones': ['+44 1234567', '+44 2345678']}

print(type(dictionary))
# Output: <class 'dict'>

for x in dict(dictionary).keys():
    print(x)
# Output:
    # name
    # age
    # address
    # phones


dictionary['name'] = 'Aaron King'
dictionary['age'] = 45
print(dictionary)
# Output:
    # {'name': 'Aaron King', 'age': 45, 'address': {'street': '10 Downing Street', 'city': 'London'}, 'phones': ['+44 1234567', '+44 2345678']}


json_file.close()


json_file2 = open('files/Test2.json', 'w')
print(json.dumps(dictionary))
json_object = json.dumps(dictionary)

json_file2.write(json_object)

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

print(json_object)
# Object:
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
