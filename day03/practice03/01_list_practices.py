"""

1. Create a python file named list_practices:
		1.1 Write a program that can move all the zeros to the last indexes of ArrayList
	            Ex:
	                list = [1,0,2,0,3,0,4,0]

	            output:
	                [1, 2, 3, 4, 0, 0, 0, 0]


	    1.2 write a program that can multiply each odd number by 2
		            ex:
		            	list = [1,2,3,4,5];

		                output: [2, 4, 6, 8, 10]


	    1.3 Write a program that can remove all the names "Ahmed" from a list of strings
				Ex:
	                list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]

	            output:
	            	["John", "Daniel", "James", "Muhammed"]


		1.4 Write a program that can display the palindrome strings from a list of String
				Ex:
					words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']

					output:
						Anna
						Level


		1.5 Write a program that can display the common elements of two lists:
				Ex:
					list1 = [1,2,3,4,5]
					list2 = [4,5,6,7,8]

					Output:
						4
						5

		1.6 Write a program that can remove the duplicated elements from a list
				Ex:
					elements = [1,2,3,4,5,1,2,3,4,5]

					Output:
						[1, 2, 3, 4, 5]

					00_Notes.txt: Do Not use Set


		1.7 Write a program that can remove string elements from a list if the first and last characters of the string are same
				ex:
					list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}

				output:
					["Lan", "Ebrahim", "Farida"]


		1.8  Write a program that can display the unique elements of an arrayList:
					ex:
						list = [1, 1, 2, 3, 3, 4, 5, 5]

					output:
						[2, 4]

"""
print('----------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------')

number_list = [1, 0, 2, 0, 3, 0, 4, 0]
new_list = []
zero_count = 0
number = 0

for i in number_list:
    if i != number:
        new_list.append(i)
    else:
        zero_count += 1

new_list.extend([number] * zero_count)

print(new_list)

print('--------------------------------------------')


def move_zeros_to_end(arr):
    zeros_count = arr.count(0)
    arr = [x for x in arr if x != 0]
    arr.extend([0] * zeros_count)
    return arr


input_list = [1, 0, 2, 0, 3, 0, 4, 0]
result = move_zeros_to_end(input_list)
print(result)

print('----------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------')

num_list = [1, 2, 3, 4, 5]

for i in range(len(num_list)):
    num_list[i] *= 2

print(num_list)

print('--------------------------------------------')


def multiply_odd_numbers(arr):
    return [x * 2 if x % 2 != 0 else x for x in arr]


input_list = [1, 2, 3, 4, 5]
result = multiply_odd_numbers(input_list)
print(result)

print('----------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------')

name_list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]
name = 'Ahmed'
new_name_list = []

for i in name_list:
    if i != name:
        new_name_list.append(i)

print(new_name_list)

print('--------------------------------------------')


def remove_name(name_list, name):
    return [x for x in name_list if x != name]


name_list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]
name_to_remove = "Ahmed"
result = remove_name(name_list, name_to_remove)
print(result)

print('----------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------')

words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']
new_words_list = []

for word in words:
    if word.lower() == word[::-1].lower():
        new_words_list.append(word)

print(new_words_list)

print('--------------------------------------------')


def is_palindrome(word):
    return word == word[::-1]


words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']
palindromes = [word for word in words if is_palindrome(word)]
for palindrome in palindromes:
    print(palindrome)

print('----------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------')

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

for i in list1:
    for j in list2:
        if i == j:
            print(i)

print('--------------------------------------------')

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = [x for x in list1 if x in list2]
for element in common_elements:
    print(element)

print('----------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------')

elements = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
unique_elements = []

for i in elements:
    for j in elements:
        if i not in unique_elements:
            unique_elements.append(i)
print(unique_elements)

print('--------------------------------------------')

elements = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
unique_elements = []
for element in elements:
    if element not in unique_elements:
        unique_elements.append(element)
print(unique_elements)

print('----------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------')

word_list = ["Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"]
filtered_list = []

for word in word_list:
    if len(word) > 1 and word[0].lower() != word[-1].lower():
        filtered_list.append(word)

print(filtered_list)


print('--------------------------------------------')


def has_same_first_and_last(word):
    return len(word) > 1 and word[0].lower()== word[-1].lower()

word_list1 = ["Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"]
filtered_list1 = [word for word in word_list1 if not has_same_first_and_last(word)]
print(filtered_list1)

print('----------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------')


numbers = [1, 1, 2, 3, 3, 4, 5, 5]
unique_numbers = []

for number in numbers:
    if numbers.count(number) == 1:
        unique_numbers.append(number)

print(unique_numbers)



print('--------------------------------------------')
def unique_elements(arr):
    unique = []
    for item in arr:
        if arr.count(item) == 1:
            unique.append(item)
    return unique

input_list = [1, 1, 2, 3, 3, 4, 5, 5]
result = unique_elements(input_list)
print(result)


print('----------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------')
