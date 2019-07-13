def make_sandwiches(*toppings):
    for topping in toppings:
        print ('Your sandwich will include ' + topping)

make_sandwiches('lettuce')
make_sandwiches('ham', 'cheese',)
make_sandwiches('turkey', 'bacon', 'cheese', 'tomatoes')

