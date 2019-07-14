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


location_1 = Restaurant('Peruvian Vibes', 'Peruvian')
location_2 = Restaurant('The Red White and Blue', 'American')
location_3 = Restaurant('Zen Garden', 'Thai')

location_1.describe_restaurant()
location_1.open_restaurant()

location_2.describe_restaurant()
location_2.open_restaurant()

location_3.describe_restaurant()
location_3.open_restaurant()
