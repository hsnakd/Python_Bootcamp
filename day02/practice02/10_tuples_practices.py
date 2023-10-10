"""

10. Create a python file named tuples_practices:
        10.1 Write a program that can display the palindrome strings from a tuple of string

                Ex:
                    words = ('Java', 'Anna', 'python', 'Cydeo', 'Level')

                    output:
                        Anna
                        Level


        10.2 Write a program that can display the common elements of two lists:

                Ex:
                    tuple1 = (1,2,3,4,5)
                    tuple2 = (4,5,6,7,8)

                    Output:
                        4
                        5


        10.3 Write a program that can count the even and odd number from a tuple of integers

                Ex:
                    numbers = (1, 2, 3, 4, 5, 6, 7)

                    Output:
                        There are 3 even numbers and 4 odd numbers

"""

words = ('Java', 'Anna', 'python', 'Cydeo', 'Level')


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


for word in words:
    if is_palindrome(word):
        print(word)

"""

        10.2 Write a program that can display the common elements of two lists:

                Ex:
                    tuple1 = (1,2,3,4,5)
                    tuple2 = (4,5,6,7,8)

                    Output:
                        4
                        5


"""

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

common_elements = []

for element in tuple1:
    if element in tuple2:
        common_elements.append(element)

for element in common_elements:
    print(element)

"""Another solution"""
# Defines two tuples

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

# Convert the tuples to sets for easier comparison
set1 = set(tuple1)
set2 = set(tuple2)

# Find the common elements by taking the intersection of the sets
common_elements = set1.intersection(set2)

# Print the common elements
for element in common_elements:
    print(element)

"""

        10.3 Write a program that can count the even and odd number from a tuple of integers

                Ex:
                    numbers = (1, 2, 3, 4, 5, 6, 7)

                    Output:
                        There are 3 even numbers and 4 odd numbers

"""
numbers = (1, 2, 3, 4, 5, 6, 7)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"There are {even_count} even numbers and {odd_count} odd numbers.")