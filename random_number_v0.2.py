import random


def jeu():
    # Boucle principale pour proposer de jouer ou non
    while True:
        # Demande à l'utilisateur s'il souhaite jouer (réponse oui/non)
        reponse = input("Voulez-vous jouer à un jeu aléatoire ? (oui/non) : ").strip().lower()
        
        # Si l'utilisateur refuse de jouer, quitte la boucle et termine le programme
        if reponse == "non":
            print("Pas de soucis, une prochaine fois peut-être.")
            break
        
        # Si l'utilisateur accepte de jouer
        elif reponse == "oui":
            # Boucle de jeu répétée tant que l'utilisateur veut rejouer
            while True:
                # Boucle de saisie pour obtenir un nombre entier valide
                while True:
                    saisie = input("Choisissez un nombre : ")
                    try:
                        nombre = int(saisie)  # Conversion en entier
                        break  # Sort de la boucle de saisie si conversion réussie
                    except ValueError:
                        print("Veuillez entrer uniquement des chiffres.")  # Erreur en cas de non chiffre
                
                # Génère un nombre aléatoire entre 1 et 10
                chiffre = random.randint(1, 10)
                
                # Vérifie si le nombre choisi correspond au nombre généré
                if chiffre == nombre:
                    print("Bravo, vous avez gagné !")
                    break  # Sort de la boucle de jeu
                    
                else:
                    # Propose de rejouer si l'utilisateur a perdu
                    rejouer = input("Oh mince ce n'est pas le bon numéro, voulez-vous retenter votre chance ? (oui/non) : ").strip().lower()
                    if rejouer == "non":
                        print("En espérant vous revoir bientôt !")
                        break  # Sort de la boucle de jeu
                
        else:
            # Cas où la réponse n'est ni "oui" ni "non"
            print("Merci de répondre par oui ou non.")


# Appel de la fonction principale pour démarrer le jeu
jeu()