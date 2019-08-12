"""
List; Is a type of container in data structures, which is used to store multiple data at the
same time
"""
cars = ["bmw", "benz", "audi", "honda", "toyota"]
print(cars)
print(len(cars))
print(cars[1])

# create an empty list
empty_list = []
print(empty_list)

# create a list with a string
string_list = ["this is a string"]

# create a list with multiple items
str_list_1 = ["this", "is", "a", "string"]
print(str_list_1[1])

# create a list with mixed type of values
str_list_2 = ["abc", 123, 123.45, "string"]
print(str_list_2)

# changing the values inside the list
str_list_2[0] = 456
print(str_list_2)

# built-in methods of List
str_list_2.append(345)  # add the object at the end of the list.
print(str_list_2)

# how to add an item at the desired index in the list
cars.insert(1,"Jeep")
print(cars)

# how to find the index of an element inside the list
print(cars.index("honda"))

# how to remove an item from the list
# pop function by default removes an item from the end
# append function by default adds an item at the end
cars.pop()
print(cars)

cars.remove("Jeep")
print(cars)

# slicing the list. syntax: List_Name[start_index: end_index], ending index will not be included
print(cars[1:])
print(cars[::-1])   # print list in reverse order

# sorting the list
cars.sort()
print(cars)

a = ["I","like","python","coding"]
print(' '.join(a))
