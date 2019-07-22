from users import *

admin = Admin("Ketty", "Duclos", "kd@yahoo.com", "password")
admin.greet_user()

admin_2 = Admin("Kaleb", "Drane", "kd@yahoo.com", "password")
admin_2.privileges.show_privileges()