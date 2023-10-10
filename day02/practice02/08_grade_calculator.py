"""

8. Create a python file named grade calculator, and Write a program for grade calculator:
    8.1. Ask the user "Enter your score"
            If user enters invalid score, terminate the program after displaying the error message "Invalid Entry"

    8.2 Display the grade of the student.
                    90 ~ 100 ==> A
                    80 ~ 89 ==> B
                    70 ~ 79 ==> C
                    60 ~ 69 ==> D
                    0 ~ 59 ==> F

    8.3 Ask the user would you like to continue
            If "yes" --> repeat the previous steps
            If "no" --> print "Thank you for using Cydeo Grade Calculator APP"

            If a user enters an invalid entry, ask the user to re-enter until the user provides a valid entry



"""

while True:
    score = int(input('Enter your score: '))

    if 90 <= score <= 100:
        grade = 'A'
    elif 80 <= score <= 89:
        grade = 'B'
    elif 70 <= score <= 79:
        grade = 'C'
    elif 60 <= score <= 69:
        grade = 'D'
    elif 0 <= score <= 59:
        grade = 'F'
    else:
        print('Invalid Entry')
        break

    print(f'Grade: {grade}')



print('--------------------------------------')


while True:
    answer = input('Would you like to continue (yes/no): ').lower()

    if answer == 'yes':
        pass
    elif answer == 'no':
        print("Thank you for using Cydeo Grade Calculator APP")
        break
    else:
        print('You entered an invalid answer. Please enter "yes" or "no".')


