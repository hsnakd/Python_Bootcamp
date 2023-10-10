# List Operations
groceries_list = ['Eggs', 'Milk', 'Rice', 'Chicken']
print(groceries_list)               # Output: ['Eggs', 'Milk', 'Rice', 'Chicken']
print(len(groceries_list))          # Output: 4

groceries_list.extend(('Beef', 'Oranges', 'Onion'))  # It can be tuple, list, set
print(groceries_list)               # Output: ['Eggs', 'Milk', 'Rice', 'Chicken', 'Beef', 'Oranges', 'Onion']
print(len(groceries_list))          # Output: 7

groceries_list[-2] = 'Cherry'
print(groceries_list)               # Output: ['Eggs', 'Milk', 'Rice', 'Chicken', 'Beef', 'Cherry', 'Onion']

groceries_list[-2:] = 'Cherry'
print(groceries_list)               # Output: ['Eggs', 'Milk', 'Rice', 'Chicken', 'Beef', 'C', 'h', 'e', 'r', 'r', 'y']

print('------------------------------------')

# List Slicing and Modification
numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers_list)                 # Output: [10, 20, 30, 40, 50, 60, 70, 80]

numbers_list[2:-2] = [300, 400, 500, 600]
print(numbers_list)                 # Output: [10, 20, 300, 400, 500, 600, 70, 80]

numbers_list[2:] = [3000, 4000, 5000, 6000]
print(numbers_list)                 # Output: [10, 20, 3000, 4000, 5000, 6000]

print('------------------------------------')

# List Slicing
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

list1 = characters[2: -3]
print(list1)                        # Output: ['c', 'd', 'e', 'f']

list2 = characters[:4]
print(list2)                        # Output: ['a', 'b', 'c', 'd']

list3 = characters[2:]
print(list3)                        # Output: ['c', 'd', 'e', 'f', 'g', 'h', 'i']

characters[2:5] = ['C', "D", 'E', 'C', 'D', 'E', 'X', 'Y', 'Z']
print(characters)                   # Output: ['a', 'b', 'C', 'D', 'E', 'C', 'D', 'E', 'X', 'Y', 'Z', 'f', 'g', 'h', 'i']

characters[2:] = ['C', "D", 'E', 'C', 'D', 'E', 'X', 'Y', 'Z']
print(characters)                   # Output: ['a', 'b', 'C', 'D', 'E', 'C', 'D', 'E', 'X', 'Y', 'Z']

print('------------------------------------')

# Looping through a List
names = ['Conor', 'Steve', 'Hazel', 'Breanna']

for x in names:
    print(x)
# Output:
    # Conor
    # Steve
    # Hazel
    # Breanna

print('------------------------------------')

# Modifying List Elements in a Loop
nums = [10, 20, 30, 40, 50, 60]

# for i in range(0, len(nums)):
for i in range(len(nums)):
    nums[i] = int(nums[i] / 5)

print(nums)                         # Output: [2, 4, 6, 8, 10, 12]

print('------------------------------------')

# Reversing a List
nums = [10, 20, 30, 40, 50, 60]

for i in reversed(range(len(nums))):
    print(nums[i])
# Output:
    # 60
    # 50
    # 40
    # 30
    # 20
    # 10

print('------------------------------------')

for x in nums[::-1]:
    print(x)
# Output:
    # 60
    # 50
    # 40
    # 30
    # 20
    # 10

print('------------------------------------')

for x in reversed(nums):
    print(x)
# Output:
    # 60
    # 50
    # 40
    # 30
    # 20
    # 10

print('------------------------------------')

# While Loop with a List
i = 0

while i < len(nums):
    print(nums[i])
    i += 1
# Output:
    # 10
    # 20
    # 30
    # 40
    # 50
    # 60

print('------------------------------------')

# Looping with Range
for i in range(1, 6):
    i += 2
    print(i)
# Output:
    # 3
    # 4
    # 5
    # 6
    # 7

print('------------------------------------')

# Sorting a List
nums = [60, 500, 10, 20, 15, 5, 0]

nums.sort()  # ascending order
print(nums)                         # Output: [0, 5, 10, 15, 20, 60, 500]

nums.sort(reverse=True)
print(nums)                         # Output: [500, 60, 20, 15, 10, 5, 0]

print('------------------------------------')

# Reversing a List
list1 = [10, 20, 30, 40]

# list1 = list( reversed(list1) )  # it creates a new object

