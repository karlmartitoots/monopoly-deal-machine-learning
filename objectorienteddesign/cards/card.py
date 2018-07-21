

class Card:
    'Abstract class for holding card information'

    def __init__(self,title):
        self.title = "Card" + title

    def use(self, currentPlayer):
        raise NotImplementedError

    def __str__(self):
        return self.title