# Ask user for name
name = input("What is your name?: ")

# Ask user for age
age = input("What is your age?: ")

# Ask user for country
country = input("Which country do you live in?: ")

# Ask user for hobby
hobby = input("What is your favourite hobby?: ")

# Ask user for favourite food
food = input("What is your favourite food?: ")

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {} and {}. What an exceptionally interesting person you are!"

output = string.format(name, age, country, hobby, food)

# Print output to screen
print(output)
