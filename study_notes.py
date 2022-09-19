# ===============================================
# VARIABLES

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

# ===============================================
# MATH

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

from email.errors import MalformedHeaderDefect
import math
from pickle import FALSE, TRUE
from re import L
from xml.dom.pulldom import SAX2DOM
math.floor(1.5)
# Rounds down to the nearest integer

math.ceil(1.5)
# Rounds up to the nearest integer

9 ** 2
# Exponential

# Whole numbers are integers, decimal numbers are floats

# ===============================================
# STRINGS

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
# This shows the index number of where the element "birthday" starts, which is index number 6
# Index elements start from 0

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

a = "sadboy"
a[0]
> h

a[start:end:step]
a[0:3:1]
> sad

# minus 1 from the start, go to the end

a[:3]
# This gives everything up to element 3

a[2:]
# This gives from the second element to the end

a[::-1]
# Goes from end to start reversing the string

a[-1]
# The very end value is -1
# This could be useful for getting say the 3rd to final element as it would be -3, rather than counting from the start

a(a.index("boy"))
> 3
# Shows which index "boy" starts from

a[a.index("sad"):a.index("boy")]
# The square brackets are important here

# Index only return the first time the slice is mentioned in the string


# ===============================================
# LOGIC
# Boolean is a data type which evaluates whether a statement is True or False
# 2 = 3     using the assignment operator - used for a function
# 2 == 3    using the equality operator - used to set/check if values are equal to eachother

# Logical comparison operators: ==, !=, >, <, <=, >=

2 == 3
> False
# This is evaluating if 2 is equal to 3

a = 100
b = 150

if a>b:
    print("a is bigger than b")
elif a<b:
    print("b is bigger than a")
else:
    print("a=b")

# Operators: combining if with not, and, or

not 4 == 3
> True (it is True that 4 does not == 3)

not 2 < 3
> False (it is False that 3 is not greater than 2)
# The not operator gives the opposite of the input, like a minus sign

C = 10
D = 5

if C > 10 and D > 1:
      print("it worked")
> Error (as both conditions were not satisfied)

if not (C > 10 and D > 1):
      print("it worked")
> "it worked" (false inside the brackets + false from not = true)


c = 5
d = -1

if c > 1 or d > 1:
    print("it worked")
> it worked

# not can be combined with the or to make it negative e.g.

if not (c > 1 or d > 1):
    print("it worked")
> Error

# false and true = false
# false or true = true
# it tries to be true but if both, it's false. If you're bad and good, you're still bad
# in general, not switches the sign of anything - work is out by thinking if a statement is overall positive or negative

#_____ Data Structures: Lists, Tuples, Dictionaries

our_list = [2, "A", 1, 7, TRUE]
print(our_list)
> [2, A, 1, 7, TRUE]
# Lists can have any type of variable

our_list[3]
> 7
# Selects the third element to bring it back

our_list[0:3:1]
> [2, "A", 1]

second_list = [4, 1, [5, 2], 7]
second_list[2][0]
> 5
# There is a list within a list. We queried the second element which is the second list, then then zeroth element within that list
# This follows the normal slicing rules

my_table = [ [1, 2, 3] , [4, 5, 6] , [7, 8, 9] ]

my_table[0]
> [1, 2, 3]

my_table[1]
> [4, 5, 6]

my_table[2]
> [7, 8, 9]

# By doing this, we have rows and cols
# If we carried on with  lists within the above lists, we could make 3D structures, then 4D etc 
# Slices don't modify the list, they just take a copy

my_table[0][1]
> 2
# This is effectively like doing zeroth row, second col

l = [1, 2, 3]
2 in l
> TRUE

known_users = ["Jay", "Dan", "Eddie", "George", "Harry"]

print(len(known_users))
# Prints the length of the list i.e., num of known_users

# Deleting data:

example = [5, 2, 3, 2, 4]

example.remove("2")
print(example)
> [5, 3, 2, 4]
# removed the first occurance of "2"
# good when knowing the value to remove but leaves further occurances

del example[1]
print(example)
> [5, 3, 2, 4]
# removed element number one 
# good when knowing element num and ability to remove all occurances in one line by writing further elements

del example[0:2]
# can also cut out slices

#______ Adding to a list

dogs = ["Milo", "Rox", "Trixy"]
dogs.append("Oscar")
print(dogs)
> ['Milo', 'Rox', 'Trixy', 'Oscar']
# This has added a string item to the list

