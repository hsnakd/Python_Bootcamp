# day03/abstraction2.py
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        super().__init__('Square')
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__('Rectangle')
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# day03/inheritance.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# main.py
from day03.abstraction2 import Shape, Square, Rectangle
from day03.inheritance import Person

shape1: Shape = Square(5)
shape2: Shape = Rectangle(3, 4)

def display_area(shape: Shape):
    print(f"The {shape.name}'s area is {shape.area()}")

display_area(shape1)
display_area(shape2)

person1 = Person('James', 35)
