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

print('Sorry guys, the table will not arrive on time. I only have space for two guests.')

y = [x[0], x[1]]
print(y)

y.pop()

print(y)