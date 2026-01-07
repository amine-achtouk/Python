# # Définition de la fonction Lire
# def Lire():
#     n = int(input("Entrez le nombre d'éléments de la liste : "))
#     liste = []
#     for i in range(n):
#         valeur = int(input(f"Entrez l'entier {i + 1} : "))
#         liste.append(valeur)
#     return liste

# # Lecture de la première liste
# liste1 = Lire()

# # Lecture de la deuxième liste
# liste2 = Lire()

# # Assemblage des deux listes dans une troisième
# liste3 = liste1 + liste2

# # Affichage des trois listes
# print("Première liste :", liste1)
# print("Deuxième liste :", liste2)
# print("Troisième liste (assemblée) :", liste3)

def Lire():
    n = int(input("Entrez le nombre d'éléments de la liste :"))

    list = []

    for i in range(n):
        v = int(input(f"Entrez l'entier {i+1} : "))
        list.append(v)
    return list

list1 = Lire()
list2 = Lire()

list3 = list1 + list2

print("Première liste :", list1)
print("Deuxième liste :", list2)
print("Troisième liste :", list3)


