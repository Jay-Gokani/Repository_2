# question
choice = input("Type something and I will tell you how many vowels, consonants and spaces it has!: ")

# initial count
vowels = 0
consonants = 0
spaces = 0

# question count
for letter in(choice):
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        spaces = spaces + 1
    else: 
        consonants = consonants + 1

# vowel count
if vowels == 0:
    print("There are 0 vowels")
elif vowels == 1:
    print("There is 1 vowel")
else:
    print("There are {} vowels".format(vowels))

# consonant count
if consonants == 0:
    print("There are zero consonants")
elif consonants == 1:
    print("There is 1 consonant")
else:
    print("There are {} consontants".format(consonants))

# spaces count
if spaces == 0:
    print("There are zero spaces")
elif spaces == 1:
    print("There is 1 space")
else:
    print("There are {} spaces".format(spaces))