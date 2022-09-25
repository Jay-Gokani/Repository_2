# Explain to the user that this is a dating profile creator
print("This is a dating profile creator. Please input the following fields and your profile text will be printed!")

# Ask user for name
name = input("What is your name?: ")

# Ask user for age
age = input("What is your age?: ")

# Ask user for city
city = input("Which city do you live in?: ")

# Ask user for country
country = input("Which country do you live in?: ")

# Ask user for hobby
hobby = input("What is your favourite hobby?: ")

# Ask user for favourite food
food = input("What is your favourite food?: ")

# Create output text
string = "Hello! My name is {}, I am {} years old and you live in {}, {}. {} is my favourite hobby - which I really love! {} is my favourite food. I hope to chat with you soon!"

output = string.format(name, age, city, country, hobby, food)

# Print output to screen
print(output)

