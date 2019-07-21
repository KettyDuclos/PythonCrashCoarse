class Restaurant():
    """Simple attempt a modeling a Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a car"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This is " + self.restaurant_name)
        print("We server " + self.cuisine_type + " cuisine")

    def open_restaurant(self):
        print(self.restaurant_name + " is open for business!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant('Chez Moi', 'French')
print(restaurant.set_number_served(10))
print(restaurant.increment_number_served(100))