list1.reverse()
print(list1)                        # Output: [40, 30, 20, 10]

print('------------------------------------')

# Tuple to List and Back
tuple_elements = ('Java', 'Python', 'C#', 'Ruby')

list_elements = list(tuple_elements)
list_elements[-2] = 'C++'
print(list_elements)                # Output: ['Java', 'Python', 'C++', 'Ruby']

list_elements.append('SWIFT')
print(list_elements)                # Output: ['Java', 'Python', 'C++', 'Ruby', 'SWIFT']

tuple_elements = tuple(list_elements)
print(tuple_elements)               # Output: ('Java', 'Python', 'C++', 'Ruby', 'SWIFT')

print('------------------------------------')

# Identity Comparison
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

print(list1 == list2)               # Output: True / checks if the values of the two tuples are equal, which is True.
print(list1 is list2)               # Output: False / checks if the two lists refer to the exact same object, which is False.


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 5)

print(tuple1 == tuple2)             # Output: True
print(tuple1 is tuple2)             # Output: True

print('------------------------------------')

# List Manipulation - Append, Remove, Pop, Insert, Index, Count
groceries_list = ['Eggs', 'Milk', 'Rice']

# append() : Add 'Chicken' to the end of the list.
groceries_list.append('Chicken')

# extend() : Extend the list with the items ('Beef', 'Oranges', 'Onion').
groceries_list.extend(('Beef', 'Oranges', 'Onion'))
print(groceries_list)               # Output: ['Eggs', 'Milk', 'Rice', 'Chicken', 'Beef', 'Oranges', 'Onion']

# remove() : Remove 'Beef' from the list.
groceries_list.remove('Beef')
print(groceries_list)               # Output: ['Eggs', 'Milk', 'Rice', 'Chicken', 'Oranges', 'Onion']

# pop() : Remove the last item from the list.
groceries_list.pop()
print(groceries_list)               # Output: ['Eggs', 'Milk', 'Rice', 'Chicken', 'Oranges']

# Remove the item at index 1.
groceries_list.pop(1)
print(groceries_list)               # Output: ['Eggs', 'Rice', 'Chicken', 'Oranges']

# insert() : Insert 'Apple' at index 2.
groceries_list.insert(2, 'Apple')
print(groceries_list)               # Output: ['Eggs', 'Rice', 'Apple', 'Chicken', 'Oranges']

# index() : Find the index of 'Eggs'.
print(groceries_list.index('Eggs')) # Output: 0

# count() : Count the occurrences of 1 in the list 'nums'.
nums = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]
print(nums.count(1))                # Output: 6

nums.remove(1)
print(nums)                         # Output: [2, 3, 4, 5, 1, 1, 1, 1, 1]


print('------------------------- Comprehensions -------------------------')

# List Comprehensions
    # • Used to create a new list based the values of an exiting iterable (list/set/tuple)
# numbers = [1, 2, 3, 4, 5]
# new_list = [expression for item in iterable if condition]
# new_list = [ var_name for var_name in iterable if condition ]
# new_list = [    x     for    x     in numbers  if x % 2 == 0]
# print(new_list)           Output: [2, 4]

    # var_name  ==> both var_name must be same
    # for       ==> keyword
    # in        ==> keyword
    # iterable  ==> must be a List/Tuple/Set
    # if        ==> keyword
    # condition ==> for filtering the elements of the iterable


# Create a list of numbers from 1 to 50.
nums = [x for x in range(1, 51)]
print(nums)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]


"""
divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)

print(divisible_by_5)

"""

print('------------------------------------')

# Filter numbers divisible by 5 and create a tuple.
divisible_by_5 = tuple([x for x in nums if x % 5 == 0])
print(divisible_by_5)  # Output: (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)

print('------------------------------------')

# Even and odd separate numbers.
even_nums = [x for x in nums if x % 2 == 0]
odd_numbers = [x for x in nums if x % 2 != 0]
print(even_nums)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
print(odd_numbers)
# Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

print('------------------------------------')

# Remove occurrences of 'Java' (case-insensitive) from the list.
names = ['Python', 'Java', 'Java', 'JavaScript', 'java', 'JaVA', 'Ruby']
names = [x for x in names if x.lower() != 'java']
print(names)  # Output: ['Python', 'JavaScript', 'Ruby']


numbers = [1, 2, 3, 4, 5]

new_list = [    x     for    x     in numbers  if x % 2 == 0]

