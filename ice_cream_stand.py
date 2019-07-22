from restaurant import Restaurant


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

        
