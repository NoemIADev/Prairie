# Card Game

> Simulation d’un jeu de cartes entre un ROBOT et un HUMAIN, avec comparaison de stratégies.

[Lien vers le depot](https://github.com/NoemIADev/Prairie/tree/master/noemie-doc/Nona)

---

## Énoncé de l’exercice

Le but de cet exercice est de simuler un jeu de cartes très simple entre deux joueurs :
- un **ROBOT**
- un **HUMAIN**

Puis :
- simuler un grand nombre de parties
- calculer le **pourcentage de victoire du robot**
- tester différentes **stratégies de jeu** pour comparer leurs performances

---

## Règles du jeu

### Matériel
- 10 cartes au total :
  - 5 cartes **rond** numérotées de 0 à 4
  - 5 cartes **carré** numérotées de 1 à 5

### Joueurs
- 2 joueurs : **ROBOT** et **HUMAIN**

### Déroulement
- Chaque joueur reçoit 5 cartes au hasard
- La partie se joue en **5 tours**
- À chaque tour :
  1. Le robot joue une carte
  2. L’humain joue une carte
- Le joueur qui a la carte avec la **plus grande valeur** gagne le pli
- En cas d’égalité, **le robot gagne**
- Le joueur qui gagne **au moins 3 plis** remporte la partie

---

## Structure du projet

Le projet est découpé en plusieurs fichiers pour séparer les responsabilités :

- `Card.py` → représentation d’une carte
- `Joueur.py` → gestion d’un joueur
- `strategy.py` → stratégies de jeu
- `parties.py` → logique d’une partie complète
- `main.py` → simulation de plusieurs parties et statistiques

---

## Classe Carte

Chaque carte est définie par :
- un **chiffre**
- une **forme**

```python
class Carte:
    def __init__(self, chiffre, forme):
        self.chiffre = chiffre
        self.forme = forme

    def __str__(self):
        return str(self.chiffre) + str(self.forme)
```
    ---

## Classe Joueur (`Joueur.py`)

La classe `Player` représente un joueur du jeu.
Un joueur possède :
- un **nom** (`name`)
- une **main de cartes** (`hand`)
- un **nombre de points** (`points`)
- une **stratégie** qui détermine quelle carte jouer

---

### Initialisation du joueur

```python
from Card import Carte

class Player:
    def __init__(self, name, hand, points=0, strategy=None):
        self.name = name
        self.hand = hand
        self.points = points
        self.strategy = strategy
```
---

## Stratégies de jeu (`strategy.py`)

Une **stratégie** est une fonction qui choisit quelle carte jouer.
Elle reçoit :
- `hand` → la main du joueur (liste de cartes)
- `carte` → la carte jouée par l’adversaire (ou `None` si on ne sait pas)

Elle doit **retourner une Carte** (et l’enlever de la main).

---

### Stratégie aléatoire

```python
import random

def rand(hand, carte):
    random.shuffle(hand)
    return hand.pop()
```
Elle dit au joueur de toujours jouer une carte au pif.

---

### Strategie de la plus Grande

    def plusGrande(hand, carte):
    hand.sort(key=lambda carte: carte.chiffre)
    return hand.pop(-1)

On range la liste de carte dans l'ordre croissant puis on joue la derniere (donc la plus grande).

---

### Stratégie de la plus petite 

    def plusPetite(hand, carte):
    hand.sort(key=lambda carte: carte.chiffre)
    return hand.pop()

Pareil au précédent sauf qu'on joue la 1er carte (donc la plus petite).

---

### Stratégie smart

    def smart(hand, carte):
    if carte:
        hand.sort(key=lambda c: c.chiffre)
        for c in hand:
            if c.chiffre > carte.chiffre:
                hand.remove(c)
                return c
    return plusPetite(hand, carte)

Cette fois le joueur va réfléchir un peu plus on va lui faire comparer la carte jouée par l'adversaire pour qu'il joue la plus grande s'il n'a pas la plus grande il joue la plus petite pour ne pas perdre de grosses cartes.

## Déroulement de la partie (`parties.py`)

Le fichier `parties.py` contient la fonction `partie()` qui simule une partie complète
entre un ROBOT et un HUMAIN.

Cette fonction permet de :
- créer la pioche
- mélanger et distribuer les cartes
- jouer 5 tours
- compter les points
- déterminer le gagnant

---

### Définition de la fonction

```python
def partie(strategy_humain, strategy_robot):
```
La fonction prend en paramètre :

- strategy_humain : stratégie utilisée par l’humain

- strategy_robot : stratégie utilisée par le robot

Cela permet de tester différentes combinaisons de stratégies.

### Création de la pioche

On commence par créer une liste pioche contenant les 10 cartes du jeu.

    pioche = []

    for chiffre in range(1, 6):
            pioche.append(Carte(chiffre, "○"))

    for chiffre in range(0, 5):
            pioche.append(Carte(chiffre, "▢"))

puis on la melange `` random.shuffle(pioche)``

### Création des joueurs

     # Il y a 2 joueurs : le ROBOT et l’HUMAIN.
    
    humain = Player("HUMAIN", [], strategy=strategy_humain)
    robot = Player("ROBOT", [], strategy=strategy_robot)

Chaque joueur possède un nom, une main vide au départ
et une stratégie définie lors de l’appel de la fonction.

### Distribution des cartes

Les cartes sont distribuées alternativement jusqu’à ce que la pioche soit vide.
     while len(pioche) > 0:
            humain.hand.append(pioche.pop(-1))
            robot.hand.append(pioche.pop(-1))
       
À la fin de la distribution :

- l’humain possède 5 cartes

- le robot possède 5 cartes

### Déroulement des tours

La partie se joue en 5 tours.

     for tour in range(5):
        carte_du_robot = robot.play(carte_de_humain)
        carte_de_humain = humain.play(carte_du_robot)

À chaque tour :
- le robot joue une carte
- l’humain joue une carte en réponse
les stratégies déterminent automatiquement les cartes jouées.

À la fin des de chaque plis, le gagnant est déterminé ainsi :
    if carte_du_robot.chiffre >= carte_de_humain.chiffre:
            points_robot += 1

Si le robot gagne le pli, son nombre de points augmente de 1.

À la fin des 5 tours, le gagnant est déterminé ainsi :

``return robot if points_robot >= 3 else humain  ``

Le robot gagne s’il remporte au moins 3 plis,
sinon c’est l’humain qui gagne la partie.

---

## Simulation de plusieurs parties (`main.py`)

Le fichier `main.py` permet de lancer un grand nombre de parties
afin de calculer le **pourcentage de victoire du robot**
en fonction des stratégies utilisées.

```py 
n_parties = 1000
victoires_robot = 0
```
- n_parties : nombre total de parties simulées

- victoires_robot : compteur du nombre de victoires du robot

On lance n_parties simulations consécutives.

    for i in range(n_parties):
    gagnant = partie(
        strategy_humain=smart,
        strategy_robot=smart
    )

- une nouvelle partie est simulée

- les stratégies de l’humain et du robot sont définies ici

- la fonction partie() retourne le gagnant

puis on determine le gagnant 

```py
 if gagnant.name == "ROBOT":
        victoires_robot += 1 
```
puis on affiche le pourcentage de victoire du robot
```py
print("% victoire robot: ", (victoires_robot / n_parties)*100)
```

