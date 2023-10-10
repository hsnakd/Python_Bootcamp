"""
1.Create a python file named functions_practices:
    1.1 Create a function that can check if a person is eligible to vote
                Ex:
                    eligibleToVote(19, "USA");

                output:
                    You are not eligible to vote!

    1.2 Creates a function that can calculate the grade of the student based on the score

    1.3 Create a function that can if the given integer is positive, negative or zero

    1.4 Creates a function that can check if a string is palindrome, the function should return true if the given string is palindrome.

"""


# 1.1 Function to check if a person is eligible to vote
def eligibleToVote(age, country):
    if age >= 18 and country.lower() == "usa":
        return "You are eligible to vote!"
    else:
        return "You are not eligible to vote!"


print(eligibleToVote(19, "USA"))


# 1.2 Function to calculate the grade of a student based on the score
def calculateGrade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid score"

    print(calculateGrade(85))


# 1.3 Function to check if an integer is positive, negative, or zero
def checkInteger(value):
    if value > 0:
        return "Positive"
    elif value < 0:
        return "Negative"
    else:
        return "Zero"

    print(checkInteger(-5))


# 1.4 Function to check if a string is a palindrome
def isPalindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    s = ''.join(e for e in s if e.isalnum())  # Remove non-alphanumeric characters
    return s == s[::-1]  # Check if the string is equal to its reverse


# Test the functions
print(isPalindrome("racecar"))
