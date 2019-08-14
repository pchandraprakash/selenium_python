"""
Tuple is very similar to list the only difference is tuples are IMMUTABLE
"""
my_list = [1, 'a', 'name', 2.0]
print(my_list)

my_list[1] = 1.1
print(my_list)

"""
define and declare a tuple
"""
my_tuple = (1, 'a', 1.1)
print(my_tuple)
print(my_tuple[1])
print(my_tuple[1:2])
print(my_tuple.index(1.1))

my_tuple_1 = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5)
print(my_tuple_1.count(1), my_tuple_1.count(2), my_tuple_1.count(3), my_tuple_1.count(4), my_tuple_1.count(5))

