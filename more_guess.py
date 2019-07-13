x = ['a', 'b','c']

for guess in x:
    print('Hello' + guess + ' ' + 'you are invited')

print(x[0] + ' ' + 'will not be able to make it.')

x[0] = 'd'

print(x)

for guess in x:
    print('Hello' + ' '+ guess + ' ' + 'you are invited')

print('we have a bigger table, we have space for three more guess')

x.insert(0, 'z')
x.insert(1, 'k')
x.append('s')

print(x)


