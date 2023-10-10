"""

3. Create a python file named inheritance_practice:
		Create an abstract class named Animal:
	        Variables:
	            name, breed(final), gender(final),  age, size, color(final)

	        Encapsulate all the fields

	        Add a cosntructor that can set all the fields

	        Methods:
	            eat() ==> different animals eat different foods
	            drink() ==> all the animals drink water
	            toString() ==> to display the full info of the animal


		    Create the following subclasses of Animal:
		            Dog
		                eat(): Dog Food

		            Cat
		                eat(): Cat Food

		            Parrot
		                eat():


		            Eagle

"""

even_count = 0
odd_count = 0

for i in range(1, 51):

    if i % 2 == 0:
        even_count += i
    else:
        odd_count += i

print(f'{even_count} even, {odd_count} odd')


print('--------------------------------------------------')

number = int(input("Enter a number : "))

number_count = 0

for i in range(1, number):
    number_count += i

print(f'Total Number : {number_count}')



"""

# 3.1 Program: Sum of Even Numbers between 1 and 100
def sum_of_even_numbers():
    even_sum = sum(range(2, 101, 2))
    return even_sum

# 3.2 Program: Sum of Odd Numbers between 1 and 100
def sum_of_odd_numbers():
    odd_sum = sum(range(1, 101, 2))
    return odd_sum

# 3.3 Program: Sum of All Numbers up to a Given Number
def sum_of_numbers_up_to_n(n):
    total_sum = sum(range(1, n + 1))
    return total_sum

# Main program to demonstrate the functions
if __name__ == "__main__":
    print("1. Sum of Even Numbers between 1 and 100:", sum_of_even_numbers())
    print("2. Sum of Odd Numbers between 1 and 100:", sum_of_odd_numbers())
    
    # Get user input for the number to calculate the sum up to
    user_input = int(input("Enter a number: "))
    print(f"3. Sum of all numbers between 1 and {user_input}:", sum_of_numbers_up_to_n(user_input))
    
"""