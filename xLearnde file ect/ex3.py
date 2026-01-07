
def  saisir():
    file = open("concours.txt", "w")
    ncin = input("NCIN : ")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    age = int(input("Age : "))
    decision = input("Décision (admis/refusé/ajourné) : ")
    file.write(f"{ncin} - {nom} - {prenom} - {age} - {decision}\n")
    file.close()



def admis():
    file1 = open("concours.txt", "r")
    file2 = open("admis.txt", "w")

    for ligne in file1:
        data = ligne.strip().split(";")
        if data[4] == "admis":
            file2.write(ligne)
    
    file1.close()
    file2.close()


saisir()    
admis()