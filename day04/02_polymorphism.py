# Importing Shape, Square, Rectangle from abstraction2 module
from day03.abstraction2 import Shape, Square, Rectangle
# Output:
    # Square {'name': 'Square', 'side': 5}
    # 25
    # Circle {'name': 'Circle', 'radius': 3}
    # 28.274333882308138
    # Rectangle {'name': 'Rectangle', 'width': 4, 'length': 6}
    # 24
    # Cube {'name': 'Cube', 'side': 3}
    # 54
    # 27
    # Cylinder {'name': 'Cylinder', 'radius': 2, 'height': 5}
    # 87.96459430051421
    # 62.83185307179586

print('-------------------------------------------------')

# Importing Person from inheritance module
from day03.inheritance import Person
# Output:
    # Employee{'name': 'Hazel', 'age': 27, 'job_title': 'QA', 'company_name': 'Apple Inc', 'salary': 0}
    # Developer{'name': 'Jack', 'age': 39, 'job_title': 'Java Developer', 'company_name': 'Unknown', 'salary': 0}
    # Developer{'name': 'Daniel', 'age': 35, 'job_title': 'Python Developer', 'company_name': 'Google Inc', 'salary': 100000}
    # Teacher{'name': 'Breanna', 'age': 45, 'job_title': 'Teacher', 'company_name': 'Unknown', 'salary': 0}
    # Hazel is working
    # Python Developer Daniel is coding
    # Breanna is teaching


# Creating a Square object with side length 5
shape1: Shape = Square(5)

# Creating a Rectangle object with width 3 and height 4
shape2: Shape = Rectangle(3, 4)


# Function to display the area of a Shape
def display_area(shape: Shape):  # parameter's type is restricted to shape objects ONLY
    print(f'The {shape.name}\'s area is {shape.area()} ')

print('-------------------------------------------------')

# Displaying the area of the Square
display_area(shape1)  # Output: The Square's area is 25

print('-------------------------------------------------')

# Displaying the area of the Rectangle
display_area(shape2)  # Output: The Rectangle's area is 12

print('-------------------------------------------------')

# Creating a Person object
person1 = Person('James', 35)

# Printing information about the person
print(f'Person: Name - {person1.name}, Age - {person1.age}')  # Output: Person: Name - James, Age - 35