dogs = ["Milo", "Rox", "Trixy"]
wild_dogs = ["Gruff", "Gnasher"]
dogs.append(wild_dogs)
print(dogs)
['Milo', 'Rox', 'Trixy', ['Gruff', 'Gnasher']]
# This has added a list of strings to a list of strings

A = [5, 1, 6, 3]
A.append(4)
print(A)
# This also works with adding one integer to a list

B = [3, 5, 1, 5]
C = [2, 4]
B.append(C)
print(B)
# This also works with adding a list of integers to a list
# Don't ever do B = B.append(C) as the equal operator will remove the data

A = [5, 1, 6, 3]
A = A + [2, 5]
print(A)
> [5, 1, 6, 3, 2, 5]
# This has added integers to the list

B = [3, 5, 1, 5]
B = B + [[2, 4]]
print(B)
> [3, 5, 1, 5, [2, 4]]
# This has added an integer list to a list of integers
print(B[-1])
# This removes the endmost element i.e. the [2, 4]

c = [3, 2, 6]
c.insert(2, 50)
print(c)
> [3, 2, 50, 6]
# We have inserted the num 50 in element num 2

c.insert(2, [50, 10])
> [3, 2, [50, 10], 6]
# This also works with slices

# Lists are mutable (can be changed), so never write name = name.function , whether that function be remove, append etc

#______ Tuples

# A tuple is like an immutable list, which is good for protecting data
# A string is also immutable

example = (8, "a", 5)
# A tuple is like an immutable list, with no square brackets
# To make it obvious that it's a tuple, using brackets it common practice, but aren't technically neccessery

example[0:1]
> (8)
# Can also slice tuples

A = [1, 2, 3]
# This is a list due to the square brackets
tuple(A)
> (1, 2, 3)
# This has converted the list into a tuple

(A, B, C) = 1, 2, 3
print(A, B, C)
> 1, 2, 3
print(A)
> 1
# Assigning multiple values

#_____ Dictionaries
# They store key-values, so when you look up a variable, it shows the value - like a real dictionary
# Dictionaries don't support indexing, looking via element number, as they don't have an order
# You can either convert to a list or lookup via the key

students = {"Jay": 24, "Eddie": 23, "Dan": 45}
print(students["Dan"])
> 45

students = {"Jay": 24, "Eddie": 23, "Dan": 45}
students ["Fred"] = 27
print(students["Fred"])
> 27
# This has added a new key and can be used to append a key

del students["Fred"]
# This has deleted him

a = list(students.keys())
b = list(students.values())
print(a)
print(b)
# This converts to a list then prints

students.items()
> dict_items([('Jay', 24), ('Eddie', 23), ('Dan', 45)])

# Pulls keys and values
b = list(students.values())[2:]
# Can pull out slices as it's a list


students = {
    "Jay": ["ID1", 24, "A"],
    "Eddie": ["ID2", 23, "B"],
    "Dan": ["ID3", 45, "A"]
    }

print(students["Jay"])
> ['ID1', 24, 'A']
print(students["Dan"][1:])
> [45, 'A']
# Multiple values can be assigned to a key
# Lists can be added for each key. As long as we know the order, we can pull any value back

students = {
    "Jay": {"id": "ID1", "age": 24, "grade": "A"},
    "Eddie": {"id": "ID2", "age": 23, "grade": "B"},
    "Dan": {"id": "ID3", "age": 45, "grade": "A"}
    }
# We have a dictionary inside a dictionary with multiple values assigned to a key here

 print(students["Jay"]["age"])
 > 24
# Looking up a single key

 print(
    students["Jay"]["age"],
    students["Jay"]["grade"]
    )
# Looking up multiple keys

 if choice in films:
        pass
    # pass tells Python to continue with the programme
    else:
        print("Sorry, we don't have that choice")

#_____ Loops

while condition:
    code
# while statement loops something while something is true

print(1)
print(2)
print(3)
print(4)
print(5)
# This works but is long

number = 1

while number <= 5:
    print(number)
    number = number + 1
# A quicker loop

for pancakes in range(1, 11):
    print(pancakes)
# prints a col of 1, 2, 3, 4, 5 up to 10
# notice that the range goes one higher than what we want to include

for pancakes in range(1, 11, 2):
    print(pancakes)
# prints in steps of 2 from 1 to up to but not including 11

#_____ For Loop
# The syntax includes a list, then 
# for *item* in *list:
#   code
# Notice that the name of the items doesn't need to be called before the for loop

my_list = ["apple", "cherry", "melon"]

