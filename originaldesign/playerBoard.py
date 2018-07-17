class PlayerBoard:
    'Holds a players cards on board information and its modification methods'

    def __init__():
        self.board = [np.zeros((7,)),       #0. browns
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