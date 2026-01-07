import json


def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

produits_file = "produits.json"
commandes_file = "commande.json"
clients_file = "client.json"

produits = load_data(produits_file)
commandes = load_data(commandes_file)
clients = load_data(clients_file)



def ajouter_produit():
    id = int(input("ID produit: "))
    description = input("Description: ")
    quantite = int(input("Quantité: "))
    prix = float(input("Prix: "))
    produits.append({"id": id, "description": description, "quantité": quantite, "prix": prix})
    save_data(produits_file, produits)

def modifier_produit():
    id = int(input("ID produit à modifier: "))
    for p in produits:
        if p["id"] == id:
            p["description"] = input(f"Nouvelle description ({p['description']}): ") or p["description"]
            p["quantité"] = int(input(f"Nouvelle quantité ({p['quantité']}): ") or p["quantité"])
            p["prix"] = float(input(f"Nouveau prix ({p['prix']}): ") or p["prix"])
            save_data(produits_file, produits)
            print("Produit modifié.")
            return
    print("Produit non trouvé.")

def supprimer_produit():
    id = int(input("ID produit à supprimer: "))
    global produits
    produits = [p for p in produits if p["id"] != id]
    save_data(produits_file, produits)
    print("Produit supprimé.")



def ajouter_commande():
    id = int(input("ID commande: "))
    produits_ids = input("IDs produits (séparés par des virgules): ").split(",")
    produits_ids = [int(pid.strip()) for pid in produits_ids]
    total = sum([p["prix"] for p in produits if p["id"] in produits_ids])
    commandes.append({"id": id, "produits": produits_ids, "total": total})
    save_data(commandes_file, commandes)

def modifier_commande():
    id = int(input("ID commande à modifier: "))
    for c in commandes:
        if c["id"] == id:
            produits_ids = input(f"Nouveaux IDs produits (actuels {c['produits']}): ").split(",")
            produits_ids = [int(pid.strip()) for pid in produits_ids if pid.strip()]
            if produits_ids:
                c["produits"] = produits_ids
                c["total"] = sum([p["prix"] for p in produits if p["id"] in produits_ids])
            save_data(commandes_file, commandes)
            print("Commande modifiée.")
            return
    print("Commande non trouvée.")

def supprimer_commande():
    id = int(input("ID commande à supprimer: "))
    global commandes
    commandes = [c for c in commandes if c["id"] != id]
    save_data(commandes_file, commandes)
    print("Commande supprimée.")


def ajouter_client():
    id = int(input("ID client: "))
    nom = input("Nom du client: ")
    commande_id = int(input("ID de la commande: "))
    clients.append({"id": id, "nom": nom, "commande_id": commande_id})
    save_data(clients_file, clients)

def modifier_client():
    id = int(input("ID client à modifier: "))
    for c in clients:
        if c["id"] == id:
            c["nom"] = input(f"Nouveau nom ({c['nom']}): ") or c["nom"]
            commande_id = input(f"Nouveau ID commande ({c['commande_id']}): ")
            if commande_id:
                c["commande_id"] = int(commande_id)
            save_data(clients_file, clients)
            print("Client modifié.")
            return
    print("Client non trouvé.")

def supprimer_client():
    id = int(input("ID client à supprimer: "))
    global clients
    clients = [c for c in clients if c["id"] != id]
    save_data(clients_file, clients)
    print("Client supprimé.")


def menu():
    while True:
        print("""
1- Ajouter produit
2- Modifier produit
3- Supprimer produit
4- Ajouter commande
5- Modifier commande
6- Supprimer commande
7- Ajouter client
8- Modifier client
9- Supprimer client
0- Quitter
""")
        choix = input("Choisissez une option: ")
        if choix == "1":
            ajouter_produit()
        elif choix == "2":
            modifier_produit()
        elif choix == "3":
            supprimer_produit()
        elif choix == "4":
            ajouter_commande()
        elif choix == "5":
            modifier_commande()
        elif choix == "6":
            supprimer_commande()
        elif choix == "7":
            ajouter_client()
        elif choix == "8":
            modifier_client()
        elif choix == "9":
            supprimer_client()
        elif choix == "0":
            print("Au revoir!")
            break
        else:
            print("Option invalide!")


menu()
