class Carte:
    def __init__(self, chiffre, forme):
        self.chiffre = chiffre
        self.forme= forme
    def __str__(self):
        return str(self.chiffre) + str(self.forme)