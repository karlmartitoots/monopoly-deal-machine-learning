import numpy as np


class Deck():
    def __init__(self):
        self.cardAmount = 106
        self.cards = np.ones(self.cardAmount)
        self.weights = np.ones(self.cardAmount)/self.cardAmount

    def updateWeights(self):
        self.weights = self.cards/np.sum(self.cards)

    def getTwoCardIndices(self):
        return np.random.choice(self.cardAmount, size = 2, replace = False, p = self.weights)

    def getFiveCardIndices(self):
        return np.random.choice(self.cardAmount, size = 5, replace = False, p = self.weights)
        
    def giveTwo(self, cardIndices):
        self.cards[cardIndices] = 0
        Deck().updateWeights

    def giveFive(self, cardIndices):
        self.cards[cardIndices] = 0
        Deck().updateWeights
    