
class Deck:

    class __Deck:
        def __init__(self, arg):
            self.val = arg
            self.cards = {}
    instance = None
    def __init__(self, arg):
        if not Deck.instance:
            Deck.instance = Deck.__Deck(arg)
        else:
            Deck.instance.val = arg