from .card import Card

class PropertyCard(Card):

    def __init__(self, title, value, color, ):
        super().__init__(", Property Card, " + title)
        self.value = value
        self.color = color
    
    def use(self, currentPlayer):
        currentPlayer.addToProperty(self)
    
    def getRent(self, propertyAmount):
        