"""

7. Create a python file named finra,
    Write a program which prints out the numbers from 1 to 100 but for numbers which are a multiple of both 3 and 5, print "FINRA" instead of the number,  for numbers which are a multiple of 3, print "FIN" instead of the number and for numbers which are a multiple of 5, print "RA" instead of the number.

    ex:
        output:
            1 2 FIN 4 RA FIN 7 8 FIN RA 11 FIN 13 14 FINRA 16 17 FIN



"""

for i in range(1, 101):
    # Check if the number is a multiple of both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FINRA", end=" ")
    # Check if the number is a multiple of 3
    elif i % 3 == 0:
        print("FIN", end=" ")
    # Check if the number is a multiple of 5
    elif i % 5 == 0:
        print("RA", end=" ")
    # If none of the above conditions are met, print the number itself
    else:
        print(i, end=" ")

# Print a newline to end the output
print()




for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FINRA")
    elif i % 3 == 0:
        print("FIN")
    elif i % 5 == 0:
        print("RA")
    else:
        print(i)
