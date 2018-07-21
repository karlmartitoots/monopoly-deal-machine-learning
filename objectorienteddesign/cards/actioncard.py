from .card import Card

class ActionCard(Card):

    def __init__(self, title, value):
        super().__init__(", Action Card, " + title)
        self.value = value
    
    def use(self, currentPlayer):
        self.runAction(currentPlayer)

    def runAction(self, currentPlayer):
        raise NotImplementedError