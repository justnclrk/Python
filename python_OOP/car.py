# Assignment: Car
# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 
# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.
class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax):
        #attributes
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
        #methods
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print self.price
        print self.speed
        print self.fuel
        print self.mileage
        print self.tax
car2 = Car(8000, '50mph', 'Full', '35mpg', '')
car3 = Car(12000, '60mph', 'Kind of Full', '45mpg', '')
car4 = Car(7000, '70mph', 'Full', '55mpg', '')
car5 = Car(10000, '80mph', 'Empty', '65mpg', '')
car6 = Car(15000, '90mph', 'Kind of Full', '75mpg', '')