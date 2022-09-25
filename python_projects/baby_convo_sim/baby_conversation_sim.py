from random import choice

questions = [
    "Why is the sky blue?", 
    "Do you think there are aliens on Mars?",
    "Is the Moon made of cheese?"]

question = choice(questions)
answer = input("Baby: {} : ".format(question)).lower()

while answer != "just because":
    answer = input("Baby: Whyyy?: ").strip().lower()
    print("Uncle Jim: Say 'just because' if you want him to stop")

print("Baby: Oh.. Okay.")