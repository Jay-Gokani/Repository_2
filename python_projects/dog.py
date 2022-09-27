class Dog:
    def __init__(self, name, age, yawn):
        self.name = name
        self.age = age
        self.yawn = yawn                    # argument
    
    def Age(self):
        if self.age > 1 and self.age < 30:
            return "The dog is not a puppy"
        elif self.age > 25:
            return "The dog holds the Guinness Record for greatest age"
        elif self.age < 1:
            return "The dog is a puppy"
        else:
            return "Please type a valid number"

    def Sleep(self):                        # method
        if self.yawn == True:
            return "The dog fell asleep"
        else:
            return "The dog is not tired" 

jack = Dog("Jack", 34, yawn = False)
print(jack.Age())
print(jack.Sleep())