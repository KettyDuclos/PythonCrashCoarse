def build_cars(make, model, **optional):
    car = {}
    car['manufacture'] = make
    car['model'] = model
    for key, value in optional.items():
        car[key] = value
        return car

my_car = build_cars('Toyota', 'Camry', Color = 'White', Edition = 'Special Edition')
print(my_car)
