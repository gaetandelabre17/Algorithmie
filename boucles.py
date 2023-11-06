# while True :
#     number = int(input("Donnez moi un chiffre entre 0 et 10 : "))

#     if number > 0 and number < 10:
#         break

# print("TY!")

# numberBis = int(input("Donnez moi un chiffre : "))



# while numberBis != 0:
    
#     if numberBis < 0:
#         numberBis += 1
#     else:
#         numberBis -= 1
    
#     print(numberBis)



# guessNumber = 21

# while True:
#     userNumber = int(input("Devinez le nombre auquel je pense : "))

#     if userNumber < guessNumber:
#         print("C'est plus!")
#     elif userNumber > guessNumber:
#         print("C'est moins!")
#     else:
#         break

# print("GJ!")



for i in range(1, 21):
    print(f"{i} Francs = {i * 6.55957} €")
    i += 1