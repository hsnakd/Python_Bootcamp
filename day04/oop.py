print('-------------------Class / Object--------------------')
# Class:
# A class is a blueprint for creating objects.
# It defines a data structure (attributes) and methods (functions) that operate on that data.

# Example:
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")

# Object:
#     An object is an instance of a class.
#     It represents a real-world entity and encapsulates data and behavior.

# Example:
car1 = Car("Toyota", "Camry")
car1.display_info()  # Output: Toyota Camry

print('--------------Encapsulation--------------')
# Encapsulation:
# Encapsulation bundles data (attributes) and the methods that operate on the data into a single unit (class).
# It restricts direct access to some of the object's components and can control the modification and access of the data.

# Example:
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")
    # Adding a print statement for demonstration
    def display_balance(self):
        print(f"Current Balance: {self.__balance}")
# Creating an instance of BankAccount
account = BankAccount(balance=1000)
account.display_balance()  # Output: Current Balance: 1000


print('--------------Inheritance--------------')
# Inheritance:
# Inheritance allows a class to inherit the properties and methods of another class.
# It promotes code re-usability and establishes a hierarchy between classes.

# Example:
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    # Adding a print statement for demonstration
    def display_battery_info(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Creating an instance of ElectricCar
electric_car = ElectricCar("Tesla", "Model 3", battery_capacity=75)
electric_car.display_info()         # Output: Tesla Model 3
electric_car.display_battery_info() # Output: Battery Capacity: 75 kWh


print('--------------Polymorphism--------------')
# Polymorphism:
#     Polymorphism allows objects to be treated as instances of their parent class.
#     It can be achieved through method overriding.
#     Your example demonstrates polymorphism with 3D shapes, where different classes have a common method name (volume).

# Example:
class Shape3D:
    def volume(self):
        pass  # The method is intended to be overridden in child classes


class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4 / 3) * 3.14 * self.radius ** 3

class Cube(Shape3D):
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        return self.side_length ** 3


class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return 3.14 * self.radius ** 2 * self.height


def print_volume(shape_3d):
    try:
        print(f"Volume: {shape_3d.volume()}")
    except AttributeError:
        print("Volume calculation requires additional attributes.")


# Create instances of 3D shapes
sphere = Sphere(radius=5)
cube = Cube(side_length=4)
cylinder = Cylinder(radius=3, height=6)

# Print volumes
print_volume(sphere)   # Output: Volume: 523.3333333333334
print_volume(cube)     # Output: Volume: 64
print_volume(cylinder) # Output: Volume: 169.56

print('--------------Abstraction--------------')
# Abstraction:
#     Abstraction simplifies complex systems by hiding unnecessary details.
#     Abstract classes define a common interface with abstract methods to be implemented by concrete classes.
#     Your example uses abstraction to calculate the area of different shapes without knowing specific details.

from abc import ABC, abstractmethod

# Abstraction Example:
# Abstract class representing a shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method to be implemented by concrete classes

# Concrete classes implementing the Shape abstract class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Function to print the area of any shape without knowing its specific details
def print_area(shape):
    print(f"Area: {shape.area()}")

# Usage of abstraction
circle = Circle(radius=5)
square = Square(side=4)

print_area(circle)  # Output: Area: 78.5
print_area(square)  # Output: Area: 16
