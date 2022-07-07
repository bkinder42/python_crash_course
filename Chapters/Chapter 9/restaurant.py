class Restaurant:
    """Models a restaurant"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine 
        self.number_served = 0

    def describe(self):
        print(f"This is {self.name} and we serve {self.cuisine} food.")

    def open(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavors):
        super().__init__(name, cuisine)
        self.flavors = flavors
    
    def get_flavors(self):
        print("The flavors we have today are: ")
        for flavor in self.flavors:
            print(f"\t- {flavor}")