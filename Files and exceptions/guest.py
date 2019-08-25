filename = 'guest_name.txt'

name = input("Tell me your name please: ")

with open(filename, 'w') as file_object:
    file_object.write(name)
