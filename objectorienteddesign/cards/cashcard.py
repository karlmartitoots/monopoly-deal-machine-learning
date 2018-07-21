from .card import Card

class CashCard(Card):

    def __init__(self, title, value):
        super().__init__(", Cash Card, " + title)
        self.value = value
    
    def use(self, currentPlayer):
        currentPlayer.addToCash(self)