class Person:
    def __init__(self, name: str, age: int):
        # Constructor to initialize name and age
        self.name = name
        self.age = age

    def __str__(self):
        # String representation of the object
        return f'{type(self).__name__}{self.__dict__}'


class Employee(Person):
    def __init__(self, name: str, age: int, job_title: str, company_name: str = 'Unknown', salary: int = 0):
        # Constructor calling parent class' constructor
        super().__init__(name, age)
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        # Work behavior for employees
        print(f'{self.name} is working')


class Developer(Employee):
    # Right Click ==>  Generate ==> Override Methods ==> Select method
    def work(self):
        # Work behavior for developers
        print(f'{self.job_title} {self.name} is coding')


class Teacher(Employee):
    def __init__(self, name: str, age: int, job_title: str = "Teacher", company_name: str = 'Unknown', salary: int = 0):
        # Constructor calling parent class' constructor
        super().__init__(name, age, job_title, company_name, salary)

    def work(self):
        # Work behavior for teachers
        print(f'{self.name} is teaching')


# Example Usage
employee1 = Employee('Hazel', 27, 'QA', 'Apple Inc')
developer0 = Developer('Jack', 39, 'Java Developer')
developer1 = Developer('Daniel', 35, 'Python Developer', 'Google Inc', 100_000)
teacher = Teacher('Breanna', 45)

# Output the string representation of instances and their specific work behaviors

print(employee1)  # Output:Employee{'name': 'Hazel', 'age': 27, 'job_title': 'QA', 'company_name': 'Apple Inc', 'salary': 0}
print(developer0)  # Developer{'name': 'Jack', 'age': 39, 'job_title': 'Java Developer', 'company_name': 'Unknown', 'salary': 0}
print(developer1)  # Output:Developer{'name': 'Daniel', 'age': 35, 'job_title': 'Python Developer', 'company_name': 'Google Inc', 'salary': 100000}
print(teacher)  # Output:Teacher{'name': 'Breanna', 'age': 45, 'job_title': 'Teacher', 'company_name': 'Unknown', 'salary': 0}

employee1.work()  # Output:Hazel is working
developer1.work()  # Output:Python Developer Daniel is coding
teacher.work()  # Output:Breanna is teaching
