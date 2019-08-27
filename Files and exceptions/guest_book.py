filename = 'guest_book.txt'

prompt = "/n Please enter your name: "
prompt += "/n Enter 'quit' to end the program: "

name = ""

while name != 'quit':
    name = input(prompt)
    print("Hello " + name)
    
    with open(filename, 'a') as file_object:
        file_object.write(name)
        

