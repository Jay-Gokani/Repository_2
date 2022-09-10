# _____ VARIABLES

# Variable = a box which stores data, has a name and value
number = 1
print(number)

# Variables are case sensitive and can't start with a number. The assignment operator in Py is the = sign

my_number = 1 + 2
print(my_number)
# The statement is evaluated then is printed

my_number = 1 + 2
my_second_number = 3 + 4
print(my_number + my_second_number)
# The result is 10

total = my_number + my_second_number
print(total)
# This makes it quicker

# _____ MATH

print(1 + 2)
# This gives back 3

print(type(0.5))
# This shows class 'float'

print(5 % 3)
# 3 goes into 5 with a remainder of 2, this is a modulo operation to find the remainder of a division

list = 1, 2, 3
print(sum(list))
# This returns 6

round(1.5)
# This rounds to the nearest whole no.

import math
math.floor(1.5)
# Rounds down to the nearest integer

math.ceil(1.5)
# Rounds up to the nearest integer

9 ** 2
# Exponential

# Whole numbers are integers, decimal numbers are floats

# _____ STRINGS

message = "I said "hello""
# This is a broken string - fix by using single quotes

message = 'I said "hello"'

# If you have a complex and long string, put triple speech marks on either end

# As standard, variables store numbers as strings

A + B
# This concatenates strings

"="*20
# This is useful for creating an underline:
====================

A = "part"
B = 1
A + B
# This won't work as a string and integer are not compatible

A + str(B)
# This will work as they are both strings now

"{1} {0}".format(A,B)
# This is a quicker method to print lines as strings. The numbers will print B then A

start = "I like "

middle = "to eat"

end = " pizza"

output = "{0} {1} {2}".format(start,middle,end)

print(output)

