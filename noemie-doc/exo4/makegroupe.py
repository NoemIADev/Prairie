import json
import random


# Ouvre et lit le fichier json pour recuperer la liste des eleves et la taille des groupes
with open("Variable.json") as Variable:
    data = json.load(Variable)
    eleves = data["eleves"]
    k = data["k"]

# Fonction qui cree des groupes d'eleves de taille k
def groupe(eleves,k) :
    
    # melange la liste d'eleves
    random.shuffle(eleves)
    print("la liste des eleves melangee est :",eleves)
    
    # cree des groupe de taille k a partir de la liste melanger
    
    listgroupe =[eleves[i:i+k]for i in range(0,len(eleves),k)]

    print("les groupes avant ajustement sont :",listgroupe)
    
    # si la liste fait mini 3 groupe et que le dernier groupe a un seul eleve
    
    if len(listgroupe)>=3 and len(listgroupe[-1])== 1 :

        # ajoute le dernier eleve au groupe precedent
        listgroupe[-2].append(listgroupe[-1][0])

    # Supprime le dernier groupe vide 
        listgroupe.pop()
    return listgroupe 
print("groupe final:",groupe(eleves,3))
