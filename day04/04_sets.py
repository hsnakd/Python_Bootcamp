# Creating an empty dictionary and checking its type
empty_dictionary = {}
print(type(empty_dictionary))       # Output: <class 'dict'>

# Creating an empty set and checking its type
empty_set = set()
print(type(empty_set))              # Output: <class 'set'>

print('--------------------------------------------')

# Creating a set with unique elements using the add() method
unique_element = set()

unique_element.add(10)
unique_element.add(10)
unique_element.add(10)
unique_element.add(20)
unique_element.add(20)

print(type(unique_element))         # Output: <class 'set'>
print(unique_element)               # Output: {10, 20}

# Attempting to access elements in a set using indexing (which is not allowed)
# print(unique_element[1])          # Output: TypeError: 'set' object is not subscriptable
# print(unique_element[1:])         # Output: TypeError: 'set' object is not subscriptable

# Removing an element from the set using the remove() method
unique_element.remove(10)
print(unique_element)               # Output: {20}

# Updating the set with additional elements using the update() method
unique_element.update((1, 2, 3, 4, 5, 1, 2, 3, 4, 5))
print(unique_element)               # Output: {1, 2, 3, 4, 5, 20}

# Popping an arbitrary element from the set using the pop() method
n = unique_element.pop()
print(unique_element)               # Output: {2, 3, 4, 5, 20}
print(n)                            # Output: 1

print('----------------------- difference -----------------------')

# Using the difference() method to find elements unique to the first set
s1 = {'Java', 'Python', 'C#'}
s2 = {'Ruby', 'Java', 'C++', 'Swift'}
s3 = s1.difference(s2)
print(s3)                           # Output: {'C#', 'Python'}

print('----------------------- intersection -----------------------')

# intersection() method to find common elements between two sets
set1 = {'Java', 'Python', 'C#', 'Cydeo'}
set2 = {'C++', 'Ruby', 'Swift', 'Java', 'Python'}
set3 = set1.intersection(set2)
print(set3)                         # Output: {'Java', 'Python'}

print('----------------------- different_update -----------------------')

# difference_update() to remove elements of the first set that exist in the second set
a1 = {'Book', 'Pen', 'Apple', 'Cherry', 'Coffee'}
a2 = {'Book', 'Apple', 'Banana', 'Grape', 'TV'}
a1.difference_update(a2)
print(a1)                           # Output: {'Cherry', 'Coffee', 'Pen'}

print('----------------------- intersection_update -----------------------')

# intersection_update() to remove uncommon elements between two sets
b1 = {'Cydeo', 'Python', 'Java', 'C#', 'Wooden Spoon', 'Ruby', 'Swift'}
b2 = {'Wooden Spoon', 'Python', 'Cydeo'}
b1.intersection_update(b2)
print(b1)                           # Output: {'Python', 'Wooden Spoon', 'Cydeo'}

print('----------------------- symmetric_update -----------------------')

# symmetric_difference() to find elements unique to each set
e1 = {'Apple', 'Banana', 'Cherry'}
e2 = {'Grape', 'Strawberry', 'Banana', 'Mango', 'Lemon', 'Apple'}
e3 = e1.symmetric_difference(e2)
print(e3)                           # Output: {'Lemon', 'Cherry', 'Strawberry', 'Grape', 'Mango'}

print('----------------------- symmetric_difference_update -----------------------')

# Using the symmetric_difference_update() method to update the set with the symmetric difference
set1 = {'Apple', 'Banana', 'Cherry'}
set2 = {'Grape', 'Strawberry', 'Banana', 'Mango', 'Lemon', 'Apple'}
set1.symmetric_difference_update(set2)
print(set1)                         # Output: {'Cherry', 'Grape', 'Strawberry', 'Mango', 'Lemon'}

print('------------------------------------------------------------')

# Demonstrating other set methods
fruits = {"apple", "banana", "orange"}

# Adding an element to the set using the add() method
fruits.add("kiwi")
print(fruits)                       # Output: {'apple', 'banana', 'orange', 'kiwi'}

# Removing a specified element using the remove() method
fruits.remove("banana")
print(fruits)                       # Output: {'apple', 'orange', 'kiwi'}

# Clearing all elements from the set using the clear() method
fruits.clear()
print(fruits)                       # Output: set()

# Updating the set with another set or iterable using the update() method
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)                         # Output: {1, 2, 3, 4, 5}

# Popping an arbitrary element using the pop() method (First In Last Out)
fruits = {"apple", "banana", "orange"}
removed_fruit = fruits.pop()
print(removed_fruit)                # Output: apple ==> a randomly selected element, e.g., 'banana'
print(fruits)                       # Output: {'banana', 'orange'}  ==> The set without the popped element

# Copying the set using the copy() method
original_set = {1, 2, 3}
copy_set = original_set.copy()
print(copy_set)                     # Output: {1, 2, 3}

# Using the difference() method to find the difference between two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference_set = set1.difference(set2)
print(difference_set)               # Output: {1, 2}

difference_set2 = set2.difference(set1)
print(difference_set2)               # Output: {5, 6}

# Using the intersection() method to find the common elements between two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = set1.intersection(set2)
print(intersection_set)             # Output: {3, 4}

# Using the difference_update() method to update the set with the difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference_update(set2)
print(set1)                         # Output: {1, 2}

# Using the intersection_update() method to update the set with the intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print(set1)                         # Output: {3, 4}


# Using the symmetric_difference() method to find the symmetric difference of two sets and creating a new set
set1 = {'Apple', 'Banana', 'Cherry'}
set2 = {'Grape', 'Strawberry', 'Banana', 'Mango', 'Lemon', 'Apple'}
set3 = set1.symmetric_difference(set2)
print(set3)     # Output: {'Lemon', 'Mango', 'Strawberry', 'Cherry', 'Grape'}

# Using the symmetric_difference_update() method to update the set with the symmetric difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)
print(set1)                         # Output: {1, 2, 5, 6}

# TODO: Both symmetric_difference_update() and symmetric_difference() methods achieve the same result,
#       but symmetric_difference() returns a new set without modifying the original sets,
#       while symmetric_difference_update() modifies the original set in place.
#       Depending on your use case, you can choose the one that suits your needs.