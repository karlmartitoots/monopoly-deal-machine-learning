import numpy as np
from gameState import *

class Game:
    
    def __init__(self, nPlayers):
        self.nPlayers = nPlayers
        self.gameState = GameState(np.zeros((110,nPlayers)),
                                   self.createBoards(),
                                   np.zeros((110,)),
                                   np.ones((110,)))
    
    def createBoards(self):
        board = [np.zeros((7,)),       #0. browns
                 np.zeros((7,)),       #1. dark blues
                 np.zeros((9,)),       #2. greens
                 np.zeros((9,)),       #3. light blues
                 np.zeros((9,)),       #4. oranges
                 np.zeros((9,)),       #5. purple
                 np.zeros((11,)),      #6. rail roads
                 np.zeros((9,)),       #7. reds
                 np.zeros((7,)),       #8. utilites
                 np.zeros((9,)),       #9. yellows
                 np.zeros((67,))]      #10. money
        boards = []
        for i in range(self.nPlayers):
            boards.append(board)
        return boards
        
