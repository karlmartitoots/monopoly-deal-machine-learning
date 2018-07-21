import numpy as np

nPlayers = 4
board = [np.zeros((7,)),       #0. browns
                 np.zeros((7,)),       #1. dark blues
                 np.zeros((9,)),       #2. greens
                 np.zeros((9,)),       #3. light blues
                 np.zeros((9,)),       #4. oranges
                 np.zeros((9,)),       #5. purple
                 np.zeros((11,)),      #6. rail roads
                 np.zeros((9,)),       #7. reds
                 np.zeros((7,)),       #8. utilites
                 np.zeros((9,)),       #9. yellows
                 np.zeros((67,))]      #10. money
boards = []
for i in range(nPlayers):
    boards.append(board)
# give cards to players
hands = np.zeros((nPlayers,110))

def action1():
    print("Action 1")

def action2():
    print("Action 2")

d = {
    0: action1,
    1: action2
}
for i in range(53,63):
    print(np.random.randint(2))




class thing:

    def __init__(self,noPlayers):
        self.noPlayers = noPlayers
        self.all_action_cards = {
            0: self.deal_breaker,
            1: self.deal_breaker
        }
    
    def deal_breaker(self):
        pass
