# Importe le module "random"
import random

# Defini l'itération de 1 à 10
selection = random.randint(1, 10)

# Initialise le nombre d’essais et le maximum autorisé
essais = 0
max_essais = 5

# Boucle principale de jeu (nombre d’essais limité)
while essais < max_essais:

    # Demande la proposition de nombre à l'utilisateur
    number = int(input("Entrez un nombre de 1 à 10 : \n"))
    # Incrémente le compteur d'essais
    essais += 1
    # Vérifie si la proposition est correcte
    if number == selection :
        print("Bravo, vous avez trouvé le nombre.")
        # Sors de la boucle
        break
    # Si la proposition est trop petite
    elif number < selection:
        print(f"Le nombre est supérieur à {number}.")
    else:
    # Si la proposition est trop grande
        print(f"le nombre est inferieur à {number}.")

# Si le nombre maximal d'essais est atteint sans réussite
if essais == max_essais and number != selection:
    print(f"C'est perdu, le numéro exacte était {selection}")
