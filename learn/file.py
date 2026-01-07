students = [('Ali',15), ('amine', 19), ('walid', 7)]

with open("students.txt", "w") as file:
    for name, grade in students:
        file.write(f"{name}: {grade}\n")