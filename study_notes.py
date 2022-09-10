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
from pickle import FALSE, TRUE
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


string.method()
# this is the formal for running a test on a string e.g.

"hello".count("e")
# this counts the number of the letter 'e's that appear in hello, which is 1

message = "Happy Birthday"
message.count("day")
#this works with functions, here 1 returns

message.upper()
> HAPPY BIRTHDAY

message.capitalize()
> Happy birthday

message.title()
> Happy Birthday

message.lower()
> happy birthday

message
> Happy Birthday

# The string didn't change as strings are unmutable, it can be overwritten though

message = message.upper()
message =
> HAPPY BIRTHDAY

message.islower()
> FALSE

message.isupper()
> TRUE

message.isalpha()
> FALSE
#Shows if everything is alphabetic. False as there is a space

message.isdigit()
> FALSE

message.isalnum()
> FALSE
# This shows whether alphanumeric

message.index("birthday")
> 6
# This shows the index number of where "birthday" is found, which is index number 6. h = 1, a = 2, p = 3, p = 3, y = 4, space = 5, b = 6

message.index("hadsgiwd")
> -1
# This shows that the string does not exist
# Index is case sensitive
# Could be useful first converting the string to a particular case then running index

x = "000yes000"
x.strip("0")
> yes
# The 0's have been stripped

x.lstrip("0")
x.rstrip("0")
# These strip from the left or right side only

x.strip()
# This strips the spaces

len(x)
# Shows the length (num characters) of a string

name = input("what is your name?").strip
# If someone types "Jay  " it will strip the spaces

