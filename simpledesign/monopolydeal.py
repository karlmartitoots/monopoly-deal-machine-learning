import numpy as np

# TESTED
def drawFromDeck(amount, forPlayer):
    # old one: cardIndices = np.random.choice([index for index, exists in zip(np.arange(106),deck) if exists], amount, replace=False)
    cardIndices = np.random.choice(np.where(deck == 1)[0], amount, replace=False)
    deck[cardIndices] = 0
    giveCards(cardIndices, forPlayer)

# TESTED
def giveCards(cardIndices, toPlayer):
    hands[toPlayer][cardIndices] = 1

# TESTED
def addHouseRent(func):
    def houseRentAdder(currentPlayer, propertyColor):
        return (func(currentPlayer, propertyColor) + 3) if boards[currentPlayer][colorToSetIndex[propertyColor]][-2] == 1 else func(currentPlayer, propertyColor)
    return houseRentAdder

# TESTED
def addHotelRent(func):
    def hotelRentAdder(currentPlayer, propertyColor):
        return (func(currentPlayer, propertyColor) + 4) if boards[currentPlayer][colorToSetIndex[propertyColor]][-1] == 1 else func(currentPlayer, propertyColor)
    return hotelRentAdder

# TESTED
@addHouseRent
@addHotelRent
def calculateRentForPlayer(currentPlayer, propertyColor):
    return colorToRent[propertyColor][getPropertyAmount(currentPlayer, propertyColor)-1]

# TESTED
def getPropertyAmount(currentPlayer, propertyColor):
    # actually includes houses and hotels, but can't have them anyway if not complete
    return min(np.sum(boards[currentPlayer][colorToSetIndex[propertyColor]] == 1), colorToFullSetAmount[propertyColor])


# amount of players
noOfPlayers = 2
#noOfPlayers = int(input("Insert amount of players:"))

# init deck
deck = np.ones((106,))

# init cardIndices down
cardsDown = np.zeros((106,))

# init hands
hands = np.zeros((noOfPlayers, 106))
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
# make player boards and give first five cardIndices to all players
for player in range(noOfPlayers):
    boards.append(board)
    drawFromDeck(5, player)

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

def start_game(self):
    while 1:
        for player in range(self.no_of_players):
            move_counter = 0
            current_player = player
            current_hand = self.hands[player]
            current_board = self.boards[player]
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

def deal_breaker(self):
    pass

def debt_collector(self, parameter_list):
    pass

def double_rent(self, parameter_list):
    pass

def forced_deal(currentPlayer):
    pass

def sly_deal(self, parameter_list):
    pass

def hotel(self, parameter_list):
    pass

def house(self, parameter_list):
    pass

# TODO
def say_no(currentPlayer):
    pass

# TOTEST 
# after askAmount is finished
def birthday(currentPlayer):
    for player in range(noOfPlayers):
        if player != currentPlayer:
            askAmount(player, currentPlayer, 2)
    # askOthers 2m

# TODO:
# say no option
# all different paying options
def askAmount(fromPlayer, toPlayer, amount):
    pass

# TOTEST
def passGo(currentPlayer):
    drawFromDeck(2, currentPlayer)

# TOTEST
def drawFromDeck(amount, forPlayer):
    #cardIndices = np.random.choice([index for index, exists in zip(np.arange(106),deck) if exists], amount, replace=False)
    cardIndices = np.random.choice(np.where(deck == 1), amount, replace=False)
    deck[cardIndices] = 0.0
    giveCards(cardIndices, toPlayer)

# TOTEST
def giveCards(cardIndices, toPlayer):
    hands[toPlayer][cardIndices] = 1.0

# set index in a players board array
colorToSetIndex = {
    "brown": 0,
    "blue": 1,
    "green": 2,
    "lightblue": 3,
    "orange": 4,
    "purple": 5,
    "black": 6,
    "red": 7,
    "pistacchio": 8,
    "yellow": 9
}

# amount of properties in full set
colorToFullSetAmount = {
    "brown": 2,
    "blue": 2,
    "green": 3,
    "lightblue": 3,
    "orange": 3,
    "purple": 3,
    "black": 4,
    "red": 3,
    "pistacchio": 2,
    "yellow": 3
}

