# numbers = input("Donnez moi deux chiffres (séparés d'un espace) : ")

# a, b = numbers.split()
# result = int(a) * int(b)

# if result >= 0:
#     print("Le produit de ces deux nombres est positif")
# else:
#     print("Le produit de ces deux nombres est négatif")




age = int(input("Quel âge as-tu : "))

if age < 13:
    print("Tu peux aller voir le film Action Man")
elif age > 13 and age < 18:
    print("Tu peux aller voir Matrix")
else:
    print("Tu peux aller voir Evil Dead")