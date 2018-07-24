import numpy as np


class Hand():
    def __init__(self):
        self.cards = np.zeros((106,))
        self.cardIndexList = np.array([])
    def updateCardIndexList(self):
        cardIndexList = []
        for i in range(106):
            if self.cards[i] == 1:
                cardIndexList.append(i)
        self.cardIndexList = np.array(cardIndexList)
    def getTwoCards(self, cardIndexes):
        for i in range(2):
            self.cards[cardIndexes[i]] = 1
        Hand().updateCardIndexList()
    def getFiveCards(self, cardIndexes):
        for i in range(5):
            self.cards[cardIndexes[i]] = 1
        Hand().updateCardIndexList()
    def giveCard(self, cardIndex):
        self.cards[cardIndex] = 0
        Hand().updateCardIndexList
