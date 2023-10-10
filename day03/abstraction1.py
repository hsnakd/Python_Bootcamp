import numbers

# BaseClass Abstraction
class Shape:
    def __init__(self):
        # Initialize the name attribute to the name of the class
        self.name = type(self).__name__

    def area(self) -> numbers:
        # Abstract method to be overridden by subclasses
        pass  # When we give a pass statement in a method, it is optional for the child class to implement it.

    def __str__(self):
        # Provide a string representation of the object
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):
    def __init__(self, side):
        # Call the superclass (Shape) constructor
        super().__init__()
        # Set the side attribute
        self.side = side

    def area(self):
        # Override the area method to calculate the area of a square
        return self.side ** 2


# Example Usage
square = Square(5)

# Output the string representation of the square and its area
print(square)               # Output: Square{'name': 'Square', 'side': 5}
print(square.area())        # Output: 25
