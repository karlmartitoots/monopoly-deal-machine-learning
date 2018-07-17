class Hand:
    'Holds a players cards in hand information and its modification methods'

    def __init__(self):
        self.cards = np.zeros((110,))
    
    def useCard(self):
        