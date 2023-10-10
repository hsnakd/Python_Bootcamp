from typing import final

# Using final for Constants
pi: final = 3.14

pi = 3.5  # Error: Redeclared 'pi' defined above without usage

print(pi)  # Output: 3.5


# Using @final for Classes and Methods
@final
class Animal:
    pass


class Dog(Animal):  # Error: 'Animal' is marked as '@final' and should not be subclassed
    pass


# The @final decorator prevents subclassing, so creating a subclass (like Dog) will result in an error.

class Employee:
    @final
    def work(self):
        print('Working')


class Driver(Employee):
    def work(self):  # Error: 'Employee.work' is marked as '@final' and should not be overridden
        print('Driving')


# The work method in Driver cannot override the final method in Employee, so calling Driver().work() would result in an error.

class Person:

    def __init__(self, age: int):
        self.__age = age

    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, value):
        raise RuntimeError(f' age is constant, can not be changed')


person1 = Person(10)

print(person1.person_age)       # Output: 10

# person1.person_age = 100      # Output: RuntimeError:  age is constant, can not be changed
# This line would raise a RuntimeError since the person_age property has a setter that raises an error.

print(person1.person_age)       # Output: 10

# print(person1.__age)           # Output: IndentationError: unexpected indent
# This line would result in an AttributeError because __age is a private attribute and cannot be accessed directly.
