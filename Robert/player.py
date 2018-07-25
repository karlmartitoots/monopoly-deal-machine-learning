import numpy as np
from deck import Deck
from hand import Hand
from board import Board



class Player():
    
    playerId = 0
    
    def __init__(self):
        self.hand = Hand()
        self.board = Board()
        self.id = Player.playerId
        Player.playerId += 1