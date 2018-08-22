Bob_Tower = {
    'first_name': 'Bob',
    'last_name': 'Tower',
    'age': '83',
    'city': 'Richland',
}

for key,value in Bob_Tower.items():
    print("\nKey: " + key)
    print("Value: " + value)

Chris_Tower = {
    'first_name': 'Chris',
    'last_name': 'Tower',
    'age': '56',
    'city': 'Woodland',
}

Lori_Tower = {
    'first_name': 'Lori',
    'last_name': 'Tower',
    'age': '49',
    'city': 'Kalamazoo',
}

people = [Bob_Tower, Chris_Tower, Lori_Tower]

for person in people:
    print(person)

for person in people:
    for key,value in person.items():
        print("\nKey: " + key)
        print("Value: " + value)


# How to sort a Python dict by value
# (== get a representation sorted by value)
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(xs.items(), key=lambda x: x[1]))
# output [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
#output [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
