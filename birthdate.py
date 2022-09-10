# Ask user for DoB
birth = input("What is your date of birth (e.g. 14/03/1990?)").strip()

# Slice day
day = birth[:2]

# Slice month
month = birth[3:5] 

# Slice year
year = birth[6:]

# Output
print("You were born on day {} of month {} in the year {}".format(day, month, year))