import numpy as np


class cardsDown():
    def __init__(self):
        self.cards = np.zeros((106,))
    def getCard(self, cardIndex):
        self.cards[cardIndex] = 0
