import numpy as np

# TODO: make draw card better - numpy choice from given indices
class Game:

    def __init__(self, no_of_players):
        self.no_of_players = no_of_players
        # make deck
        self.deck = np.ones((110,))
        # make cards down
        self.cards_down = np.zeros((110,))
        # init hands
        self.hands = np.zeros((self.no_of_players,110))
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
        # make player boards and give first five cards
        for i in range(self.no_of_players):
            self.boards.append(board)
            self.add_five_cards(i)
        
        self.all_action_cards = {
            0: self.deal_breaker,
            1: self.deal_breaker,
            2: self.debt_collector,
            3: self.debt_collector,
            4: self.debt_collector,
            5: self.double_rent,
            6: self.double_rent,
            7: self.forced_deal,
            8: self.forced_deal,
            9: self.forced_deal,
            10: self.hotel,
            11: self.hotel,
            12: self.hotel,
            13: self.house,
            14: self.house,
            15: self.house,
            16: self.say_no,
            17: self.say_no,
            18: self.say_no,
            19: self.birthday,
            20: self.birthday,
            21: self.birthday,
            22: self.pass_go,
            23: self.pass_go,
            24: self.pass_go,
            25: self.pass_go,
            26: self.pass_go,
            27: self.pass_go,
            28: self.pass_go,
            29: self.pass_go,
            30: self.pass_go,
            31: self.pass_go,
            32: self.sly_deal,
            33: self.sly_deal,
            34: self.sly_deal
        }
        self.all_property_cards = {
            35: self.brown,
            36: self.brown, 
            37: self.blue, 
            38: self.blue, 
            39: self.green, 
            40: self.green, 
            41: self.green, 
            42: self.lightblue, 
            43: self.lightblue, 
            44: self.lightblue, 
            45: self.orange, 
            46: self.orange, 
            47: self.orange, 
            48: self.purple, 
            49: self.purple,
            50: self.purple, 
            51: self.black, 
            52: self.black, 
            53: self.black, 
            54: self.black, 
            55: self.red, 
            56: self.red, 
            57: self.red, 
            58: self.pistacchio, 
            59: self.pistacchio,
            60: self.yellow, 
            61: self.yellow, 
            62: self.yellow
        }
        self.all_property_wild_cards = {
            63: self.bluegreen, 
            64: self.lightbluebrown, 
            65: self.rainbow, 
            66: self.rainbow, 
            67: self.orangepurple, 
            68: self.orangepurple, 
            69: self.greenblack,
            70: self.lightblueblack, 
            71: self.pistacchioblack, 
            72: self.redyellow, 
            73: self.redyellow
        }
        self.all_rent_cards = {
            74: self.rainbowrent,
            75: self.rainbowrent,
            76: self.rainbowrent, 
            77: self.bluegreenrent, 
            78: self.bluegreenrent, 
            79: self.lightbluebrownrent, 
            80: self.lightbluebrownrent,
            81: self.orangepurplerent, 
            82: self.orangepurplerent,
            83: self.pistacchioblackrent, 
            84: self.pistacchioblackrent,
            85: self.redyellowrent,
            86: self.redyellowrent
        }
        self.all_money = {
            87: self.cash10,
            88: self.cash1,
            89: self.cash1,
            90: self.cash1,
            91: self.cash1, 
            92: self.cash1, 
            93: self.cash1, 
            94: self.cash2, 
            95: self.cash2, 
            96: self.cash2, 
            97: self.cash2, 
            98: self.cash2, 
            99: self.cash3, 
            100: self.cash3, 
            101: self.cash3, 
            102: self.cash4, 
            103: self.cash4, 
            104: self.cash4,
            105: self.cash5,
            106: self.cash5
        }

    def add_five_cards(self,player):
        for i in range(5):
            self.add_card(player)

    def add_two_cards(self,player):
        self.add_card(player)
        self.add_card(player)

    def add_card(self,player):
        card_index = np.random.randint(107)
        current_hand = self.hands[player]
        while 1:
            if current_hand[card_index] == 0:
                current_hand[card_index] = 1
                break
            else:
                card_index = np.random.randint(107)
    
    def start_game(self):
        while 1:
            for i in range(self.no_of_players):
                move_counter = 0
                current_player = i
                current_hand = self.hands[i]
                current_board = self.boards[i]
                while move_counter < 3:
                    card_chosen = False
                    while not card_chosen:
                        card_index = int(input("What card will you use?"))
                        if card_index in current_hand and self.can_use(current_player,card_index):
                            self.make_move(current_player, card_index)
                            move_counter += 1
                            card_chosen = True
                        else:
                            print("Can't do, try again")
            # start someones turn
            # make a move using card_index
            # check for end condition
            # repeat up to two times
            # start next players turn
    
    def can_use(self,current_player,card_index):
        return 1

    def make_move(self,current_player,card_index):
        if card_index in range(35):
            self.all_action_cards[card_index](current_player)
        elif card_index in range(35,63):
            self.all_property_cards[card_index](current_player)
        elif card_index in range(63,74):
            while 1:
                side = input(("Which color(brown,blue,green,lightblue,orange,purple,black,red,pistacchio,yellow):").lower())
                if side in ['brown','blue','green','lightblue','orange','purple','black','red','pistacchio','yellow']:
                    break
                else:
                    print("Please enter a valid option.")
            self.all_property_wild_cards[card_index](card_index,current_player)
        elif card_index in range(74,87):
            self.all_rent_cards[card_index]()
        elif card_index in range(87,107):
            self.all_money[card_index]()
    
    def cash1(self, parameter_list):
        pass
    
    def cash2(self, parameter_list):
        pass

    def cash3(self, parameter_list):
        pass

    def cash4(self, parameter_list):
        pass
    
    def cash5(self, parameter_list):
        pass
    
    def cash10(self, parameter_list):
        pass

    def deal_breaker(self):
        pass
    
    def debt_collector(self, parameter_list):
        pass
    
    def double_rent(self, parameter_list):
        pass
    
    def forced_deal(self, parameter_list):
        pass
    
    def sly_deal(self, parameter_list):
        pass

    def hotel(self, parameter_list):
        pass
    
    def house(self, parameter_list):
        pass

    def say_no(self, parameter_list):
        pass

    def birthday(self, parameter_list):
        pass

    def pass_go(self, parameter_list):
        pass
    
    def brown(self, parameter_list):
        pass
    
    def green(self, parameter_list):
        pass

    def lightblue(self, parameter_list):
        pass

    def blue(self, parameter_list):
        pass

    def orange(self, parameter_list):
        pass

    def purple(self, parameter_list):
        pass

    def black(self, parameter_list):
        pass
    
    def red(self, parameter_list):
        pass

    def pistacchio(self, parameter_list):
        pass
    
    def yellow(self, parameter_list):
        pass

    def lightbluebrown(self, parameter_list):
        pass
    
    def rainbow(self, parameter_list):
        pass
    
    def orangepurple(self, parameter_list):
        pass
    
    def greenblack(self, parameter_list):
        pass
    
    def lightblueblack(self, parameter_list):
        pass

    def pistacchioblack(self, parameter_list):
        pass
    
    def redyellow(self, parameter_list):
        pass
    
    def bluegreen(self, parameter_list):
        pass
    
    def lightbluebrownrent(self, parameter_list):
        pass
    
    def rainbowrent(self, parameter_list):
        pass
    
    def orangepurplerent(self, parameter_list):
        pass
    
    def greenblackrent(self, parameter_list):
        pass
    
    def lightblueblackrent(self, parameter_list):
        pass

    def pistacchioblackrent(self, parameter_list):
        pass
    
    def redyellowrent(self, parameter_list):
        pass
    
    def bluegreenrent(self, parameter_list):
        pass