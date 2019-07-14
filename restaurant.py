class Restaurant():
    """Simple attempt a modeling a Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a car"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This is " + self.restaurant_name)
        print("We server " + self.cuisine_type + " cuisine")

    def open_restaurant(self):
        print(self.restaurant_name + " is open for business!")


restaurant = Restaurant("The Island Spot", "West Indian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
        