import numpy as np


class CardsDown():
    def __init__(self):
        self.cards = np.zeros((106,))

    def getCard(self, cardIndex):
        self.cards[cardIndex] = 1

    def giveAll(self):
        a = np.where(self.cards[0])
        self.cards[a] = 0
        return a