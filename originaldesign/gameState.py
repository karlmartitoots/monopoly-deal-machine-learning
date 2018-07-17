import numpy as np

class GameState:

    def __init__(self, nPlayers, hands, boards, usedCards, deck, choices):
        self.hands = hands
        self.boards = boards
        self.usedCards = usedCards
        self.deck = deck
        self.choices = choices

    def drawCard(self, playerIndex):
        
        cardIndex = np.random.choice(choices, p=deckWeights)