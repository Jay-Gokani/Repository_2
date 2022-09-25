import random

while True:

    health = 50

    vial = random.randint(25,50)
    potion = random.randint(50,75)
    elixer = random.randint(75,100)
    
    selection = input("Your current health is {}. Would you like to use the Vial, Potion or Elixer?: ".format(health)).strip().capitalize()

    if selection == "Vial":
    confirm_vial = input("Your New Health will increase to {}. Are you sure you want to use the Vial?".format(health + vial))
        if confirm_vial == "y":
            print("Your new health has increased to {}".format(health + vial))
        elif confirm_vial == "n":
            # Need a statement which takes the user back to the selection stage, maybe break?
            # If I don't want to do this confirmation step, remove the lines below the if statement
            # If I do, repeate this for the below elif statements

    elif selection == "Potion":
        print("Your New Health increased to {}".format(health + potion))

    elif selection == "Elixer":
        print("Your New Health increased to {}".format(health + elixer))

    else:
        print("Try again")


# I want to add two features to this programme: 
#   confirmation of item choice (which loops back to the selection step if choice is "n"
#   loop so that the health increases which each item used
