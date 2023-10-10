import numbers


class Employee:
    is_human = True     # similar to static variable of Java
    planet = 'Earth'    # similar to static variable of Java

    # def __init__(self, name: str = None, job_title: str = None, salary: numbers = None):
    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')

    # toString() method in JAva
    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


employee1 = Employee()

print(employee1.name)               # Output: Unknown

print(employee1.job_title)          # Output: Janitor

print(employee1.salary)             # Output: 0

print('---------------------------------------------------------')

employee2 = Employee('Daniel')

print(employee2.name)               # Output: Daniel

print(employee2.job_title)          # Output: Janitor

print(employee2.salary)             # Output: 0

print('---------------------------------------------------------')

employee3 = Employee('Breanna', 'SDET')

print(employee3.name)               # Output: Breanna

print(employee3.job_title)          # Output: SDET

print(employee3.salary)             # Output: 0

print('---------------------------------------------------------')

employee4 = Employee('Yulia', 'Python Developer', 150_000)

print(employee4.name)               # Output: Yulia

print(employee4.job_title)          # Output: Python Developer

print(employee4.salary)             # Output: 150000

print('---------------------------------------------------------')

print(Employee.is_human)            # Output: True

print(Employee.planet)              # Output: Earth

print(Employee.__name__)            # Output: Employee

print('---------------------------------------------------------')

employee1.work()                    # Output: Unknown is working

employee2.work()                    # Output: Daniel is working

employee3.work()                    # Output: Breanna is working

employee4.work()                    # Output: Yulia is working

print('---------------------------------------------------------')

print(employee1)                    # Output: Employee{'name': 'Unknown', 'job_title': 'Janitor', 'salary': 0}

print(employee2)                    # Output: Employee{'name': 'Daniel', 'job_title': 'Janitor', 'salary': 0}

print(employee3)                    # Output: Employee{'name': 'Breanna', 'job_title': 'SDET', 'salary': 0}

print(employee4)                    # Output: Employee{'name': 'Yulia', 'job_title': 'Python Developer', 'salary': 150000}
