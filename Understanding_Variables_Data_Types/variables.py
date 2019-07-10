# 1. Variable Assignment

# A variable is a name attached to a particular object
a = 100
print(type(a))

# Assignment is done through a single equals sign (=)
print("value of variable 'a': " + str(a))
print(type(a))

# Changing the value
a = 200
print(type(a))
print("value of variable 'a': " + str(a))
print(type(a))

# Chained assignment
a = b = c = 500
print(a, b, c)

# 2. Variable Types in Python

# In Python, a variable may be assigned a value of one type and then later re-assigned a value of a different type
var = 100
print(var)
print(type(var))

var = "this is a string"
print(var)
print(type(var))

# 3. Object References
# What happens during variable assignment?
"""
When presented with the statement print(500), the interpreter does the following:

Creates an integer object
Gives it the value 300
Displays it to the console
"""
a = 500
print(a)
print(type(a))

# This assignment creates an integer object with the value 500 and assigns the variable n to point to that object.

# 4. Object Identity
"""
In Python, every object that is created is given a number that uniquely identifies it. 
It is guaranteed that no two objects will have the same identifier during any period in which their lifetimes overlap. 
Once an object’s reference count drops to zero and it is garbage collected
"""
a = 400
b = 800
print(id(a), id(b))

a = 4
b = 8
print(id(a), id(b))

# 5. Variable Names

# Variable names cannot begin with number
# 1_a = 2 # this results in SyntaxError: Invalid token during runtime

"""
Naming Conventions:
Camel Case: findChildElements
Pascal Case: FindChildElements
Snake Case: find_child_elements

Snake Case should be used for functions and variable names
Pascal Case should be used for class names
"""

# Reserved Keywords
# No object can have the same name as a reserved word.
"""
Following are the reserved keywords in python:
False,def,if,raise,None,del,import,return,True,elif,in,try,and,else,is,while,as,except,lambda,with,assert,finally,
nonlocal,yield,break,for,not,class,from,or,continue,global,pass
"""