import numpy as np


class Board():
    def __init__(self):
        self.board = -np.ones((153,))
    def getCard(self, boardIndex, cardIndex):
        self.board[boardIndex] = cardIndex
    def giveCard(self, boardIndex):
        self.board[boardIndex] = -1