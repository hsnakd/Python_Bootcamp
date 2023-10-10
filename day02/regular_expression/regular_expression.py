"""
findall()       Returns a list which containing all matches with the specified search pattern
search()        Returns a Match Object if the specified search pattern is found anywhere in the string
split()         Returns a list where the string has been split at each match
sub()           Replaces one or many matches with a string
"""
import re

# Sample text for demonstration
text = "Hello, my email addresses are john@example.com and jane@example.org. Please contact me."

# findall() - Returns a list of all email addresses in the text
email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
email_addresses = re.findall(email_pattern, text)
print("Email Addresses:", email_addresses)
#Email Addresses: ['john@example.com', 'jane@example.org']


# search() - Searches for the word "email" in the text
search_result = re.search(r'email', text)
if search_result:
    print("Found 'email' at index:", search_result.start())
#Found 'email' at index: 10


# split() - Splits the text at spaces
words = re.split(r'\s', text)
print("Words in the text:", words)

# sub() - Replaces all email addresses with "<email>"
masked_text = re.sub(email_pattern, '<email>', text)
print("Masked Text:", masked_text)
#Words in the text: ['Hello,', 'my', 'email', 'addresses', 'are', 'john@example.com', 'and', 'jane@example.org.', 'Please', 'contact', 'me.']

"""
In this example:

findall() is used to find all email addresses in the text using a regular expression pattern.

search() is used to search for the word "email" in the text, and it returns a Match Object if found.

split() is used to split the text into a list of words based on spaces.

sub() is used to replace all email addresses in the text with the string "<email>".

Make sure to customize the regular expressions (email_pattern in this case) to match your specific use case or search patterns.

"""

text = "The quick brown fox jumps over the lazy dog. The dog barks loudly."

# Find all words that contain the letters 'o' and 'g'
matches = re.findall(r'\w*o\w*g\w*', text)

print(matches)  # ['brown', 'fox', 'over', 'dog', 'dog']


text = "The quick brown fox jumps over the lazy dog."

# Search for the word "fox" in the text
match = re.search(r'fox', text)

if match:
    print("Match found at index:", match.start())
else:
    print("Match not found.")
# Match found at index: 16


text = "apple,banana,orange,grape"

# Split the text at commas
result = re.split(r',', text)

print(result)  # ['apple', 'banana', 'orange', 'grape']


text = "The quick brown fox jumps over the lazy dog."

# Replace "fox" with "cat"
new_text = re.sub(r'fox', 'cat', text)

print(new_text)  # The quick brown cat jumps over the lazy dog.

s = 'a1b2c3d4e5'

result = re.findall('[0-9]', s)
print(result)       #['1', '2', '3', '4', '5']

