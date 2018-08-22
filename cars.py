def build_car(make, model, **car_features):
    """Build a dictionary containing everything we know about a car."""
    car = {}
    car['make'] = make
    car['model'] = model
    for key, value in car_features.items():
        car[key] = value
    return car

car_profile = build_car('subaru', 'outback',
                             style='four door',
                             drive='all wheel')
print(car_profile)

car_profile = build_car('subaru', 'crosstrek',
                             deal='lease',
                             style='four door and hatch',
                             drive='front')
print(car_profile)
