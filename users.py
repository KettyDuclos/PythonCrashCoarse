class User():
    """A simple attempt to model a website user"""

    def __init__(self, first_name, last_name, email, password):
        """initialzes attributes to describe user"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.login_attempt = 0

    def describe_user(self):
        print("Quick summary of user, name: " + self.first_name +self.last_name +
         "email and password is: " + self.email + self.password
        )

    def greet_user(self):
        print("Hello " + self.first_name + " , welcome to our site")

    def increment_login_attempts(self):
        self.login_attempt += 1
        return self.login_attempt

    def reset_login_attempts(self):
        if self.login_attempt == 1:
            self.login_attempt = 0
        return self.login_attempt


user = User("Ketty", "Duclos", "kettyD@yahoo.com", "password")

user.describe_user()
user.greet_user()

print(user.increment_login_attempts())
print(user.reset_login_attempts())




