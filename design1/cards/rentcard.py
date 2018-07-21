from .card import Card

class RentCard(Card):

    def __init__(self, title, value, color):
        super().__init__(", Rent Card, " + title)
        self.value = value
        self.color = color
        self.isCash = False
    
    def use(self, currentPlayer):
        if self.isCash:
            currentPlayer.addToCash(self)
        else:
            currentPlayer.askRent(color)
    
    def makeIntoCash(self):
        self.isCash = True