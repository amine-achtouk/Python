


def saisir():
    f = open("concours.txt", "w")
    n = int(input("Nombre de candidats : "))

    for i in range(n):
        print(f"\nCandidat {i+1}")
        ncin = input("NCIN : ")
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        age = int(input("Age : "))
        decision = input("Décision (admis/refusé/ajourné) : ")

        f.write(f"{ncin};{nom};{prenom};{age};{decision}\n")

    f.close()


def admis():
    f1 = open("concours.txt", "r")
    f2 = open("admis.txt", "w")

    for ligne in f1:
        data = ligne.strip().split(";")
        if data[4] == "admis":
            f2.write(ligne)

    f1.close()
    f2.close()


def attente():
    f1 = open("admis.txt", "r")
    f2 = open("attente.txt", "w")

    for ligne in f1:
        data = ligne.strip().split(";")
        age = int(data[3])

        if age > 30:
            f2.write(f"{data[0]};{data[1]} {data[2]}\n")

    f1.close()
    f2.close()


def statistiques(dec):
    f = open("concours.txt", "r")
    total = 0
    nb = 0

    for ligne in f:
        total += 1
        if ligne.strip().split(";")[4] == dec:
            nb += 1

    f.close()

    if total == 0:
        return 0
    return (nb / total) * 100


def supprimer():
    f = open("admis.txt", "r")
    lignes = []

    for ligne in f:
        age = int(ligne.strip().split(";")[3])
        if age <= 30:
            lignes.append(ligne)

    f.close()

    f = open("admis.txt", "w")
    f.writelines(lignes)
    f.close()



saisir()
admis()
attente()
print("Pourcentage admis :", statistiques("admis"))
supprimer()
