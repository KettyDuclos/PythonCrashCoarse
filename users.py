class User():
    """A simple attempt to model a website user"""

    def __init__(self, first_name, last_name, email, password):
        """initialzes attributes to describe user"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def describe_user(self):
        print("Quick summary of user, name: " + self.first_name +self.last_name +
         "email and password is: " + self.email + self.password
        )

    def greet_user(self):
        print("Hello " + self.first_name + " , welcome to our site")


user = User("Ketty", "Duclos", "kettyD@yahoo.com", "password")

user.describe_user()
user.greet_user()

