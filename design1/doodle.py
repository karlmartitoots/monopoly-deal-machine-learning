import numpy as np
from cards import ActionCard
from cards import CashCard

ac = ActionCard("Deal Breaker", 5)
print(ac)

class thing:

    def __init__(self,noPlayers):
        self.noPlayers = noPlayers
        self.all_action_cards = {
            0: self.deal_breaker,
            1: self.deal_breaker
        }
    
    def deal_breaker(self):
        pass
 