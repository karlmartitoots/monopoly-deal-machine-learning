import numpy as np

class Game:

    def __init__(self, no_of_players):
        # make deck
        self.deck = np.ones((110,))
        # make boards
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
        self.boards = []
        for i in range(self.no_of_players):
            self.boards.append(board)
        # give cards to players
        self.hands = np.zeros((nPlayers,110))
        # action card options
        self.all_action_cards = {
            0: deal_breaker,
            1: deal_breaker,
            2: debt_collector,
            3: debt_collector,
            4: debt_collector,
            5: double_rent,
            6: double_rent,
            7: forced_deal,
            8: forced_deal,
            9: forced_deal,
            10: hotel,
            11: hotel,
            12: hotel,
            13: house,
            14: house,
            15: house,
            16: say_no,
            17: say_no,
            18: say_no,
            19: birthday,
            20: birthday,
            21: birthday,
            22: pass_go,
            23: pass_go,
            24: pass_go,
            25: pass_go,
            26: pass_go,
            27: pass_go,
            28: pass_go,
            29: pass_go,
            30: pass_go,
            31: pass_go,
            32: sly_deal,
            33: sly_deal,
            34: sly_deal
        }
        # self.all_property_cards = {
        #     35: brown(0),
        #     36: brown(1), 
        #     37: blue(0), 
        #     38: blue(1), 
        #     39: green(0), 
        #     40: green(1), 
        #     41: green(2), 
        #     42: lightblue(0), 
        #     43: lightblue(1), 
        #     44: lightblue(2), 
        #     45: orange(0), 
        #     46: orange(1), 
        #     47: orange(2), 
        #     48: purple(0), 
        #     49: purple(1),
        #     50: purple(2), 
        #     51: black(0), 
        #     52: black(1), 
        #     53: black(2), 
        #     54: black(3), 
        #     55: red(0), 
        #     56: red(1), 
        #     57: red(2), 
        #     58: pistacchio(0), 
        #     59: pistacchio(1),
        #     60: yellow(0), 
        #     61: yellow(1), 
        #     62: yellow(2)
        # }
        self.all_property_cards = {
            35: brown,
            36: brown, 
            37: blue, 
            38: blue, 
            39: green, 
            40: green, 
            41: green, 
            42: lightblue, 
            43: lightblue, 
            44: lightblue, 
            45: orange, 
            46: orange, 
            47: orange, 
            48: purple, 
            49: purple,
            50: purple, 
            51: black, 
            52: black, 
            53: black, 
            54: black, 
            55: red, 
            56: red, 
            57: red, 
            58: pistacchio, 
            59: pistacchio,
            60: yellow, 
            61: yellow, 
            62: yellow
        }
        self.all_property_wild_cards = {
            63: bluegreen, 
            64: lightbluebrown, 
            65: rainbow, 
            66: rainbow, 
            67: orangepurple, 
            68: orangepurple, 
            69: greenblack,
            70: lightblueblack, 
            71: pistacchioblack, 
            72: redyellow, 
            73: redyellow
        }
        self.all_rent_cards = {
            74: rainbowrent,
            75: rainbowrent,
            76: rainbowrent, 
            77: bluegreenrent, 
            78: bluegreenrent, 
            79: lightbluebrownrent, 
            80: lightbluebrownrent,
            81: orangepurplerent, 
            82: orangepurplerent,
            83: pistacchioblackrent, 
            84: pistacchioblackrent,
            85: redyellowrent,
            86: redyellowrent
        }
        self.all_money = {
            87: cash10,
            88: cash1,
            89: cash1,
            90: cash1,
            91: cash1, 
            92: cash1, 
            93: cash1, 
            94: cash2, 
            95: cash2, 
            96: cash2, 
            97: cash2, 
            98: cash2, 
            99: cash3, 
            100: cash3, 
            101: cash3, 
            102: cash4, 
            103: cash4, 
            104: cash4,
            105: cash5,
            106: cash5
        }

    
    def start_game(self, no_of_players):
        for i in range(self.no_of_players):
            current_hand = self.hands[i]
            current_board = self.boards[i]
            move = input(int("What is your move?"))
            makeMove(current_player,move)
        # start someones turn
        # make a move
        # check for end condition
        # repeat up to two times
        # start next players turn

    def makeMove(self,current_player,move):
        if move in range(35):
            self.all_action_cards[move](current_player)
        else if move in range(35,63):
            self.all_property_cards[move](current_player)
        else if move in range(63,74):
            while 1:
                side = input(("Which color(brown,blue,green,lightblue,orange,purple,black,red,pistacchio,yellow):").lower())
                if side in ['brown','blue','green','lightblue','orange','purple','black','red','pistacchio','yellow']:
                    break
                else:
                    print("Please enter a valid option.")
            self.all_property_wild_cards[move](card_number,current_player)
        else if move in range(74,87):
            self.all_rent_cards[move]()
        else if move in range(87,107):
            self.all_money[move]()
