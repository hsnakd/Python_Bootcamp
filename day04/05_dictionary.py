employee0 = {'name': 'Jack', 'age': 39, 'salary': 100_000}
print(employee0)  # Output: {'name': 'Jack', 'age': 39, 'salary': 100000}

employee1 = {}

employee1['name'] = 'James'
employee1['name'] = 'Daniel'
employee1['age'] = 45
employee1['salary'] = 60_000

print(employee1)  # Output: {'name': 'Daniel', 'age': 45, 'salary': 60000}

employee2 = {
    'name': 'James',
    'age': 29,
    'salary': 80_000,
    'full_time': False
}

print(employee2)  # Output: {'name': 'James', 'age': 29, 'salary': 80000, 'full_time': False}

print(employee2['name'])  # Output: James

employee2['salary'] += 10000
print(employee2)  # Output: {'name': 'James', 'age': 29, 'salary': 90000, 'full_time': False}

# update()
employee2.update({'age': 40})
print(employee2)  # Output: {'name': 'James', 'age': 40, 'salary': 90000, 'full_time': False}

employee2['full_time'] = True
print(employee2)  # Output: {'name': 'James', 'age': 40, 'salary': 90000, 'full_time': True}

employee2.update({'salary': 95000})
print(employee2)  # Output: {'name': 'James', 'age': 40, 'salary': 95000, 'full_time': True}

# pop()
employee2.pop('full_time')
print(employee2)  # Output: {'name': 'James', 'age': 40, 'salary': 90000}

# popitem()
employee2.popitem()
print(employee2)  # Output: {'name': 'James', 'age': 40}

# copy()
l = employee2.copy()
print(employee2)  # Output: {'name': 'James', 'age': 40}
print(l)  # Output: {'name': 'James', 'age': 40}

print(employee2 is l)  # Output: False

print('--------- Iterating Dictionary -----------------')

employee3 = {
    'name': 'Shay',
    'age': 29,
    'salary': 110_000,
    'full_time': False,
    'job_title': 'Developer',
    'company': 'Apple Inc'
}
print('---------------------------------------------')

print(employee3.keys())  # Output: dict_keys(['name', 'age', 'salary', 'full_time', 'job_title', 'company'])
print(list(employee3.keys()))  # Output: ['name', 'age', 'salary', 'full_time', 'job_title', 'company']

print('---------------------------------------------')

for key in employee3.keys():
    print(f'{key} : {employee3[key]}')
# Output:
# name : Shay
# age : 29
# salary : 110000
# full_time : False
# job_title : Developer
# company : Apple Inc

print('---------------------------------------------')

values = list(employee3.values())
print(values)  # Output: ['Shay', 29, 110000, False, 'Developer', 'Apple Inc']

for key in employee3.keys():
    print(key)
# Output:
# name
# age
# salary
# full_time
# job_title
# company

print('---------------------------------------------')

for value in employee3.values():
    print(value)
# Output:
    # Shay
    # 29
    # 110000
    # False
    # Developer
    # Apple Inc

print('---------------------------------------------')

for x in employee3.items():     # items(): returns a collection of tuples, in each tuple there will be two elements
    print(x)
# Output:
    # ('name', 'Shay')
    # ('age', 29)
    # ('salary', 110000)
    # ('full_time', False)
    # ('job_title', 'Developer')
    # ('company', 'Apple Inc')


print('---------------------------------------------')

for x in employee3.items():     # items(): returns a collection of tuples, in each tuple there will be two elements
    print(f'{x[0]} : {x[1]}')

# Output:
    # name : Shay
    # age : 29
    # salary : 110000
    # full_time : False
    # job_title : Developer
    # company : Apple Inc

print('---------------------------------------------')

# Nested Dictionary
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

print(students)
# Output:
    # {'A01': {'name': 'James', 'gender': 'Male', 'gpa': 3.5, 'subjects': ['Math', 'Physics']},
    #  'A02': {'name': 'Hazel', 'gender': 'Female', 'gpa': 3.8, 'subjects': ['Biology', 'Programming']},
    #  'A03': {'name': 'Yulia', 'gender': 'Female', 'gpa': 4, 'subjects': ['Chemistry', 'Programming']}}

