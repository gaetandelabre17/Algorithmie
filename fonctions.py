import random

# word = input("Donnez moi un mot : ")

# print(f"Votre mot contient {len(word)} lettres")


randomNumber = random.randint(0, 5)

while True:
    userNumber = int(input("Devinez le nombre auquel je pense : "))

    if userNumber < randomNumber:
        print("C'est plus!")
    elif userNumber > randomNumber:
        print("C'est moins!")
    else:
        break

print("GJ!")