# amount of jokers in existance
colorToJokers = {
    "brown": 1,
    "blue": 1,
    "green": 2,
    "lightblue": 2,
    "orange": 2,
    "purple": 2,
    "black": 3,
    "red": 2,
    "pistacchio": 1,
    "yellow": 2
}

# property color
cardIndexToColor = {
    11: "brown",
    12: "brown",
    13: "blue",
    14: "blue",
    15: "green",
    16: "green",
    17: "green",
    18: "lightblue",
    19: "lightblue",
    20: "lightblue",
    21: "orange",
    22: "orange",
    23: "orange",
    24: "purple",
    25: "purple",
    26: "purple",
    27: "black",
    28: "black",
    29: "black",
    30: "black",
    31: "red",
    32: "red",
    33: "red",
    34: "pistacchio",
    35: "pistacchio",
    36: "yellow",
    37: "yellow",
    38: "yellow"
}

# card value
cardIndexToValue = {
    0: 5,
    1: 5,
    2: 3,
    3: 3,
    4: 3,
    5: 1,
    6: 1,
    7: 3,
    8: 3,
    9: 3,
    10: 4,
    11: 4,
    12: 4,
    13: 3,
    14: 3,
    15: 3,
    16: 4,
    17: 4,
    18: 4,
    19: 2,
    20: 2,
    21: 2,
    22: 1,
    23: 1,
    24: 1,
    25: 1,
    26: 1,
    27: 1,
    28: 1,
    29: 1,
    30: 1,
    31: 1,
    32: 3,
    33: 3,
    34: 3,
    35: 1,
    36: 1, 
    37: 4, 
    38: 4, 
    39: 4, 
    40: 4, 
    41: 4, 
    42: 1, 
    43: 1, 
    44: 1, 
    45: 2, 
    46: 2, 
    47: 2, 
    48: 2, 
    49: 2,
    50: 2, 
    51: 2, 
    52: 2, 
    53: 2, 
    54: 2, 
    55: 3, 
    56: 3, 
    57: 3, 
    58: 2, 
    59: 2,
    60: 3, 
    61: 3, 
    62: 3,
    63: 4, 
    64: 1, 
    65: 0, 
    66: 0, 
    67: 2, 
    68: 2, 
    69: 4,
    70: 4, 
    71: 2, 
    72: 3, 
    73: 3,
    74: 3,
    75: 3,
    76: 3, 
    77: 1, 
    78: 1, 
    79: 1, 
    80: 1,
    81: 1, 
    82: 1,
    83: 1, 
    84: 1,
    85: 1,
    86: 1,
    87: 10,
    88: 1,
    89: 1,
    90: 1,
    91: 1, 
    92: 1, 
    93: 1, 
    94: 2, 
    95: 2, 
    96: 2, 
    97: 2, 
    98: 2, 
    99: 3, 
    100: 3, 
    101: 3, 
    102: 4, 
    103: 4, 
    104: 4,
    105: 5,
    106: 5
}

# index - property amount, value - rent amount
colorToRent = {
    "brown": (1,2),
    "blue": (3,8),
    "green": (2,4,7),
    "lightblue": (1,2,3),
    "orange": (1,3,5),
    "purple": (1,2,4),
    "black": (1,2,3,4),
    "red": (2,3,6),
    "pistacchio": (1,2),
    "yellow": (2,4,6)
}

# TOTEST
def placeHouse(currentPlayer, propertyColor):
    boards[currentPlayer][colorToSetIndex[propertyColor]][-2]

# TOTEST
def placeHotel(currentPlayer, propertyColor):
    boards[currentPlayer][colorToSetIndex[propertyColor]][-1]

# TODO
def placeProperty(currentPlayer, propertyIndex):
    boards[currentPlayer][colorToSetIndex[propertyColor]][-1]

# TOTEST
def calculateRentForPlayer(currentPlayer, propertyColor):
    return colorToRent[color][getPropertyAmount(currentPlayer, propertyColor)-1]

# TOTEST
def getPropertyAmount(currentPlayer, propertyColor):
    # actually includes houses and hotels, but can't have them anyway if not complete
    return min(np.sum(boards[currentPlayer][colorToSetIndex[propertyColor]] == 1), colorToFullSetAmount[propertyColor])
