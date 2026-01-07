professeur1 = {
    "numéro_somme" : 2, 
    "nom" : "Bouho", 
    "prénom" : "abelmajid",
    "diplôme" : "Techencien Specialise", 
    "année_recrutement" : 2024,
    "spécialité" : "Python"
}
professeur2 = {
    "numéro_somme" : 3, 
    "nom" : "ait ofkir", 
    "prénom" : "merise",
    "diplôme" : "Techencien Specialise", 
    "année_recrutement" : 2025,
    "spécialité" : "Data Base"
}

S1 = {
    "numéro": 154,
    "nom": "janah",
    "prénom": "yassine",
    "professeur_enseigne": professeur1

}

S2 = {
    "numéro": 101,
    "nom": "Messi",
    "prénom": "Lionel",
    "professeur_enseigne": professeur2
}

if S1["professeur_enseigne"]["numéro_somme"] == S2["professeur_enseigne"]["numéro_somme"]:
    print("Same professor")
else:
    print("Different professors")

print('------------------------------------')

if S1["professeur_enseigne"]["année_recrutement"] < S2["professeur_enseigne"]["année_recrutement"]:
    print("le stagiaire qui a le professeur le plus ancien est :", S1["nom"])
else:
    print("le stagiaire qui a le professeur le plus ancien est :", S2["nom"])