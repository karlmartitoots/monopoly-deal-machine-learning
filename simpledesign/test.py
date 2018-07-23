import numpy as np


def giveCards(cardIndices, toPlayer):
    hands[toPlayer][cardIndices] = 1

def giveCardsTest():
    cardIndices = [0,2,59,38,105,3]
    toPlayer = 0

    giveCards(cardIndices,toPlayer)

    assert(all(hands[toPlayer][[0,2,3,38,59,105]]))

def drawFromDeck(amount, forPlayer):
    # old one: cardIndices = np.random.choice([index for index, exists in zip(np.arange(106),deck) if exists], amount, replace=False)
    cardIndices = np.random.choice(np.where(deck == 1)[0], amount, replace=False)
    deck[cardIndices] = 0
    giveCards(cardIndices, forPlayer)

def drawFromDeckOneCardTest():
    player = 0
    deck[1] = 1
    
    drawFromDeck(1, player)

    assert(hands[player][1] == 1)
    assert(not(1 in deck))

def drawFromDeckAllCardsTest():
    player = 0
    deck[:] = 1
    
    drawFromDeck(106, player)

    assert(all(hands[player]))
    assert(not(1 in deck))

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

def getPropertyAmount(currentPlayer, propertyColor):
    # actually includes houses and hotels, but can't have them anyway if not complete
    return min(np.sum(boards[currentPlayer][colorToSetIndex[propertyColor]] == 1), colorToFullSetAmount[propertyColor])

def getPropertyAmountTest():
    player1 = 1
    player2 = 0
    boards[player1][0][0:2] = 1 # 2 browns
    boards[player1][5][[1,-3]] = 1 # 2 purples with rainbow wild card
    boards[player2][2][[0,1,2,-1]] = 1 # 3 greens + house

    assert(getPropertyAmount(player1, "brown") == 2)
    assert(getPropertyAmount(player1, "purple") == 2)
    assert(getPropertyAmount(player2, "green") == 3)

    boards[player1][0][0:2] = 0
    boards[player1][5][[1,-3]] = 0
    boards[player2][2][[0,1,2,-1]] = 0

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

def addHouseRent(func):
    def houseRentAdder(currentPlayer, propertyColor):
        return (func(currentPlayer, propertyColor) + 3) if boards[currentPlayer][colorToSetIndex[propertyColor]][-2] == 1 else func(currentPlayer, propertyColor)
    return houseRentAdder

def addHotelRent(func):
    def hotelRentAdder(currentPlayer, propertyColor):
        return (func(currentPlayer, propertyColor) + 4) if boards[currentPlayer][colorToSetIndex[propertyColor]][-1] == 1 else func(currentPlayer, propertyColor)
    return hotelRentAdder

@addHouseRent
@addHotelRent
def calculateRentForPlayer(currentPlayer, propertyColor):
    return colorToRent[propertyColor][getPropertyAmount(currentPlayer, propertyColor)-1]

def calculateRentForPlayerTest():
    player1 = 0
    player2 = 1
    boards[player1][0][[0,2]] = 1 # 2 browns
    boards[player1][6][[0,1,-3]] = 1 # 3 blacks with rainbow wild card
    boards[player2][2][[0,1,2]] = 1 # 3 greens

    assert(calculateRentForPlayer(player1, "brown") == 2)
    assert(calculateRentForPlayer(player1, "black") == 3)
    assert(calculateRentForPlayer(player2, "green") == 7)

    boards[player1][0][[0,2]] = 0
    boards[player1][6][[0,1,-3]] = 0
    boards[player2][2][[0,1,2]] = 0

def addHouseRentTest():
    player1 = 0
    player2 = 1
    boards[player1][0][[0,2,-2]] = 1 # 2 browns + house
    boards[player2][2][[0,1,2,-2]] = 1 # 3 greens + house

    assert(calculateRentForPlayer(player1, "brown") == 5)
    assert(calculateRentForPlayer(player2, "green") == 10)

    boards[player1][0][[0,2,-2]] = 0
    boards[player2][2][[0,1,2,-2]] = 0

def addHotelRentTest():
    player1 = 0
    player2 = 1
    boards[player1][5][[0,1,-3,-2,-1]] = 1 # 3 purples + house + hotel
    boards[player2][2][[0,1,2,-2,-1]] = 1 # 3 greens + house + hotel

    assert(calculateRentForPlayer(player1, "purple") == 11)
    assert(calculateRentForPlayer(player2, "green") == 14)

    boards[player1][5][[0,1,-3,-2,-1]] = 0
    boards[player2][2][[0,1,2,-2,-1]] = 0

def placeHouse(currentPlayer, propertyColor):
    boards[currentPlayer][colorToSetIndex[propertyColor]][-2] = 1

def placeHouseTest():
    player = 1
    boards[player][5][[0,1,-3]] = 1

    placeHouse(player, "purple")

    assert(boards[player][5][-2] == 1)

    boards[player][5][[0,1,-3,-2]] = 0

def placeHotel(currentPlayer, propertyColor):
    boards[currentPlayer][colorToSetIndex[propertyColor]][-1] = 1

def placeHotelTest():
    player = 0
    boards[player][4][[0,2,-3,-2]] = 1
    
    placeHotel(player, "orange")
    
    assert(boards[player][4][-1] == 1)

    boards[player][4][[0,2,-3,-1]] = 0

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

def placeProperty(currentPlayer, cardIndex, propertyColor):
    # TODO: have to check if player has property in case of rainbow wildcard
    target = boards[currentPlayer][colorToSetIndex[propertyColor]]
    if cardIndex in range(65,74):
        target[cardToJoker[cardIndex][propertyColor]] = 1
    else:
        target[cardToProperty[cardIndex]] = 1

def placePropertyTest():
    player = 0
    purpleCard = 45
    rainbowCard1 = 63
    rainbowCard2 = 64
    blueCard = 37
    bluegreenJokerCard = 65

    placeProperty(player, purpleCard, "purple")
    placeProperty(player, rainbowCard1, "purple")
    placeProperty(player, rainbowCard2, "purple")
    placeProperty(player, blueCard, "blue")
    placeProperty(player, bluegreenJokerCard, "blue")

    assert(boards[player][5][0] == 1)
    assert(boards[player][5][-3] == 1)
    assert(boards[player][5][-4] == 1)
    assert(boards[player][1][0] == 1)
    assert(boards[player][1][2] == 1)

    boards[player][5][0] = 1
    boards[player][5][-3] = 1
    boards[player][5][-4] = 1
    boards[player][1][0] = 1
    boards[player][1][2] = 1


hands = np.zeros((2, 106))
deck = np.zeros((106,))
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
for player in range(2):
    boards.append(board)

# RUN TESTS
giveCardsTest()
drawFromDeckOneCardTest()
getPropertyAmountTest()
calculateRentForPlayerTest()
addHouseRentTest()
addHotelRentTest()
placeHouseTest()
placeHotelTest()
placePropertyTest()