person = {
    "name": "Ali",
    "age": 25,
    "grade": "18"
}

person['city'] = 'agadir'

person["grade"] = 19

del person["age"]

for key, value in person.items():
    print(f'{key} : {value}')


n = int(input("Donner la taille du tableau : "))

T1 = []
T2 = [2,5,6,4]

for i in range(n):
    x = int(input(f"T1[{i}] = "))
    T1.append(x)

# Copie
for i in range(n):
    T2.append(T1[i])

print("Tableau T2 :", T2)



n = int(input("Donner la taille : "))

T1 = []
T2 = []
T = []

print("Remplir T1 :")
for i in range(n):
    T1.append(int(input()))

print("Remplir T2 :")
for i in range(n):
    T2.append(int(input()))

for i in range(n):
    T.append(T1[i] + T2[i])

print("Résultat T :", T)
