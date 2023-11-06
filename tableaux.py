# chiffres = [10, 15, 20, 15, 14, 8]
# somme = 0

# for i in chiffres:
#     somme = somme + i

# print(somme)



numberStudents = int(input("Combien y'a t'il d'élèves : "))
topMoyenne = []

for i in range(numberStudents):
    gradeStudents = int(input(f"Donnez moi la note de l'élève {i + 1} : "))
    if gradeStudents > 13 and gradeStudents <= 20:
        topMoyenne.append(gradeStudents)

print(f"Il y a {len(topMoyenne)} élève(s) au dessus de la moyenne")