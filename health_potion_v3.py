import random

Health = 50

Vial = random.randint(25,50)
Potion = random.randint(50,75)
Elixer = random.randint(75,100)

Selection = input("Your current Health is 50. Would you like to use the Vial, Potion or Elixer?")

if Selection == "Vial":
  New_Health = (Health + Vial)
  print("Your New Health increased to", New_Health)

elif Selection == "Potion":
  New_Health = (Health + Potion)  
  print("Your New Health increased to", New_Health)

elif Selection == "Elixer":
  New_Health = (Health + Elixer) 
  print("Your New Health increased to", New_Health)

else:
    print("Try again")
# This programme works besides the else line, as when a random statement is inputted, then a correct input is entered, it just shows the number for the input rather than New_Health
