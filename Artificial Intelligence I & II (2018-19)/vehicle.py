class Vehicle():
    make = ""
    model = ""
    year = 0

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0.
    def drive(self):
        """Simulate driving."""
        self.fuel_level -= random.uniform(0.,10.)
        print("The vehicle is moving.")
