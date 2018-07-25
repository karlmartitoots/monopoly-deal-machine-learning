import numpy as np


class Hand():
    def __init__(self):
        self.cards = np.zeros((106,))
        self.cardIndexList = np.array([])
        
    def updateCardIndexList(self):
        self.cardIndexList = np.where(self.cards)

    def getTwoCards(self, cardIndices):
        self.cards[cardIndices] = 1
        Hand().updateCardIndexList()

    def getFiveCards(self, cardIndices):
        self.cards[cardIndices] = 1
        Hand().updateCardIndexList()

    def giveCard(self, cardIndex):
        self.cards[cardIndex] = 0
        Hand().updateCardIndexList
