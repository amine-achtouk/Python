import json

students = [
  {"name": "Ali", "score": 15},
  {"name": "Amine", "score": 18}
]

name = input('Donner votre nom :')
score = int(input('votre Score : '))

new_student = {"name": name, "score": score}
students.append(new_student)

with open("students.json", "w") as file:
    json.dump(students, file)

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    print(f"name : {student['name']} - score : {student['score']}")

