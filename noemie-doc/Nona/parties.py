#parties
import random
from Card import Carte
from Joueur import Player
from strategy import rand, plusGrande, plusPetite, smart 

# faire plussieurs parties et calculer le pourcentage de victoire du robot
def partie(strategy_humain, strategy_robot):
    # Créez une pioche de 10 cartes : 5 cartes "○" numérotées de 1 à 5 et 5 cartes "▢" numérotées de 0 à 4.
    pioche = []

    for chiffre in range(1, 6):
            pioche.append(Carte(chiffre, "○"))

    for chiffre in range(0, 5):
            pioche.append(Carte(chiffre, "▢"))

    random.shuffle(pioche)

        # Il y a 2 joueurs : le ROBOT et l’HUMAIN.
    humain = Player("HUMAIN", [], strategy=strategy_humain)
    robot = Player("ROBOT", [], strategy=strategy_robot)
        # Distribuez (au hasard) 5 cartes à chaque joueur.
    while len(pioche) > 0:
            humain.hand.append(pioche.pop(-1))
            robot.hand.append(pioche.pop(-1))
       
        # La partie se joue en 5 tours, Le ROBOT joue une carte puis L’HUMAIN joue une carte.
    points_robot = 0
    carte_de_humain = None
    for tour in range(5):
        carte_du_robot = robot.play(carte_de_humain)
        carte_de_humain = humain.play(carte_du_robot)
        if carte_du_robot.chiffre >= carte_de_humain.chiffre:
            points_robot += 1
    # victoire
    
    return robot if points_robot >= 3 else humain      
