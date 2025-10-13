"""
Jeu Pierre-Papier-Ciseaux interactif en Python.
Corrige automatiquement les fautes de frappe du joueur grâce à difflib.
Propose à l'utilisateur de rejouer ou de quitter.
"""

import random    # Module pour définir le choix de l'ordinateur
import difflib   # Module pour corriger le choix du joueur en cas d'erreur de frappe

options = ["Pierre", "Papier", "Ciseaux"]

while True: # Boucle principale du jeu

    # Boucle validation choix joueur
    while True:
        choix = input("\nPierre ? Papier ? Ciseaux ? Faites votre choix : \n").strip().title()
        # Cherche la correspondance la plus proche avec un seuil de tolérance
        proche = difflib.get_close_matches(choix, options, n=1, cutoff=0.6)
        if proche:
            choix = proche[0]
            break
        else:
            print("\nMerci de choisir entre Pierre, Papier & Ciseaux.\n")

    # Initialise la selection grâce à la fonction random
    selection_rand = random.choice(options)
    print(f"\nL'ordinateur à choisi {selection_rand}\n")

    # Détermination du résultat du jeu
    if choix in options:
        if choix == selection_rand:
            print(f"{choix} contre {selection_rand}, egalité !")
        elif (
            (choix == "Ciseaux" and selection_rand == "Papier") or \
            (choix =="Papier" and selection_rand == "Pierre") or \
            (choix == "Pierre" and selection_rand == "Ciseaux")
        ):
            print(f"\n{choix} contre {selection_rand}, Vous avez gagné !\n")
        else:
            print(f"{choix} contre {selection_rand}, vous avez perdu !\n")

    # Demande si l'utilisateur souhaite recommencer (validation obligatoire)
    while True:
        play_again = input("\nVoulez-vous recommencer ? (oui/non) : \n").strip().lower()
        if play_again in ["oui", "non"]:
            break
        else:
            print("\nMerci de répondre par oui ou non.\n")
    if play_again == "oui":
        pass
    else:
        print("\nMerci d'avoir participé.\n")
        break

            