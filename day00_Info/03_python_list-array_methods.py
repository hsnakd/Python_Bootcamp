# List methods example

# append(): Adds an element to the end of the list.
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(f"fruits after append('orange'): {fruits}")  # Output: fruits after append('orange'): ['apple', 'banana', 'cherry', 'orange']

# clear(): Removes all elements from the list.
fruits.clear()
print(f"fruits after clear(): {fruits}")  # Output: fruits after clear(): []

# copy(): Creates a shallow copy of the list.
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(f"copied_list: {copied_list}")  # Output: copied_list: [1, 2, 3]

# count(): Returns the number of occurrences of a specified element in the list.
numbers = [1, 2, 3, 2, 4, 2, 5]
count_of_twos = numbers.count(2)
print(f"Count of 2 in numbers: {count_of_twos}")  # Output: Count of 2 in numbers: 3

# extend(): Appends the elements of another list to the end of the current list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f"list1 after extend(list2): {list1}")  # Output: list1 after extend(list2): [1, 2, 3, 4, 5, 6]

# index(): Returns the index of the first occurrence of a specified element.
fruits = ['apple', 'banana', 'cherry']
index_of_banana = fruits.index('banana')

print(f"Index of 'banana' in fruits: {index_of_banana}")  # Output: Index of 'banana' in fruits: 1

# insert(): Inserts an element at a specified position in the list.
numbers = [1, 2, 3, 5]
numbers.insert(3, 4)
print(f"numbers after insert(3, 4): {numbers}")  # Output: numbers after insert(3, 4): [1, 2, 3, 4, 5]

# pop(): Removes and returns the element at the specified position in the list.
colors = ['red', 'green', 'blue']
popped_color = colors.pop(1)
print(f"popped_color: {popped_color}, colors after pop(1): {colors}")  # Output: popped_color: green, colors after pop(1): ['red', 'blue']

# remove(): Removes the first occurrence of a specified element from the list.
animals = ['dog', 'cat', 'elephant', 'cat']
animals.remove('cat')
print(f"animals after remove('cat'): {animals}")  # Output: animals after remove('cat'): ['dog', 'elephant']

# reverse(): Reverses the order of elements in the list.
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"numbers after reverse(): {numbers}")  # Output: numbers after reverse(): [5, 4, 3, 2, 1]

# sort(): Sorts the elements of a list in ascending order.
unsorted_numbers = [3, 1, 4, 1, 5, 9, 2]
unsorted_numbers.sort()
print(f"unsorted_numbers after sort(): {unsorted_numbers}")  # Output: unsorted_numbers after sort(): [1, 1, 2, 3, 4, 5, 9]
