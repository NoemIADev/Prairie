import pandas as pd
import numpy as np
import random

#créer une fonction qui remplit dataframe avec 1,2,3 et ref avec 1 ou 2 ou 3 qui est = à ref et les autre aleatoire mais tous different,puis A,B,C,D qui vont choisir une barre aleatoirement parmi 1,2,3 qui n'est pas egale a ref

def auto(n) :
      #100 lignes de barres qui sont toujours differentes
     valeurs_barres = [random.sample(range(0, 101), 3) for _ in range(100)]
     
     # creer un frame avec des colonnes 1,2,3 pour valeurr "valeurs_barres"
     df = pd.DataFrame(valeurs_barres,columns=["1","2","3"],)
    
     # ajouter une colonne ref qui prend une valeur aleatoire parmi 1,2,3
     df["ref"] = [random.choice(v) for v in valeurs_barres]
     
     # determine les choix de colonne des complices
     cols = ["1","2","3"]
     
     # on met dans finalChoices le choix final 
     finalChoices = []
    
     # pour chaque ligne dans df
     for l in range(len(df)):
        
         # on prend la valeur de ref pas ref directement
         ref_val = df.loc[l, "ref"]
            # on determine les choix possibles parmis les colonnes qui ne sont pas egale a ref
         choix_possibles = [c for c in cols if df.loc[l, c] != ref_val]
            # on ajoute un choix aleatoire parmi les choix possibles
         finalChoices.append(random.choice(choix_possibles))
    
     df["A"] = finalChoices
     df["B"] = finalChoices
     df["C"] = finalChoices
     df["D"] = finalChoices
     df["V"]= np.nan


     return df
print(auto(1))

if __name__ == "__main__":
    df = auto(1000)
    print(df)