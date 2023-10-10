# TODO: Class
    # • A class is like a blueprint or a template for creating objects. (In Python, classes are only created for objects)
    # • It defines the attributes (data) and methods (functions) that the objects will have.

# TODO: Object/Instance
    # • An object is a concrete occurrence of a class. It's created based on the blueprint provided by the class.
    # • Think of a class as a blueprint for a car, and an object as an actual car created from that blueprint.

# TODO: Instantiation
    # • The process of creating an object from a class is called instantiation.
    # • It involves allocating memory for the object and initializing its attributes.

# Define a class
class Car:
    # constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# Create an instance/object of the Car class
my_car1 = Car(brand="Toyota", model="Camry")
my_car2 = Car("Nissan", "Qashqai")

    # my_car                                :   Reference Name
    # Car                                   :   Class Name
    # brand="Toyota", model="Camry"         :   Arguments of the constructor
    # "Nissan", "Qashqai"                   :   Arguments of the constructor (brand, model)
    # Car(brand="Toyota", model="Camry")    :   Object

# Accessing object attributes
print(my_car1.brand)        # Output: Toyota
print(my_car1.model)        # Output: Camry
print(my_car2.brand)        # Output: Nissan
print(my_car2.model)        # Output: Qashqai

# In this example:
    # • Car is a class with attributes brand and model.
    # • my_car is an object (instance) of the Car class.
    # • The __init__ method is a special method called the constructor, which is used for initializing object attributes.


# So, creating an object involves calling the class and providing any necessary initial values for its attributes. The object can then be used to access or modify those attributes and call its methods.


# TODO: The __init()__ Method
    # • Built-in __init()__ method used for defining & initializing the attributes
    # • Belongs to the object, and each object has its memory
    # • Gets executed when an object is created from the class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating an object and initializing its attributes
my_dog = Dog(name="Buddy", age=3)

print(f"Dog's name: {my_dog.name}")     # Output: Dog's name: Buddy
print(f"Dog's age: {my_dog.age}")       # Output: Dog's age: 3

# In this example, __init__ initializes the name and age attributes when a Dog object is created.


# TODO: Object Methods
    # • Objects can share the methods created within the class
    # • Methods can be called through the object once it’s instantiated
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")

# Creating an object and calling a method
my_car = Car(brand="Toyota", model="Camry")
my_car.display_info()  # Output: Toyota Camry

# Output: Toyota Camry

# Here, display_info is a method of the Car class, and it can be called on a Car object.


# TODO: The First Parameter in Object Methods (self)
    # • The first parameter self keyword references the instance of the class
    # • Used for accessing the attributes of the class

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2


# Creating an object and calling a method with 'self'
my_circle = Circle(radius=5)
area = my_circle.calculate_area()
print(f"Area of the circle: {area}")

# Output: Area of the circle: 78.5

# In the calculate_area method, self refers to the instance of the Circle class, allowing access to the radius attribute.


# TODO: Accessing an Object’s Data and Methods
    # • An Object’s members refer to its data fields and methods. After the object is created, its data can be accessed, and its methods can be invoked using the dot operator (.)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Creating an object and accessing data and method
student1 = Student(name="Alice", age=20)
print(f"Student's name: {student1.name}")
student1.display_info()

# Output: Student's name: Alice
# Output: Name: Alice, Age: 20

# After creating the student1 object, you can access its data (name) and invoke its method (display_info).


# TODO: The __str()__ Method
    # • Built-in __str()__ method is used for controlling what should be returned when the class object is represented as a string
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

# Creating an object and using __str__ for string representation
my_book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
print(my_book)  # Output: The Great Gatsby by F. Scott Fitzgerald

# Output: The Great Gatsby by F. Scott Fitzgerald

# The __str__ method is used to control what should be returned when the class object is represented as a string. In this case, it defines how a Book object should be printed.
