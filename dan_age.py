# Calling Elements from a Dictionary

# How old is Dan again?

import random

dan_age = random.randint(35, 65)

students = {
    "Jay": {"id": "ID1", "age": 24, "grade": "A"},
    "Eddie": {"id": "ID2", "age": 22, "grade": "A"},
    "Dan": {"id": "ID3", "age": dan_age, "grade": "A+"}
    }

jay_eddie_combo = (
    students["Jay"]["age"] +
    students["Eddie"]["age"]
    )

dan_age_dictionary = (students["Dan"]["age"])

if dan_age_dictionary > jay_eddie_combo:
     print("Dammmmn Dan is {} - that's older than Eddie and Jay combined!".format(dan_age_dictionary))
else:
    print("I guess Dan isn't so old after all, he's only {}!".format(dan_age_dictionary))