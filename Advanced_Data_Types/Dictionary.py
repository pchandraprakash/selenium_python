"""
Dictionary is closely related to hash maps in other languages
Dictionary stores the values in key,value pairs
Syntax: {'k1':'v1', 'k2':'v2'}
key and value are separated by colon and 2 pairs are separated by a comma
Dictionary is heterogenous and its not sequenced and it works on MAPPING, there is NO indexing
Mapping is key,value pair
"""
car = {'make': 'honda', 'model': 'civic', 'year': 2019}
print(car)
print(car.keys())   # list all the keys of dictionary
print(car.values())  # list all the values of dictionary

# print a value associated with a key
print(car['make'], car['model'], car['year'])

# empty dictionary
d1 = {}
d1['one'] = 1
d1['two'] = 2
d1['three'] = 3
print(d1)
print(d1['one'] + d1['three'])
d1['three'] = d1['one'] + d1['three'] + 3
print(d1)

'''
Nested Dictionary
nd = {k1:{'nestk1': 'nestvalue1', 'nestk2': 'nestvalue2'}}
'''
car1 = {'honda': {'model': 'civic', 'body': 'sport', 'year': 2019}, 'toyota': {'model': 'camry', 'body': 'sedan', 'year': 2018}}
print(car1['honda'].get('model'))
print(car1['honda']['body'])
print(car1['toyota']['year'])

'''
dictionary methods
'''
print(car.keys())
print(car1.keys())

print(car.values())
print(car1.values())

print(car.items())
print(car1.items())

car_copy = car.copy()
print(car_copy)
