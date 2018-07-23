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

# TESTED
def placeHouse(currentPlayer, propertyColor):
    boards[currentPlayer][colorToSetIndex[propertyColor]][-2] = 1
    return True

# TESTED
def placeHotel(currentPlayer, propertyColor):
    boards[currentPlayer][colorToSetIndex[propertyColor]][-1] = 1
    return True

# TESTED
def placeProperty(currentPlayer, cardIndex, propertyColor):
    # TODO: have to check if player has property in case of rainbow wildcard
    target = boards[currentPlayer][colorToSetIndex[propertyColor]]
    if cardIndex in range(65,74):
        target[cardToJoker[cardIndex][propertyColor]] = 1
    else:
        target[cardToProperty[cardIndex]] = 1
    return True

# TOTEST
def removeProperty(fromPlayer, cardIndex, propertyColor):
    target = boards[fromPlayer][colorToSetIndex[propertyColor]]
    if cardIndex in range(65,74):
        target[cardToJoker[cardIndex][propertyColor]] = 0
    else:
        target[cardToProperty[cardIndex]] = 0

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
sets = []
# make player boards and give first five cardIndices to all players
for player in range(noOfPlayers):
    sets.append({})
    boards.append(board)
    drawFromDeck(5, player)

def dealBreaker():
    # problem - set implementation doesnt allow dealbreakers
    pass

def debtCollector(fromPlayer, currentPlayer):
    askAmount(fromPlayer, currentPlayer, 5)

def doubleRent():
    pass

# TOTEST
def forcedDeal(currentPlayer, otherPlayer, ownCardIndex, otherCardIndex, ownColor, otherColor):
    removeProperty(otherPlayer, otherCardIndex, otherColor)
    removeProperty(currentPlayer, ownCardIndex, ownColor)
    placeProperty(otherPlayer, ownCardIndex, ownColor)
    placeProperty(currentPlayer, otherCardIndex, otherColor)

#TOTEST
def slyDeal(currentPlayer, otherPlayer, cardIndex, color):
    removeProperty(otherPlayer, cardIndex, color)
    placeProperty(currentPlayer, cardIndex, color)

# TODO
def sayNo(currentPlayer):
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



all_action_cards = {
     0: dealBreaker,
     1: dealBreaker,
     2: debtCollector,
     3: debtCollector,
     4: debtCollector,
     5: doubleRent,
     6: doubleRent,
     7: forcedDeal,
     8: forcedDeal,
     9: forcedDeal,
    10: placeHouse,
    11: placeHouse,
    12: placeHouse,
    13: placeHotel,
    14: placeHotel,
    15: placeHotel,
    16: sayNo,
    17: sayNo,
    18: sayNo,
    19: birthday,
    20: birthday,
    21: birthday,
    22: passGo,
    23: passGo,
    24: passGo,
    25: passGo,
    26: passGo,
    27: passGo,
    28: passGo,
    29: passGo,
    30: passGo,
    31: passGo,
    32: slyDeal,
    33: slyDeal,
    34: slyDeal
}


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

setIndexToColor = dict((reversed(item) for item in colorToSetIndex.items()))

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

# property propertyColor
cardIndexToColor = {
    35: "brown",
    36: "brown",
    37: "blue",
    38: "blue",
    39: "green",
    40: "green",
    41: "green",
    42: "lightblue",
    43: "lightblue",
    44: "lightblue",
    45: "orange",
    46: "orange",
    47: "orange",
    48: "purple",
    49: "purple",
    50: "purple",
    51: "black",
    52: "black",
    53: "black",
    54: "black",
    55: "red",
    56: "red",
    57: "red",
    58: "pistacchio",
    59: "pistacchio",
    60: "yellow",
    61: "yellow",
    62: "yellow"
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
    63: 0, 
    64: 0, 
    65: 4, 
    66: 1, 
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

#first index - card index, second index - chosen color, value - joker index
cardToJoker = {
    65: {
        "blue": 2,
        "green": 3
    },
    66: {
        "brown": 2,
        "lightblue": 3
    }, 
    67: {"orange": 3,
        "purple": 3
    }, 
    68: {"orange": 4,
        "purple": 4
    }, 
    69: {"green": 4,
        "black": 4
    },
    70: {
        "lightblue": 4,
        "black": 5
    }, 
    71: {
        "pistacchio": 2,
        "black": 6
    }, 
    72: {
        "red": 3,
        "yellow": 3
    },
    73: {
        "red": 4,
        "yellow": 4
    }
}

# index - card index, value - index in a property set
cardToProperty = {
    35: 0,
    36: 1,
    37: 0,
    38: 1,
    39: 0,
    40: 1,
    41: 2,
    42: 0,
    43: 1,
    44: 2,
    45: 0,
    46: 1,
    47: 2,
    48: 0,
    49: 1,
    50: 2,
    51: 0,
    52: 1,
    53: 2,
    54: 3,
    55: 0,
    56: 1,
    57: 2,
    58: 0,
    59: 1,
    60: 0,
    61: 1,
    62: 2,
    63: -3,
    64: -4
}

# TOTEST
def makeSets(playerIndex):
    for setIndex in range(10):
        makeSet(playerIndex, setIndexToColor[setIndex])

# TOTEST
def makeSet(playerIndex, setColor):
    playerSets = sets[playerIndex]
    setAmount = 0
    props = set(np.where(boards[playerIndex][colorToSetIndex[setColor]] == 1))
    if setColor + "1" in playerSets:
        setAmount += 1
        props -= set(playerSets[setColor + "1"])
    if setColor + "2" in playerSets:
        setAmount += 1
        props -= set(playerSets[setColor + "2"])
    if len(props) == colorToFullSetAmount[setColor]:
        playerSets[setColor + str(setAmount+1)] = list(props)
