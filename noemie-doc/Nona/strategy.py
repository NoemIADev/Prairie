# strategies
import random

def rand(hand, carte):
    random.shuffle(hand)
    return hand.pop()


def plusGrande(hand, carte):
    hand.sort(key=lambda carte: carte.chiffre)
    return hand.pop(-1)

def plusPetite(hand, carte):
    hand.sort(key=lambda carte: carte.chiffre)
    return hand.pop()

def smart(hand, carte):
    if carte:
        hand.sort(key=lambda c: c.chiffre)
        for c in hand:
            if c.chiffre > carte.chiffre:
                hand.remove(c)
                return c
    return plusPetite(hand, carte)