"""

5. Create a python file named characters, write a program that can retive the digits, letters and special characters from a string
            Ex:
                input:
                    mn@#123Ab!

                output:
                    letters: mnAb
                    digits: 123
                    special chars: @#!

"""


value = (input("Enter a value: "))
letters = ''
digits = ''
special_ch = ''

for i in value:
    if i.isalpha():
        letters = letters + i
    elif i.isdigit():
        digits = digits + i
    else:
        special_ch = special_ch + i

print(f'Letters : {letters}\nDigits : {digits}\nSpecial Characters : {special_ch}')
