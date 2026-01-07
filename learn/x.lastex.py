import json

students = [
    {"name": "Ali", "score": 15},
    {"name": "Amine", "score": 18}
]

with open("students.json", "w") as file:
    json.dump(students, file)

with open("students.json", "r") as file:
    students = json.load(file)

avg = sum(s["score"] for s in students) / len(students)
print(avg)
