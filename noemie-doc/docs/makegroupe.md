# Fonction pour crée des groupes aleatoirement

Cette fonction permet de créer des groupes à partir d’une liste d’éléments, en utilisant un paramètre k qui définit le nombre de personnes par groupe. Les informations sont stockées dans un fichier JSON.

Vous trouverez la fonction [ici](https://github.com/NoemIADev/Prairie/tree/master/noemie-doc/exo4)

## Détaillons ensemble son fonctionnement

Le but de cette fonction c'est de créer groupe juste en donnant la liste des personnes ou autres qui composeront le groupe et combien d'élément l'on souhaite par groupes.Le fichier json permet de ne pas avoir modifié le code en lui même.
*exemple*:
    {"eleves":["alex","bob","chloe","david","elie","franc","gwen","helene","igor","jean"],
    "k": 3 }
Ici si je veux des groupes de 2 ou 4 je n'ai qu'a changé la valeur de k et si je veux ajouter ou enlever des personnes je n'ai qu'a effacé leur nom ou en ajouter je peux même faire des groupes de fruits ça n'a pas d'importance.
*resultat quand on lance le code*:
    groupe final: [['bob', 'elie', 'helene'], ['chloe', 'franc', 'igor'], ['david', 'jean', 'gwen', 'alex']]
*le resultat est aleatoire,le groupe change à chaque fois*

## Comment sa marche ?

Regardons le code de plus près:
    with open("Variable.json") as Variable:
    data = json.load(Variable)
    eleves = data["eleves"]
    k = data["k"]

Cette partie du code permet de récupérer les éléments nécessaires, mentionnés précédemment.  
Grâce à cela, il n’est pas nécessaire de modifier le code par la suite, car les valeurs peuvent être réutilisées directement.

Ensuite, la fonction `groupe(eleves, k)` est définie.

Cette fonction prend deux paramètres :
- `eleves`, qui correspond à la liste des élèves,
- `k`, qui définit le nombre de personnes par groupe.

Ces paramètres sont définis en amont et transmis à la fonction afin qu’elle puisse les utiliser à l’intérieur de celle-ci pour créer les groupes.
Ensuite on melange la liste d'eleves qu'on à recupéré ` random.shuffle(eleves)` qu'on va l'utilisé pour crée la liste de groupe qui du coup sera faite à partir de la liste melanger et nom celle remplis dans Json.
     # cree des groupe de taille k a partir de la liste melanger
    
    listgroupe =[eleves[i:i+k]for i in range(0,len(eleves),k)]

Ici, on crée la liste `listegroupe`.  
On part de la liste `eleves`, qui est déjà mélangée, et on la parcourt par groupes de `k` éléments(ici 3).

À chaque étape, on prend les `k` élèves suivants afin de former un groupe.  
Ce mécanisme se répète jusqu’à ce que toute la liste des élèves ait été traitée.

## Probleme 

__A partir de la un probleme ce pose:__
Si je fait un print de ma liste de groupe qui est dans l'exemple de 10 personnes
    print("les groupes avant ajustement sont :",listgroupe)
Le resulat:
    print("les groupes avant ajustement sont :",listgroupe)
    
    les groupes avant ajustement sont : [['igor', 'chloe', 'alex'], ['jean', 'gwen', 'elie'], ['helene', 'franc', 'david'], ['bob']]

Bob est seul dans son groupe donc on a un groupe de 1 et on est d'accord si on veut faire des groupes c'est qu'on veut qu'il soit au moins 2 par tout seul.

## Solution
On doit ajouter une condition pour que le Bob soit integré un groupe pour pas qu'il se sente mis a part 😞.
Et quand on veut dire python attention si il se passe "ca" fait "cela" on crée une condition !

    # si la liste fait mini 3 groupe et que le dernier groupe a un seul eleve
    
    if len(listgroupe)>=3 and len(listgroupe[-1])== 1 :

        # ajoute le dernier eleve au groupe precedent
        listgroupe[-2].append(listgroupe[-1][0])

    # Supprime le dernier groupe vide 
        listgroupe.pop()
    return listgroupe 

*Resultat*:

```py 
print("groupe final:",groupe(eleves,3))
groupe final: [['igor', 'chloe', 'alex'], ['jean', 'gwen', 'elie'], ['helene', 'franc', 'david', 'bob']]
```

Et voila Bob a etait ajouter au groupe d'helene & co il est content.

![bobheureux](images/bob.gif)
