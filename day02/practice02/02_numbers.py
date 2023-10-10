"""

2. Create a python file named numbers,
    Write a program that asks user to enter number for 5 times, and print how many positive and negative numbers user entered
            Ex:
                Inputs:
                    10
                    20
                    -1
                    0
                    3

                Output:
                    3 positive and 1 negative

"""

positive_count = 0
negative_count = 0
zero_count = 0

for i in range(5):

    number = int(input('Enter a number : '))


    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f'{positive_count} positive, {negative_count} negative and {zero_count} zero')

