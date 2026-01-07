voitures = []

for i in range(3):
    voiture = {
        "matricule": input("Matricule: "),
        "marque": input("marque: "),
        "modele": input("Modele: "),
        "prix": float(input("Prix: "))
    }
    voitures.append(voiture)

plus_chère = voitures[0]

for voiture in voitures:
    if voiture["prix"] > plus_chère["prix"]:
        plus_chère = voiture

print("la plus chère :", plus_chère)        