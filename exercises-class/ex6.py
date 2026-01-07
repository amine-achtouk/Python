def Somme(a, b):
    return a + b

n1 = int(input("Entrez le premier entier : "))
n2 = int(input("Entrez le deuxième entier : "))
resultat_entiers = Somme(n1, n2)
print("La somme des deux entiers est :", resultat_entiers)


r1 = float(input("Entrez le premier nombre réel : "))
r2 = float(input("Entrez le deuxième nombre réel : "))
resultat_reels = Somme(r1, r2)
print("La somme des deux nombres réels est :", resultat_reels)