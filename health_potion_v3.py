import random

while True:

    health = 50

    vial = random.randint(25,50)
    potion = random.randint(50,75)
    elixer = random.randint(75,100)
    
    selection = input("Your current health is {}. Would you like to use the Vial, Potion or Elixer?: ".format(health)).strip().capitalize()

    if selection == "Vial":
        print("Your New Health increased to {}".format(health + vial))

    elif selection == "Potion":
        print("Your New Health increased to {}".format(health + potion))

    elif selection == "Elixer":
        print("Your New Health increased to {}".format(health + elixer))

    else:
        print("Try again")

    
# This programme works, but I want to figure out how to loop it
# This programme now loops but it 

