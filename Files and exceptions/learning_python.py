filename = 'learning_python.txt'

#reading the entire contents of the file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

#reaading the file line by line
with open(filename) as file_object:
    for line in file_object:
        print(line)


#making a list of lines from the file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    
