#from strategy import rand, plusGrande, plusPetite, smart
from Card import Carte

class Player:
    def __init__(self, name, hand, points=0, strategy=None):
        self.name = name
        self.hand = hand
        self.points = points
        self.strategy = strategy
    def __str__(self):
        return self.name + " has " + str(self.points) + " points and hand: " + ', '.join(str(card) for card in self.hand)
    def play(self, carte=None):
        return self.strategy(self.hand, carte)
    
    def play(self, carte=None):
        return self.strategy(self.hand, carte)