"""

18. Create a python file named grade, a variable named grade is given. write a program to print the following messages:
            'A': excellent
            'B': great job
            'C': good
            'D': passed
            'F': failed
            otherwise: invalid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT

"""

grade = str(input("Enter your grade: "))

if grade == 'A':
    message = 'Excellent'
elif grade == 'B':
    message = 'Great Job'
elif grade == 'C':
    message = 'Good'
elif grade == 'D':
    message = 'Passed'
elif grade == 'F':
    message = 'Failed'
else:
    message = 'invalid'

print(message)