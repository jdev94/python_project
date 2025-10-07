# Poids en KG et taille en M

# Création de la boucle
while True:

   #Demande à l'utilisateur son poids et sa taille
    poids = float(input("Insérez votre poids : \n"))
    taille = float(input("Insérez votre taille : \n"))

    # Vérifie que le poids et la taille sont supérieurs à zéro
    if poids <= 0 or taille <= 0:
        print("Poids et taille doivent être supérieurs à zéro. Veuillez recommencer.")
        continue

    # Calcul de l'IMC si saisie valide
    imc= poids/(taille**2)
    print(f"L'IMC d'une personne de {poids} Kg & {taille}m est de : {imc} Kg/m^2.")

    # Sort de la boucle
    break