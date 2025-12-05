# students = [
#     {"name": "Ali", "age": 20, "grades": {"Math": 80, "Physics": 70, "Chemistry": 90}},
#     {"name": "Sara", "age": 22, "grades": {"Math": 60, "Physics": 55, "Chemistry": 65}},
#     {"name": "Hassan", "age": 21, "grades": {"Math": 40, "Physics": 50, "Chemistry": 45}}
# ]

# def check_students(students):
#     for student in students:
#         print(f"Student: {student['name']}, Age: {student['age']}")
#         for module, grade in student['grades'].items():
#             if grade >= 60:
#                 print(f'✅ module {module}: Passed ({grade})')
#             else:
#                 print(f'❌ module {module}: failed ({grade})')    



# check_students(students)

def check_age(age):
    if age > 18:
        return 'adult'
    else:
        return 'child'    
    

age = 19
res = check_age(age) 
print(res)    




dict.keys()