class Player:
    def __init__(self, name, hand, points=0):
        self.name = name
        self.hand = hand
        self.points = points
    def __str__(self):
        return self.name + " has " + str(self.points) + " points and hand: " + ', '.join(str(card) for card in self.hand)