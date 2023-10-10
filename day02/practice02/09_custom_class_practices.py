"""

9. Create a python file named custom_class_practices:
    9.1 Create a custom class named Pizza:
    Attributes:
        size, numberOfCheeseTopping, numberOfPepperoniTopping

        Add a constructor that can set all the fields

    Actions:
        calcCost(): returns the totalCost of the pizza
        __str__():returns a String containing the pizza size,quantity of each topping and the pizza cost as calculated by calcCost()

    Pizza cost is determined by:
                    S: $10 + $2 per topping
                    M: $12 + $2 per topping
                    L: $14 + $2 per topping



    9.2 Create a class named Circle:
            Attributes:
                instance: radius
                static: pi

            Add a constructor that can set All the fields (instances)

            Actions:
                calcArea(): returns the area of Circle

                calcPerimeter(): returns the perimeter of Circle

                __Str__(): displays the radius, diameter, pi, area and perimeter of the circle when the object of circle is passed in the print statement



"""
import math


class Pizza:
    def __init__(self, size, number_of_cheese_topping, number_of_pepperoni_topping):
        self.size = size
        self.number_of_cheese_topping = number_of_cheese_topping
        self.number_of_pepperoni_topping = number_of_pepperoni_topping

    def calc_cost(self):
        size_cost = {"S": 10, "M": 12, "L": 14}

        cost = size_cost.get(self.size, 0) + (2 * (self.number_of_cheese_topping + self.number_of_pepperoni_topping))

        return cost

    def __str__(self):
        return f"Size: {self.size}, Cheese Toppings: {self.number_of_cheese_topping}, Pepperoni Toppings: {self.number_of_pepperoni_topping}, Cost: ${self.calc_cost():.2f}"


pizza1 = Pizza("S", 1, 1)
print(pizza1)

pizza1 = Pizza("M", 2, 3)
print(pizza1)

pizza1 = Pizza("L", 5, 10)
print(pizza1)


class Circle:
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        area = Circle.pi * self.radius * self.radius

        return area

    def calc_perimeter(self):
        perimeter = 2 * Circle.pi * self.radius

        return perimeter

    def __str__(self):
        diameter = 2 * self.radius
        return f"Radius: {self.radius}, Diameter: {diameter}, Pi: {Circle.pi}, Area: {self.calc_area():.2f}, Perimeter: {self.calc_perimeter():.2f}"


circle1 = Circle(10)
print(circle1)
