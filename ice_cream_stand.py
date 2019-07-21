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


class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant, specific to an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class
           Then initialize attributes specific to an Ice Cream Stand"""

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]
        
    
    def describe_flavors(self):
        """returns a string of all available flavors"""
        flavor_string = ''
        for flavor in self.flavors:
            flavor_string += " " + flavor
        return flavor_string
            


stand = IceCreamStand("Burr", "desert")
print(stand.describe_restaurant())
print(stand.describe_flavors())

        
