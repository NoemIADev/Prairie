import json
import random
print ("VERSION DU FICHIER: 2.0")
with open("Variable.json") as Variable:
    data = json.load(Variable)
    eleves = data["eleves"]
    k = data["k"]

def groupe(eleves,k) :
    # melange la liste d'eleves
    random.shuffle(eleves)
    print("la liste des eleves melangee est :",eleves)
    # cree des groupe de taille k a partir de la liste melanger
    listgroupe =[eleves[i:i+k]for i in range(0,len(eleves),k)]
    # si la liste fait mini 3 groupe et que le dernier groupe a un seul eleve
    if len(listgroupe)>=3 and len(listgroupe[-1])== 1 :
        print("condition vrai")
        # ajoute le dernier eleve au groupe precedent
        listgroupe[-2].append(listgroupe[-1][0])
    # Supprime le dernier groupe vide 
        listgroupe.pop()
    return listgroupe 
    print("fin de la fonction groupe")
print("groupe apres excution de la fonction",groupe(eleves,3))
