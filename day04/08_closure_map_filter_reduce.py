from functools import reduce

# Closures:
# A closure is a nested function that captures and remembers the values in the enclosing function's local scope, even if the outer function has finished execution. This allows the inner function to access and use those captured values. Closures are often used to create function factories or to maintain state.

# Closure example
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_instance = outer_function(10)
result_closure = closure_instance(5)
print("Closure result:", result_closure)  # Output: Closure result: 15
# In this example, inner_function is a closure that "closes over" the variable x from the outer_function.



# map() Function:
# The map() function applies a given function to all the items in an iterable (list, tuple, etc.) and returns an iterator that produces the results.

# map() example
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print("Map result:", list(squared))  # Output: Map result: [1, 4, 9, 16, 25]
# In this example, the map() function squares each element in the numbers list using a lambda function.



# filter() Function:
# The filter() function filters elements of an iterable based on a function that returns either True or False. It returns an iterator containing the elements for which the function returns True.

# filter() example
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Filter result:", list(even_numbers))  # Output: Reduce result: 120
# In this example, the filter() function keeps only the even numbers from the numbers list.



# reduce() Function:
# The reduce() function, which was part of the functools module in Python 2, and is available directly in Python 3 with from functools import reduce, applies a rolling computation to sequential pairs of values in an iterable, reducing the iterable to a single accumulated result.

# reduce() example
product = reduce(lambda x, y: x * y, numbers)
print("Reduce result:", product)  # Output: 120 (1 * 2 * 3 * 4 * 5)
# In this example, the reduce() function multiplies each element in the numbers list sequentially.