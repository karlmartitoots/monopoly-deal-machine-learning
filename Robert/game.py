import numpy as np
from deck import Deck
from hand import Hand
from board import Board
from cardsDown import CardsDown
from player import Player



class Game():
    
    def __init__(self):
        self.noOfPlayers = 2
        self.players = [Player(),Player()]
        self.hands = [self.players[0].hand,self.players[1].hand]
        self.boards = [self.players[0].board,self.players[1].board]
        self.deck = Deck()
        self.cardsDown = CardsDown()
    
    def givePlayerTwoCards(self, player):
        indices = self.deck.giveTwo(self.deck.getTwoCardIndices())
        self.hands[player].getTwoCards(indices)

    def givePlayerFiveCards(self, player):
        indices = self.deck.giveFive(self.deck.getFiveCardIndices())
        self.hands[player].getFiveCards(indices)