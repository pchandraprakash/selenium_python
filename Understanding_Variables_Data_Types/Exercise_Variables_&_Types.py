# Exercise: The basics - variables and types

"""
1. Let's start using the Python interactive shell and create some variables.
a. Type "python" at the command-line to start the python interactive shell.
b. Create a variable called "course" and assign it the value "python".
c. Create a variable called "rating" and assign it an integer value (anything you like).
d. Print both variables.
"""
course = "python"
rating = 5
print(course, rating)

"""
2. Let's use Pythagoras theorem to calculate the length of the hypotenuse of a
right-angled triangle where the other sides have lengths 3 and 4.
a. Create variables called "b" and "c" and assign them the values of the sides with
known lengths.
b. Write a mathematical express to calculate the length of the hypotenuse
(REMEMBER: “a-squared equals b-squared plus c-squared").
c. Create a variable "a" that equals the result of the calculation.
d. Print the value of variable "a".
"""
b = 3
c = 4

a = (b**2 + c**2)**(1/2)
print(a)

"""
3. Let's take a look at some data types.
a. Print the data type of each of the variables: a, b, c
b. Can you work out why "a" is different from "b" and "c"?
"""
print(type(a))
print(type(b))
print(type(c))
