# main.py
from parties import partie
from strategy import rand, plusGrande, plusPetite, smart


n_parties = 1000
victoires_robot = 0
for i in range(n_parties):
    gagnant = partie(
        strategy_humain=smart,
        strategy_robot=smart)
    
    if gagnant.name == "ROBOT":
        victoires_robot += 1
        

print("% victoire robot: ", (victoires_robot / n_parties)*100)
#print(victoires_robot)
