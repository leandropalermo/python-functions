import random

# List Comprehension
names = ["leandro", "Ayla", "Eduarda", "Beatriz", "Cecilia", "Paula"]
short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)

# Dictionary Comprehension
students_score = {student: random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_score.items() if score > 70}

#Looping through dictionaries
student_dict = {
    "student": ["Ayla", "Beatriz", "Eduarda"],
    "score": [56, 76, 88]
}
for (key, value) in student_dict.items():
    print(key)
    print(value)

#Looping through pandas library
import pandas
student_df = pandas.DataFrame(student_dict)
print(student_df)

for (index, row) in student_df.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
