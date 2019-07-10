# Integers
a = 100
print(a)
print(type(a))

print("This is binary: " + str(0b10))  # binary
print("This is octal: " + str(0o10))  # octal
print("This is hexadecimal: " + str(0x10))  # hexadecimal

print("**********")

# Floating point numbers
a = 3.14
print(a)
print(type(a))

b = 2e-234  # floating point numbers with scientific notation(s)
c = 2e120

print(b, c)
print(type(b), type(c))

print("**********")

# Complex numbers
a = 2+3j
print(a)
print(type(a))

print("**********")

# Boolean
print(2 < 3)
print(type(2 < 3))

print("**********")

# Arithmetic operations

print(2 + 4)    # addition
print(3 - 2)    # subtraction
print(2 * 3)    # multiplication
print(4 / 2)    # division
print(4 % 2)    # modulus without remainder
print(5 % 2)    # modulus with remainder

print("**********")

# Exponentiation
a = 10 * 2  # multiplication
b = 10 ** 2     # exponential
print(a)
print(b)

print("**********")
# order of precedence
print(900/(6+(3*4))-10)
"""
Parentheses (simplify inside 'em)
Exponents
Multiplication and Division (from left to right)
Addition and Subtraction (from left to right)
"""