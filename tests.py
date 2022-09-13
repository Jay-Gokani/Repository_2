# The Anti-Security Bot

known_users = ["Jay", "Dan", "Eddie", "George", "Harry"]
# The known users in the system

while True:
    print("Hi! My name is Rob Oto")
    name = input("What is your name?: ").strip().capitalize()

# We have two methods on the end to strip any blank space at the end and to capitalize the first letter, in case a name is entered like 'jay'
   
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()

# We added lower at the end of the line to convert their response to lowecase

        if remove == "y":
            known_users.remove(name)

# This remove function only removes the first occurance of the name

    else:
        print("Name not recognised")