for item in my_list:
    print(item)
# Goes through the list, printing each item in turn

for item in my_list:
    print(item + ' might be the best fruit')
# The same statement has been added to each item here

even_numbers = [x for x in range(1,11)
    if x % 2 == 0]
print(even_numbers)

words = ("jam", "contains", "strawberries")
item = [ingredient.upper() for ingredient in words]
print(item)

# break statement gets out of the loop and goes to the previous statement
# continue statement does the opposite

#_____ Functions

def name(x, y):
    return operation
# The above is the nomanclature
# The return keyword returns the value. This can be ommited if you don't want it shown, just for the function to operate behind the scenes
# Return is not the same as print, as print does not store the slice

def addition(x, y):
    return x + y

print(addition(5, 10))

> 15

# Functions are useful as it allows for something to be written once then used many times

# This shows that return is not the same as print
def reverse(x):
    return x[::-1]

a = reverse("hello")
print(type(a))
> str

b = print(a)
print(type(b))
> none

# As print only displays the code and does not store, it you have to keep the code in a variable which can be further used and declare a new line to see the result through print, but not using that in further lines of code
def sub (x, y):
    return x - y

a = sub(1, 4)
print(type(a))
# Should be done in two lines
# If we instead printed into the same line, it would be stored as type none

#_____ Variable Scope

# Global = variable can be seen anywhere in the programme
# Local = variable can only been seen in the specific local scope
# Functions create local scopes
# Loops and if statements don't create local scopes

def f1():
    a = 100
    print(a)

def f2():
    print(a)

print(f1)
print(f2)
# f2 fails as "a" was defined in f1's local scope
# If we defined "a" on line one, it would be in global scope and both functions would work
# Functions always create local scope inside themselves
# If we defined "a" in the local scope of f2 as "50", "100" and "50" would print as local scopes are invisibel to either function
# This is good as it means that function names do not overwrite eachother and we don't need to worry about creating unique names - as long as scopes don't overlap
# You can't overwrite a global variable with a local variable
# Local variables are destroyed once the function is

a = 200

def f1():
    b = a + 10
    print(b)

def f2():
    a = 150
    print(a)

# f1 doesn't have a defined, so used the global variable
# f2 has a defined locally, so that takes preference

a = 100

def f1():
    global a
    a = 50
    a + 100

# global a updated inside a variable
# global keyword and definition have to be on seperate lines
# With dictionaries and lists, you don't have to call global, can just edit one index

a = [1, 3, 2]

def f1():
    a[0] = 5
    print (a)

# Parameter = inside the func definition
# Argument = what is called

def about(name, age, likes):
    sentence = "My name is {}, I am {} years old and I like {}".format(name, age, likes)

about("Jay", 24, "footy")
# Name, age and likes are parameters (in function definitions)
# Jay, 24 and footy are arguments (what is passed when function is called)
# The above is an example of positional arguments

about(age = 24, name = "Jay", likes = "football")
# This also works, and are keyword arguments

def about(name, age, likes = "soccer"):
    sentence = "My name is {}, I am {} years old and I like {}".format(name, age, likes)
# Likes is a default parameter
# There can be as many as I want, as long as they go last

#_____ Packing & Unpacking

print(1, 2, 3)

numbers = [1, 2, 3]
print(numbers)
> [1, 2, 3]

numbers = [1, 2, 3]
print(*numbers)
> 1 2 3
# This has unpacked the function and stored each number as a seperate argument

def add(*numbers):
    total = 0
    for number in numbers:
            total = total + number
    return(total)

a = add(1, 2, 3, 4, 5)

print(a)


def about(name, age, likes):
    sentence = "Meet {}, he is {} and likes {}".format(name, age, likes)
    return sentence

dictionary = {"name":"Jay", "age":24, "likes":"footy"}

about(**dictionary)
# One star for normal arguments
# Double star for unpacking keyword arguments

def dict(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))

dict(Lauren = "female", Jay = "male")

> Lauren:female
Jay:male

# It's common convention to use args to mean arguments and kwargs to mean key word arguments

def arg_one(*args):
    for stuff in args:
        print(stuff)
    
my_list = ["honda", "toyota", "rover"]
arg_one = my_list

arg_one = ("honda", "toyota, "rover")

# Either one of these works - an arg is needed when pulling results from a list, but not when in a variable

def kwarg_one(**kwargs):
    for key, value in kwargs.items():
    
example = {key1:value1, key2:value2}

kwarg_one(**example)

