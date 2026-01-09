# l'expérience de Asch
Dans cet exercice on doit entrainer un model à partir d'un tableau qui simule l'expérience d'Asch (*Le paradigme d'Asch est une étude fondamentale pour comprendre la pression des pairs au sein d'un groupe . Les expériences d'Asch ont démontré comment les individus sont influencés par l'opinion majoritaire d'un groupe, même lorsque celle-ci est en contradiction avec leur propre jugement.*) le model entrainé doit représenter la personne piégée qui doit choisir la barre de la même taille que la référence.

pour cela on crée un tableau de donné qui va contenir la V la victime et A B C D les complices qui vont répondre faux et les barres 1 2 3 et REF.

## Creation du dataframe

[Lien vers le code complet](https://github.com/NoemIADev/Prairie/blob/master/noemie-doc/octavia/dataframe.py)

```python
#créer une fonction qui remplit dataframe avec 1,2,3 et ref avec 1 ou 2 ou 3 qui est = à ref et les autre aleatoire mais tous different,puis A,B,C,D qui vont choisir une barre aleatoirement parmi 1,2,3 qui n'est pas egale a ref

def auto(n) :
```

crée 100 lignes de barres qui sont toujours differentes:

```python
valeurs_barres = [random.sample(range(0, 101), 3) for _ in range(100)]
```
ici c'est le "sample" qui permet qu'il n'y ai pas de doublon

ensuite on crée  un le tableau avec des colonnes 1,2,3 pour valeurr "valeurs_barres"

     df = pd.DataFrame(valeurs_barres,columns=["1","2","3"],)

puis ajouter une colonne ref qui prend une valeur aleatoire parmi 1,2,3:

    df["ref"] = [random.choice(v) for v in valeurs_barres]

On determine les choix de colonnes des complices
    cols = ["1","2","3"]

on met dans finalChoices le choix final 
    finalChoices = []

Ensuite on va determiner les choix des complices en fonction des barres 

```py

 # pour chaque ligne dans df
     for l in range(len(df)):
        
         # on prend la valeur de ref pas ref directement
         ref_val = df.loc[l, "ref"]
            # on determine les choix possibles parmis les colonnes qui ne sont pas egale a ref
         choix_possibles = [c for c in cols if df.loc[l, c] != ref_val]
            # on ajoute un choix aleatoire parmi les choix possibles
         finalChoices.append(random.choice(choix_possibles)) 
```
et on attribu un choix final a chaque complice
    df["A"] = finalChoices
     df["B"] = finalChoices
     df["C"] = finalChoices
     df["D"] = finalChoices
     df["V"]= np.nan
et on garde V vide qui sera remplis par notre focntion solve puis le model.

