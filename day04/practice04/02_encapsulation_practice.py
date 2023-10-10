"""

2. Create a python file named encapsulation_practice:
		create a class called Item
		    private variables:
		        name, unit_price, quantity

		    Encapsulate all the fields:
		        Conditions:
		            name can not be empty
		            unit price can not be negative
		            quantity can not be negative

		        If invalid data are given to set the firled, then make sure to throw an error duribg the runtime.
		        	(hint: you can use 'raise RuntimeError('Exception message')')

		    Add a constructor that allows user to set all the fields when the object is created.
		            (If the arguments not valid it should not be set to the instances)

		    Methods:
		        calcCost(): returns the total cost
		        toString(): returns the name, unit price, quantity and total cost info as calculated by calcCost()

"""

class Item :

    def __init__(self, name, unit_price, quantity):
        self.__name = ""
        self.__unit_price = 0.0
        self.__quantity = 0
        self.__total_cost = 0.0

    def get_name(self) -> str:
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')

        return self.__name

    def set_name(self, name: str):
        if type(name) != str:
            raise RuntimeError(f'Person name must be string')

        if name == '':
            raise RuntimeError(f'Person name can not be empty')

        self.__name = name


    def unit_price(self) -> int:
        return self.__unit_price

    def unit_price(self, unit_price):

        if unit_price < 0:
            raise RuntimeError(f'Invalid age {unit_price}')
        self.__unit_price = unit_price




print('----------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------')




class Item:
    def __init__(self, name, unit_price, quantity):
        self.__name = ""
        self.__unit_price = 0.0
        self.__quantity = 0
        self.__total_cost = 0.0

        # Validate and set the attributes
        if name and unit_price >= 0 and quantity >= 0:
            self.__name = name
            self.__unit_price = unit_price
            self.__quantity = quantity
            self.__total_cost = self.calcCost()

    def calcCost(self):
        if self.__unit_price < 0 or self.__quantity < 0:
            raise RuntimeError("Unit price and quantity cannot be negative")
        return self.__unit_price * self.__quantity

    def toString(self):
        return f"Name: {self.__name}, Unit Price: {self.__unit_price}, Quantity: {self.__quantity}, Total Cost: {self.__total_cost}"


# Example usage:
try:
    item1 = Item("Widget", 10.0, 5)
    print(item1.toString())

    item2 = Item("", -5.0, 3)
    # This should raise an error for invalid data
except RuntimeError as e:
    print("Error:", e)
