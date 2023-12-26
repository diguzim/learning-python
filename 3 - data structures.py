# lists

fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed = ['apple', 1, True, 3.14]

first_fruit = fruits[0]
fruits[1] = 'pear'
fruits.append('orange')
fruits.remove('cherry')
print(fruits)

# tuples

coordinates = (1, 2)
colors = ('red', 'green', 'blue')
print(coordinates[0])
# This would result in an error:
# coordinates[0] = 3

# sets

fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
fruits.remove('cherry')
print(fruits)

# dictionaries

person = {
    'name': 'Rodrigo',
    'age': 34,
    'height': 1.75,
    'loves_coding': True
}

print(person['name'])
person['age'] += 1
person['city'] = 'São Paulo'
del person['loves_coding']
print(person)