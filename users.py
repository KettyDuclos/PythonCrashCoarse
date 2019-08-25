""" classes that can be used to represent different aspects of a user"""

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

class Privileges():
    """Initialize privilege attributes"""
    
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        admin_privileges = ''
        for privilege in self.privileges:
            admin_privileges += " " + privilege
        print("The following privileges are granted to Admins: " + admin_privileges)
    

class Admin(User):
    """Represents aspects of a user, specific to admin"""

    def __init__(self, first_name, last_name, email, password):
        """Initializes attributes of the parent  class
           Then initializes attributes specific to Admin"""

        super().__init__(first_name, last_name, email, password)
        self.privileges = Privileges()






