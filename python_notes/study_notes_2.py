# Topics to refresh on:

# Loops: for,
# Classes (OOP) example


# RETURN (when executing a function)

def change_sign_print(num):
    print(-1 * num)

change_sign_print(3)
> -3

result_print = print(change_sign_print(3))
print(result_print)
> none      # as nothing is stored in a variable


def change_sign_return(num):
    return(-1 * num):

change_sign_print(3)
> -3

result_return = change_sign_print(3)
print(result_return)
> -3

# LIST (ordered, mutable, allows duplicates, square brackets)

ages = [22, 24, 26, 23]

ages.append(25)            
ages.remove(22)
ages.reverse()
ages.index(24)


# TUPLE (ordered, immutable, allows duplicates, round brackets)

ages_2 = (22, 24, 26, 23)


# SET (unordered, unchangeabe, allows duplicates, can add or delete, stores multiple items in a single variable, set keyword)

ages_3 = set([22, 24, 26, 23])


# DICTIONARY (ordered, mutable, key-value pairs, curly brackets)

calories = {"apple" : 52, "choco" : 109, "cherry" : 23}

52 in calories.values()     # True
print(calories['apple'])    # 52

# Values are found through looking up key or value

# WHILE LOOP (while a certain condition is True, do something)

x = 5

while x < 10:
    print(x)
    x += 1          # while x is less than 10, print then add 1

while x < 10:
    print(x)
    if x == 7:
        break
    x += 1          # breaks (stops) the loop at x = 7 

while x < 10:
    x += 1
    if x == 7:
        continue
    print(x)        # misses current iteration then continues

while x < 10:
    print(x)
    x += 1
else:               
    print("x is greater than 10")   # while True, do this, else do that


# FOR LOOP (for name in item, do this)

fruit = ["apple", "cherry", "melon"]

for x in fruit:
    print(fruit)    # loops through each iteration and prints

for x in fruit:
    if x == "cherry":
        continue
    if x == "melon":
        break
    print(x)           # prints each fruit, passes cherry and stops when it reaches melon


for y in range(1,10,2):
    print(y)         


# CLASS

# Class variables are associated to the class and affect all instances
# Instance attributes are associated to the instance

class Dog:                              # class                         
    def __init__(self, name, age):      # arguments
        self.name = name
        self.age = age
        print("Name is {} and age is {}".format(self.name, self.age))

jack = Dog("Jack", "5")                 # jack is an object/instant

print(jack)
print(jack.age)




class Dog:
    def __init__(self, name, age, yawn):
        self.name = name
        self.age = age
        self.yawn = yawn                    # argument
    
    def Sleep(self):                        # method
        if self.yawn == True:
            return "The dog fell asleep"
        else:
            return "The dog is not tired" 

jack = Dog("Jack", 5, yawn = False)
print(jack.Sleep())