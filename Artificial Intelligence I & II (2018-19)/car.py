import random
from JUNIOR.AI.vehicle import Vehicle
chicken = 7
class Car(Vehicle):
    """A simple attempt to model a car."""
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        super().__init__(make, model, year)
 # Fuel capacity and level in gallons.
        self.fuel_capacity = 15.
        self.fuel_level = 0.
    def get_fuel(self):
        return self.fuel_level
    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        self.fuel_level -= random.uniform(0.,10.)
        print("The car is moving.")
    def print(self):
        print(self.make+" "+self.model+" "+str(self.year))