print('---------------------------------------------')

print(students['A01'])
# Output:
    # {'name': 'Yulia', 'gender': 'Female', 'gpa': 4, 'subjects': ['Chemistry', 'Biology']}

print('---------------------------------------------')

students['A01']['gpa'] = 2.5
print(students)
# Output:
    # {'A01': {'name': 'James', 'gender': 'Male', 'gpa': 2.5, 'subjects': ['Math', 'Physics']},
    #  'A02': {'name': 'Hazel', 'gender': 'Female', 'gpa': 3.8, 'subjects': ['Biology', 'Programming']},
    #  'A03': {'name': 'Yulia', 'gender': 'Female', 'gpa': 4, 'subjects': ['Chemistry', 'Programming']}}

print('---------------------------------------------')


print('---------------------------------------------')

students['A02'].update( {'name': 'Jennifer' , 'gender': 'Female'} )
print(students['A02'])
# Output:
    # {'name': 'Jennifer', 'gender': 'Female', 'gpa': 3.8, 'subjects': ['Biology', 'Programming']}

print('---------------------------------------------')

print(students['A02']['subjects'])              # Output: ['Biology', 'Programming']

print('---------------------------------------------')

print(students['A02']['subjects'][0])           # Output: Biology

print('---------------------------------------------')

print(students['A02']['subjects'][1])           # Output: Programming

print('---------------------------------------------')

students['A02']['name'] = 'Daniel'
students['A02']['gender'] = 'Male'
print(students)
# Output:
    # {'A01': {'name': 'James', 'gender': 'Male', 'gpa': 2.5, 'subjects': ['Math', 'Physics']},
    #  'A02': {'name': 'Daniel', 'gender': 'Male', 'gpa': 3.8, 'subjects': ['Biology', 'Programming']},
    #  'A03': {'name': 'Yulia', 'gender': 'Female', 'gpa': 4, 'subjects': ['Chemistry', 'Programming']}}


print('---------------------------------------------')

students['A03']['subjects'][1] = 'Biology'
print(students['A03'])
# Output:
    # {'name': 'Yulia', 'gender': 'Female', 'gpa': 4, 'subjects': ['Chemistry', 'Biology']}

print('---------------------------------------------')

for x in students.items():
    print(x[1])
    for y in x[1]:
        print(y)
# Output:
    # {'name': 'James', 'gender': 'Male', 'gpa': 2.5, 'subjects': ['Math', 'Physics']}
    # name
    # gender
    # gpa
    # subjects
    # {'name': 'Daniel', 'gender': 'Male', 'gpa': 3.8, 'subjects': ['Biology', 'Programming']}
    # name
    # gender
    # gpa
    # subjects
    # {'name': 'Yulia', 'gender': 'Female', 'gpa': 4, 'subjects': ['Chemistry', 'Biology']}
    # name
    # gender
    # gpa
    # subjects

print('---------------------------------------------')

for value in students.values():
    print(value)
    for item in value.items():
        print(item[1])
# Output:
    # {'name': 'James', 'gender': 'Male', 'gpa': 2.5, 'subjects': ['Math', 'Physics']}
    # James
    # Male
    # 2.5
    # ['Math', 'Physics']
    # {'name': 'Daniel', 'gender': 'Male', 'gpa': 3.8, 'subjects': ['Biology', 'Programming']}
    # Daniel
    # Male
    # 3.8
    # ['Biology', 'Programming']
    # {'name': 'Yulia', 'gender': 'Female', 'gpa': 4, 'subjects': ['Chemistry', 'Biology']}
    # Yulia
    # Female
    # 4
    # ['Chemistry', 'Biology']
    # {'name': 'Yulia', 'gender': 'Female', 'gpa': 4, 'subjects': ['Chemistry', 'Biology']}
    # Yulia
    # Female
    # 4
    # ['Chemistry', 'Biology']
