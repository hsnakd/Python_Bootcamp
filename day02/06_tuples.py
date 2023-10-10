tuples = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", 1, 2, 3, 4, 5, 6, 7, True, False)

print(type(tuples))             # Output: <class 'tuple'>

print(len(tuples))              # Output: 16

print(tuples)                   # Output: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 1, 2, 3, 4, 5, 6, 7, True, False)

print(tuples[0])                # Output: Monday

print(tuples[-1])               # Output: False

# tuples[0] = 'Java'  # This line would cause an error as tuples are immutable

print('---------------------------------------')

days = ('Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

work_days = days[1:4]
print(work_days)                # Output: ('Tuesday', 'Wednesday', 'Thursday')

week_days = days[:-2]
print(week_days)                # Output: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

weekend = days[-2:]
print(weekend)                  # Output: ('Saturday', 'Sunday')

print('---------------------------------------')

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(tuple1 == tuple2)         # Output: True

print(tuple1 is tuple2)         # Output: True

tuple3 = tuple1 + tuple2
print(tuple3)                   # Output: (1, 2, 3, 1, 2, 3)

tuple4 = tuple1 * 5
print(tuple4)                   # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)

print('---------------------------------------')

reversed_tuple1 = days[::-1]
print(reversed_tuple1)          # Output: ('Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday')

print('---------------------------------------')

reversed_tuple2 = tuple(reversed(days))
print(reversed_tuple2)          # Output: ('Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday')

print('---------------------------------------')

print(days.index('Wednesday'))  # Output: 2

print('---------------------------------------')

numbers = (10, 10, 10, 10, 20, 30, 40, 50, 10)

print(numbers.count(10))        # Output: 5

print('---------------------------------------')

for x in days:
    print(x)                    # Output: (Prints each day)

print('---------------------------------------')

for x in range(0, len(days)):
    print(x)                    # Output: Prints index from 0 to 6

print('---------------------------------------')

for x in reversed(range(0, len(days))):
    print(x)                    # Output: Prints index from 6 to 0

print('---------------------------------------')

nested_tuple = ((1, 2, 3), (4, 5, 6, 7, 8), (9, 10))

print(len(nested_tuple))        # Output: 3
print('---------------------------------------')


# Nested loop to print each element
nested_tuple = ((1, 2, 3), (4, 5, 6, 7, 8), (9, 10))
for x in nested_tuple:
    print(x)
    for y in x:
        print(y)

# Output:
# (1, 2, 3)
# 1
# 2
# 3
# (4, 5, 6, 7, 8)
# 4
# 5
# 6
# 7
# 8
# (9, 10)
# 9
# 10

print('---------------------------------------')

# Nested loop using indexes
nested_tuple = ((1, 2, 3), (4, 5, 6, 7, 8), (9, 10))
for i in range(0, len(nested_tuple)):
    for j in range(0, len(nested_tuple[i])):
        print(nested_tuple[i][j])

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
