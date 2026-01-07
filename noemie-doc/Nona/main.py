#main
import random
from Card import Carte
from Joueur import Player
# faire plussieurs parties et calculer le pourcentage de victoire du robot
def partie(nb):
    # Créez une pioche de 10 cartes : 5 cartes "○" numérotées de 1 à 5 et 5 cartes "▢" numérotées de 0 à 4.
    pioche = []

    for chiffre in range(1, 6):
            pioche.append(Carte(chiffre, "○"))

        for chiffre in range(0, 5):
            pioche.append(Carte(chiffre, "▢"))

        random.shuffle(pioche)

        # Il y a 2 joueurs : le ROBOT et l’HUMAIN.
        humain = Player("HUMAIN", [])
        robot = Player("ROBOT", [])

        # Distribuez (au hasard) 5 cartes à chaque joueur.
        while len(pioche) > 0:
            humain.hand.append(pioche.pop(-1))
            robot.hand.append(pioche.pop(-1))
        print(humain)
        print(robot)
        # La partie se joue en 5 tours, Le ROBOT joue une carte puis L’HUMAIN joue une carte.
        for tour in range(5):
            #print("\n--- Tour", tour + 1, "---")
            carte_robot = robot.hand.pop(0)
            #print("ROBOT joue:", carte_robot)
            carte_humain = humain.hand.pop(0)
            #print("HUMAIN joue:", carte_humain)
            if carte_robot.chiffre >= carte_humain.chiffre:
                robot.points += 1
                #print("ROBOT remporte le pli.")
            else:
                humain.points += 1
                #print("HUMAIN remporte le pli.")
            if robot.points > humain.points:
                print("\nROBOT gagne la partie avec", robot.points, "points!")
            else:
                print("\nHUMAIN gagne la partie avec", humain.points, "points!")
        robotwin_percent = (robot.points / nb) * 100
    return robotwin_percent
    print(partie(50))