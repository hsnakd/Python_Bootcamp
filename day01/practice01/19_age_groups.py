"""

19. Create a python file named age_groups, write a program that asks user to enter their age and define the age groups of the user
            age groups are:
                    Teenager (< 21)
                    Adult   (>=21 && <55 )
                    Senior  ( > 55 )

             if age is negative or greater than 150, print invalid

             NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT

"""


age = int(input("Enter your age: "))

if 0 < age < 150:
    age_group = "Invalid"
else:
    if age < 21:
        age_group = "Teenager"
    elif 21 <= age < 55:
        age_group = "Adult"
    else:
        age_group = "Senior"

print(age_group)