import numpy as np


class Deck():
    def __init__(self):
        self.cards = np.ones(106)
        self.weights = np.ones(106)/106
    def updateWeights(self):
        self.weights = self.cards/np.sum(self.cards)
    def getTwoCardIndexes(self):
        
    def giveTwo(self, cardIndexes):
        for i in range(2):
            self.cards[cardIndexes[i]] = 0
        Deck().updateWeights
    def giveFive(self, cardIndexes):
        for i in range(5):
            self.cards[cardIndexes[i]] = 0
        Deck().updateWeights
    