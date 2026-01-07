stagiaires  = []

for i in range(3):  # use 20 in real case
    notes = []
    for j in range(3):
        notes.append(float(input("Note: ")))

    stagiaire = {
        "name": input("Name: "),
        "firstname": input("Firstname: "),
        "notes": notes
    }

    stagiaire["average"] = sum(notes) / len(notes)
    stagiaires .append(stagiaire)

stagiaires .sort(key=lambda x: x["average"], reverse=True)

rank = 1
for s in stagiaires :
    s["rank"] = rank
    rank += 1


for s in stagiaires :
    print(s)
