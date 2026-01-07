import json

def load_students():
    with open("students.json", "r") as file:
        return json.load(file)



def add_student(students):
    name = input('Donner votre nom :')
    score = int(input('votre Score : '))
    students.append({"name": name, "score": score})

def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=3)

def show_students(students):
    for student in students:
        print(f"name : {student['name']} - score : {student['score']}")        



def best_student(students):
    best = students[0]
    for student in students:
        if student['score'] > best['score']:
            best = student
    return best['name']

def average_score(students):
    total = 0
    for student in students:
        total += student['score']
    return total / len(students)        

def delete_student(students):
    name = input("Enter name to delete: ")
    for student in students:
        if student['name'] == name:
            students.remove(student)
            print("Student deleted")
            return
    print("Student not found")
    

def update_student(students):
    name = input("Enter name to update: ")
    for student in students:
        if student['name'] == name:
            new_score = int(input("New score: "))
            student["score"] = new_score
            print("Score updated")
            return
    print("Student not found")        

students = load_students()


while True:
    print("1. Show all students")
    print("2. Add students")
    print("3. Show best student")
    print("4. Show average score")
    print("5. Delete Student")
    print("6. Update Student") 
    print("0. Exit")
    
    choice = input("Choose option: ")
    if choice == '1':
        show_students(students)
    elif choice == '2':
        add_student(students)
    elif choice == '3':
        print("Best student:", best_student(students))              
    elif choice == '4':
        print("Average score:", average_score(students))
    elif choice == '5':
        delete_student(students)  
        save_students(students)
    elif choice == '6':
        update_student(students)   
        save_students(students)   
    elif choice == '0':
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice, try again.")

