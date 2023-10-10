"""

4. Create a python file named factorial_number,
    Write a program that can return the factorial number of any given number

            Ex:
                input: 5
                output: 120

                    (Because: 5! = 5 * 4 * 3 * 2* 1 = 120)

"""


number = int(input("Enter a number: "))

factorial_number = 1

if number == 0:
    print(f'Factorial Number: {factorial_number}')
elif number > 0:
    for i in range(1, number + 1):
        factorial_number *= i
    print(f'Factorial Number: {factorial_number}')
else:
    print("Factorial is undefined for negative numbers.")
