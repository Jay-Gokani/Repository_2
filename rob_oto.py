# Rob Oto: The Anti-Security System

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
            print("You have been removed from the system")
        elif remove == "n":
            print("No worries, I'll keep you on the list!")

# This remove function only removes the first occurance of the name

    else:
        print("I don't think we've met yet, {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No problem, catch you around!")
