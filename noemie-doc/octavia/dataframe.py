import numpy as np
import pandas as pd
import random
A, B, C, D, V = int
"1" = int
"2" = int
"3" = int
ref = random.randrange(0,100,1)
#cree une fonction qui remplit dataframe avec 1,2,3 et ref avec 1 ou 2 ou 3 qui est == à ref et les autre aleatoirement,puis A,B,C,D qui vont choisir une barre aleatoirement parmi 1,2,3 qui n'est pas egale a ref
def auto() : #créer une fonction qui remplit un dataframe
    ash_keys = ["1","2","3",ref,A,B,C,D,V]
    df = pd.DataFrame(columns = ash_keys)
    


#barreRef = ref
asche_df = pd.DataFrame#({ "1":None  ,"2": None, "3": None, ref: random.randrange(0, 100, 1), A: None, B: None, C: None, D: None, V :None})