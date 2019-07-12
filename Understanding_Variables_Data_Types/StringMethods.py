# accessing characters in a string

city = "draper"
print(city[5])  # index will always start from 0

print("draper"[4])

"""
len()
upper()
lower()
str()
"""
FN = "MISSISSIPPI"
print(len(city))
print(city.upper())
print(FN.lower())
print("char at position 6: " + FN[5])   # Concatenation
print(FN + str(3))  # convert the int object to string object

"""
How to replace a string?
"""
river = "MISSISSIPPI"
print(river.replace("SS", "ss").replace("PP", "pp").replace("I", "i").replace("M", "m"))
print(river.replace("SS", "ss", 1))

"""
substring methods
aka: String slicing and indexing
In a substring range, the starting index in inclusive and ending index in exclusive
city[1:6]
1 is inclusive and 6 is exclusive
"""
city = "mississippi"
print(city[2:5])
print(city[1:9:3])
print(city[::-1])
print(city[:-1])

"""
String Operators
"""
# Concatenation
a = "Jurassic " + "Park"
print(a)

# Repetition
b = "Cat "
print(b*5)

# Slice
print(a[4])

# Slice Range
print(a[2:5])

# in & non in: These will return a boolean depending upon the condition
print("M" in "Mushroom")
print("M" in "Banana")
print("M" not in "Mushroom")
print("M" not in "Banana")

# r: suppresses an escape sequence
a = "1 " + "\t" + " billion " + "trees"
b = "1 " + r"\t" + " billion " + "trees"
print(a)
print(b)

"""
String Methods
Reference: https://www.quackit.com/python/reference/python_3_string_methods.cfm
"""
# Upper
print("san francisco".upper())

# Lower
print("SAN FRANCISCO".lower())

# Padding
City = "SAN FRANCISCO"
Padding = City.center(27, "*")
print(Padding)

a = "I felt happy because I saw the others were happy and because I knew I should feel happy, \
but I wasn’t really happy."
print(a.count("happy"))
print(a.count("I"))

b = "Mississippi Mushroom Magic"
print(b.count("M", 2, 25))

"""
String formatting
"""
City = "Salt Lake City"
Performance = "Magic"

Event = "Welcome to " + City + " and enjoy the " + Performance + " show"    # method 1
print(Event)

print("Welcome to %s and enjoy the %s show" % (City, Performance))  # method 2



