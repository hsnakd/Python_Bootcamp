# Define the Person class
class Person:
    def __init__(self, name: str = 'Unknown', age: int = 1):
        # Initialize private attributes with None
        self.__name = None
        self.__age = None
        # Call setter methods to set initial values
        self.set_name(name)
        self.set_age(age)

    # Getter method for __name attribute
    def get_name(self) -> str:
        # Raises an error if the name is not valid
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')
        return self.__name

    # Setter method for __name attribute
    def set_name(self, name: str):
        # Raises an error if the name is not a string or is empty
        if type(name) != str:
            raise RuntimeError(f'Person name must be a string')
        if name == '':
            raise RuntimeError(f'Person name cannot be empty')
        self.__name = name

    # Getter method for __age attribute
    def get_age(self) -> int:
        return self.__age

    # Setter method for __age attribute
    def set_age(self, age):
        # Raises an error if the age is not within a valid range
        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid age: {age}')
        self.__age = age

    # String representation of the object
    def __str__(self):
        # Removes the name mangling prefix added by Python
        return f'{type(self).__name__}{ str(self.__dict__).replace("_Person__", "")}'


# Instances of the Person class
person1 = Person()
print(person1.get_name())   # Output: Unknown
print(person1.get_age())    # Output: 1

person2 = Person('James')
print(person2.get_name())   # Output: James
print(person2.get_age())    # Output: 1

person3 = Person('Hazel', 27)
print(person3.get_name())   # Output: Hazel
print(person3.get_age())    # Output: 27

# Displaying Instances
print('------------------------------------')
print(person1)              # Output: Person{'name': 'Unknown', 'age': 1}
print(person2)              # Output: Person{'name': 'James', 'age': 1}
print(person3)              # Output: Person{'name': 'Hazel', 'age': 27}
