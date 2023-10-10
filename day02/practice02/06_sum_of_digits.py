"""

6. Create a python file named sum_of_digits,
    Write a program that can return the sum of digits from a string
             Ex:
                 input: A1B2C3

                 output: 6

"""


value = (input("Enter a value: "))
sum_of_digits = 0

for i in value:
    if i.isdigit():
        sum_of_digits += int(i)


print(f'Sum of Digits : {sum_of_digits}')
