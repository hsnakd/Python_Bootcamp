"""

21. Create a python file named number_to_words,
        Write a program that can convert user entered number (from 0~9) to words.

    NOTE: MUST use ternary

"""

number = int(input("Enter a number from 0 to 9: "))

if number == 0:
    word = "Zero"
elif number == 1:
    word = "One"
elif number == 2:
    word = "Two"
elif number == 3:
    word = "Three"
elif number == 4:
    word = "Four"
elif number == 5:
    word = "Five"
elif number == 6:
    word = "Six"
elif number == 7:
    word = "Seven"
elif number == 8:
    word = "Eight"
elif number == 9:
    word = "Nine"

print(word)



#
#
# number = int(input("Enter a number from 0 to 9: "))
#
# # Use ternary operators to convert the number to words
# word = (
#     "Zero" if number == 0 else
#     "One" if number == 1 else
#     "Two" if number == 2 else
#     "Three" if number == 3 else
#     "Four" if number == 4 else
#     "Five" if number == 5 else
#     "Six" if number == 6 else
#     "Seven" if number == 7 else
#     "Eight" if number == 8 else
#     "Nine" if number == 9 else
#     "Invalid input"
# )
#
# # Print the result
# print(word)