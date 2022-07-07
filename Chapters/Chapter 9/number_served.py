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

restaurant = Restaurant("Bingle's", "Thai")
restaurant.number_served = 5
print(restaurant.number_served)
restaurant.set_number_served(22)
print(restaurant.number_served)
restaurant.increment_number_served(13)
print(restaurant.number_served)