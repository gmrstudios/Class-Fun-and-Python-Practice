my_pizzas = ['pepperoni', 'sausage', 'onion']

for pizza in my_pizzas:
    print("I like " + pizza )

cubes = [value**3 for value in range(1,11)]
print(cubes)

friend_pizzas = my_pizzas[:]

for pizza in friend_pizzas:
    print("Tom likes " + pizza )

my_pizzas.append('garlic')

friend_pizzas.append('tomato')

print("\nMy favorite pizzas are")

for pizza in my_pizzas:
    print(pizza)

print("\nTom's favorite pizzas are")

for pizza in friend_pizzas:
    print(pizza)

buffet = ('Swiss Steak', 'Egg Rolls', 'Clam Chowder')

print(buffet[0])
print(buffet[1])

#Python rejects change to a tuple buffet [1] = 'Sirloin'
"""Traceback (most recent call last):
  File "pizza.py", line 33, in <module>
    buffet [1] = 'Sirloin'
TypeError: 'tuple' object does not support item assignment"""

print("\nOriginal Menu")
for food in buffet:
    print(food)

buffet = ('Salibury Steak', 'Egg Foo Yung', 'Manhattan Clam Chowder')

print("\nModified Menu")
for food in buffet:
    print(food)
