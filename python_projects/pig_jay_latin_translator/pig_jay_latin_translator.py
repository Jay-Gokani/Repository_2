 # get sentence from user

original = input("Please type a sentence: ").lower().strip()

# split sentence into words

individuals = original.split()
# This function splits a sentence into individual words

# loop through words and convert to pig latin

latin = []

# if starting with a vowel, add "yay"

for word in individuals:
    
    # if the first letter is a vowel
    if word[0] in "aeiou":
        new_word = word + "jay"
        latin.append(new_word)

    # when looping through consonants 
    else:
        vowel_index = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_index = vowel_index + 1
            else:
                break
        
        cons = word[:vowel_index]
        the_rest = word[vowel_index:]
        
        new_word = the_rest + cons + "ay"
        latin.append(new_word)


output = " ".join(latin)

print(output)