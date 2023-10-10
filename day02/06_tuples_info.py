"""

# Tuple
    • A special type of variable
    • Used to store multiple values of any types
    • Size is fixed, and cannot be increased/decreased
    • The values in the tuple are unchangeable
    • Every element in a tuple has 2 index numbers
        • Forward index
        • Reverse index
"""
"""
# Creating A Tuple

    • Created by placing all the elements inside parentheses (Optional) separated by commas
    • A comma must be given after the element, otherwise, it won’t be recognized as a tuple
    • Elements are ordered, unchangeable, can be duplicated, and can be of any data type
"""
# Creating a Tuple
my_tuple = (1, "hello", 3.14, True)

"""
# Accessing Tuple Elements
    • Elements of a tuple can be accessed by using the square brackets [ ]
    • The index number (forward/backward index) of the element needs to be provided
"""
# Accessing Tuple Elements
print(my_tuple[1])  # Outputs: hello
print(my_tuple[-2])  # Outputs: 3.14


"""
# Slicing Tuple: Start & End Indexes
    • Creates a range of elements (sub-tuples) by using the slice syntax [start : end]
    • We can specify the start index and end index (excluded), separated by a colon, to create the sub-tuples
"""
# Slicing Tuples
subset = my_tuple[1:3]
print(subset)  # Outputs: ('hello', 3.14)

"""
# Slicing Tuple: Slice From The Start
    • By not giving the start index, the slicing starts from the first element [ : end ]
"""


"""
# Slicing Tuple: Slice To The End
    • By not giving the end index, the slicing starts from the start index to the end of the tuple [start : ]
"""


"""
# Merging Tuples
    • To merge two or more tuples, we can use the + operator to merge them
"""
# Merging Tuples
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
merged_tuple = tuple1 + tuple2
print(merged_tuple)  # Outputs: (1, 2, 3, 'a', 'b', 'c')


"""
# Multiplying Tuples
    • To multiply the content of a tuple, we can use * operator
"""
# Multiplying Tuples
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Outputs: (1, 2, 3, 1, 2, 3, 1, 2, 3)


"""
# Tuple Methods
    • index(): returns the forward index number of a specified element from the tuple
    • count(): returns the frequency of a specified element from the tuple
"""
# Tuple Methods
index_of_hello = my_tuple.index("hello")
count_of_3 = my_tuple.count(3)

print(index_of_hello)  # Outputs: 1
print(count_of_3)  # Outputs: 0 (because 3 appears only once in the tuple)