import numpy as np
import random


def giveCards(cards, toPlayer):
    for card in cards:
        hands[toPlayer][card] = True

def giveCardsTest():
    cards = ["dealbreaker1","green1","black3"]
    toPlayer = 0

    giveCards(cards, toPlayer)

    assert(all([hands[toPlayer][card] for card in cards]))

def drawFromDeck(amount, forPlayer):
    availableCards = [card for card, cardInDeck in deck.items() if cardInDeck]
    chosenCards = random.sample(availableCards, amount)
    for card in chosenCards:
        deck[card] = False
    giveCards(chosenCards, forPlayer)

def drawFromDeckFiveRandomCardsTest():
    player = 0
    for card in deck:
        deck[card] = False
    random5cards = random.sample(deck.keys(), 5)
    for card in random5cards:
        deck[card] = True
    
    drawFromDeck(5, player)

    assert(all(hands[player][card] for card in random5cards))
    assert(not(True in deck.values()))

def drawFromDeckAllCardsTest():
    player = 0
    for card in deck:
        deck[card] = True
    
    drawFromDeck(106, player)

    assert(all(hands[player].values()))
    assert(not(True in deck.values()))

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

def getPropertyAmount(player, color):
    # actually includes houses and hotels, but can't have them anyway if not complete
    return min(sum(boards[player][color].values()), colorToFullSetAmount[color])

def getPropertyAmountTest():
    player1 = 1
    player2 = 0
    boards[player1]["brown"]["brown1"] = 1
    boards[player1]["brown"]["brown2"] = 1
    boards[player1]["purple"]["purple1"] = 1
    boards[player1]["purple"]["purple2"] = 1
    boards[player1]["purple"]["rainbow2"] = 1
    boards[player2]["green"]["green1"] = 1
    boards[player2]["green"]["green2"] = 1
    boards[player2]["green"]["green3"] = 1
    boards[player2]["green"]["house"] = 1


    assert(getPropertyAmount(player1, "brown") == 2)
    assert(getPropertyAmount(player1, "purple") == 3)
    assert(getPropertyAmount(player2, "green") == 3)

    boards[player1]["brown"]["brown1"] = 0
    boards[player1]["brown"]["brown2"] = 0
    boards[player1]["purple"]["purple1"] = 0
    boards[player1]["purple"]["purple2"] = 0
    boards[player1]["purple"]["rainbow2"] = 0
    boards[player2]["green"]["green1"] = 0
    boards[player2]["green"]["green2"] = 0
    boards[player2]["green"]["green3"] = 0
    boards[player2]["green"]["house"] = 0

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
    def houseRentAdder(player, color):
        return (func(player, color) + 3) if boards[player][color]["house"] == 1 else func(player, color)
    return houseRentAdder

def addHotelRent(func):
    def hotelRentAdder(player, color):
        return (func(player, color) + 4) if boards[player][color]["hotel"] == 1 else func(player, color)
    return hotelRentAdder

@addHouseRent
@addHotelRent
def calculateRentForPlayer(player, color):
    return colorToRent[color][getPropertyAmount(player, color)-1]

def calculateRentForPlayerTest():
    player1 = 0
    player2 = 1
    boards[player1]["brown"]["brown1"] = 1
    boards[player1]["brown"]["lightbluebrown"] = 1
    boards[player1]["black"]["black1"] = 1
    boards[player1]["black"]["black2"] = 1
    boards[player1]["black"]["rainbow1"] = 1
    boards[player2]["green"]["green1"] = 1
    boards[player2]["green"]["green2"] = 1
    boards[player2]["green"]["green3"] = 1

    assert(calculateRentForPlayer(player1, "brown") == 2)
    assert(calculateRentForPlayer(player1, "black") == 3)
    assert(calculateRentForPlayer(player2, "green") == 7)

    boards[player1]["brown"]["brown1"] = 0
    boards[player1]["brown"]["lightbluebrown"] = 0
    boards[player1]["black"]["black1"] = 0
    boards[player1]["black"]["black2"] = 0
    boards[player1]["black"]["rainbow1"] = 0
    boards[player2]["green"]["green1"] = 0
    boards[player2]["green"]["green2"] = 0
    boards[player2]["green"]["green3"] = 0

def addHouseRentTest():
    player1 = 0
    player2 = 1
    boards[player1]["brown"]["brown1"] = 1
    boards[player1]["brown"]["lightbluebrown"] = 1
    boards[player1]["brown"]["house"] = 1
    boards[player2]["green"]["green1"] = 1
    boards[player2]["green"]["green2"] = 1
    boards[player2]["green"]["green3"] = 1
    boards[player2]["green"]["house"] = 1

    assert(calculateRentForPlayer(player1, "brown") == 5)
    assert(calculateRentForPlayer(player2, "green") == 10)

    boards[player1]["brown"]["brown1"] = 0
    boards[player1]["brown"]["lightbluebrown"] = 0
    boards[player1]["brown"]["house"] = 0
    boards[player2]["green"]["green1"] = 0
    boards[player2]["green"]["green2"] = 0
    boards[player2]["green"]["green3"] = 0
    boards[player2]["green"]["house"] = 0

def addHotelRentTest():
    player1 = 0
    player2 = 1
    boards[player1]["purple"]["purple1"] = 1
    boards[player1]["purple"]["purple2"] = 1
    boards[player1]["purple"]["rainbow2"] = 1
    boards[player1]["purple"]["house"] = 1
    boards[player1]["purple"]["hotel"] = 1
    boards[player2]["green"]["green1"] = 1
    boards[player2]["green"]["green2"] = 1
    boards[player2]["green"]["green3"] = 1
    boards[player2]["green"]["house"] = 1
    boards[player2]["green"]["hotel"] = 1

    assert(calculateRentForPlayer(player1, "purple") == 11)
    assert(calculateRentForPlayer(player2, "green") == 14)

    boards[player1]["purple"]["purple1"] = 0
    boards[player1]["purple"]["purple2"] = 0
    boards[player1]["purple"]["rainbow2"] = 0
    boards[player1]["purple"]["house"] = 0
    boards[player1]["purple"]["hotel"] = 0
    boards[player2]["green"]["green1"] = 0
    boards[player2]["green"]["green2"] = 0
    boards[player2]["green"]["green3"] = 0
    boards[player2]["green"]["house"] = 0
    boards[player2]["green"]["hotel"] = 0

def placeHouse(player, color):
    boards[player][color]["house"] = 1

def placeHouseTest():
    player = 1
    boards[player]["purple"]["purple1"] = 1
    boards[player]["purple"]["purple2"] = 1
    boards[player]["purple"]["rainbow2"] = 1

    placeHouse(player, "purple")

    assert(boards[player]["purple"]["house"])

    boards[player]["purple"]["purple1"] = 0
    boards[player]["purple"]["purple2"] = 0
    boards[player]["purple"]["rainbow2"] = 0

def placeHotel(player, color):
    boards[player][color]["hotel"] = 1

def placeHotelTest():
    player = 0
    boards[player]["orange"]["orange1"] = 1
    boards[player]["orange"]["orange3"] = 1
    boards[player]["orange"]["rainbow2"] = 1
    boards[player]["orange"]["hotel"] = 1
    
    placeHotel(player, "orange")
    
    assert(boards[player]["orange"]["hotel"])

    boards[player]["orange"]["orange1"] = 0
    boards[player]["orange"]["orange3"] = 0
    boards[player]["orange"]["rainbow2"] = 0
    boards[player]["orange"]["hotel"] = 0

def placeProperty(player, card, color):
    if card in ["rainbow1","rainbow2"] and not getPropertyAmount(player,color):
        return False
    
    boards[player][color][card] = 1
    return True

def placePropertyTest():
    player = 0

    placeProperty(player, "purple1", "purple")
    placeProperty(player, "rainbow1", "purple")
    placeProperty(player, "rainbow2", "purple")
    placeProperty(player, "blue1", "blue")
    placeProperty(player, "bluegreen", "blue")

    assert(boards[player]["purple"]["purple1"])
    assert(boards[player]["purple"]["rainbow1"])
    assert(boards[player]["purple"]["rainbow2"])
    assert(boards[player]["blue"]["blue1"])
    assert(boards[player]["blue"]["bluegreen"])

    boards[player]["purple"]["purple1"] = 0
    boards[player]["purple"]["rainbow1"] = 0
    boards[player]["purple"]["rainbow2"] = 0
    boards[player]["blue"]["blue1"] = 0
    boards[player]["blue"]["bluegreen"] = 0

noOfPlayers = 2

deck = {
    "dealbreaker1": True,
    "dealbreaker2": True,
    "debtcollector1": True,
    "debtcollector2": True,
    "debtcollector3": True,
    "doublerent1": True,
    "doublerent2": True,
    "forceddeal1": True,
    "forceddeal2": True,
    "forceddeal3": True,
    "placehouse1": True,
    "placehouse2": True,
    "placehouse3": True,
    "placehotel1": True,
    "placehotel2": True,
    "placehotel3": True,
    "sayno1": True,
    "sayno2": True,
    "sayno3": True,
    "birthday1": True,
    "birthday2": True,
    "birthday3": True,
    "passgo1": True,
    "passgo2": True,
    "passgo3": True,
    "passgo4": True,
    "passgo5": True,
    "passgo6": True,
    "passgo7": True,
    "passgo8": True,
    "passgo9": True,
    "passgo10": True,
    "slydeal1": True,
    "slydeal2": True,
    "slydeal3": True,
    "brown1": True,
    "brown2": True,
    "blue1": True,
    "blue2": True,
    "green1": True,
    "green2": True,
    "green3": True,
    "lightblue1": True,
    "lightblue2": True,
    "lightblue3": True,
    "orange1": True,
    "orange2": True,
    "orange3": True,
    "purple1": True,
    "purple2": True,
    "purple3": True,
    "black1": True,
    "black2": True,
    "black3": True,
    "black4": True,
    "red1": True,
    "red2": True,
    "red3": True,
    "pistacchio1": True,
    "pistacchio2": True,
    "yellow1": True,
    "yellow2": True,
    "yellow3": True,
    "rainbow1": True,
    "rainbow2": True,
    "bluegreen": True,
    "lightbluebrown": True, 
    "orangepurple1": True, 
    "orangepurple2": True, 
    "greenblack": True,
    "lightblueblack": True, 
    "pistacchioblack": True,
    "redyellow1": True,
    "redyellow2": True,
    "rainbowrent1": True,
    "rainbowrent2": True,
    "rainbowrent3": True,
    "bluegreenrent1": True,
    "bluegreenrent2": True,
    "lightbluebrownrent1": True,
    "lightbluebrownrent2": True,
    "orangepurplerent1": True, 
    "orangepurplerent2": True, 
    "pistacchioblackrent1": True, 
    "pistacchioblackrent2": True, 
    "redyellowrent1": True, 
    "redyellowrent2": True, 
    "10m": True, 
    "1m1": True, 
    "1m2": True, 
    "1m3": True, 
    "1m4": True, 
    "1m5": True, 
    "1m6": True, 
    "2m1": True, 
    "2m2": True, 
    "2m3": True, 
    "2m4": True, 
    "2m5": True, 
    "3m1": True, 
    "3m2": True, 
    "3m3": True, 
    "4m1": True, 
    "4m2": True, 
    "4m3": True, 
    "5m1": True, 
    "5m2": True
}

cardsDown = {
    "dealbreaker1": False,
    "dealbreaker2": False,
    "debtcollector1": False,
    "debtcollector2": False,
    "debtcollector3": False,
    "doublerent1": False,
    "doublerent2": False,
    "forceddeal1": False,
    "forceddeal2": False,
    "forceddeal3": False,
    "placehouse1": False,
    "placehouse2": False,
    "placehouse3": False,
    "placehotel1": False,
    "placehotel2": False,
    "placehotel3": False,
    "sayno1": False,
    "sayno2": False,
    "sayno3": False,
    "birthday1": False,
    "birthday2": False,
    "birthday3": False,
    "passgo1": False,
    "passgo2": False,
    "passgo3": False,
    "passgo4": False,
    "passgo5": False,
    "passgo6": False,
    "passgo7": False,
    "passgo8": False,
    "passgo9": False,
    "passgo10": False,
    "slydeal1": False,
    "slydeal2": False,
    "slydeal3": False,
    "brown1": False,
    "brown2": False,
    "blue1": False,
    "blue2": False,
    "green1": False,
    "green2": False,
    "green3": False,
    "lightblue1": False,
    "lightblue2": False,
    "lightblue3": False,
    "orange1": False,
    "orange2": False,
    "orange3": False,
    "purple1": False,
    "purple2": False,
    "purple3": False,
    "black1": False,
    "black2": False,
    "black3": False,
    "black4": False,
    "red1": False,
    "red2": False,
    "red3": False,
    "pistacchio1": False,
    "pistacchio2": False,
    "yellow1": False,
    "yellow2": False,
    "yellow3": False,
    "rainbow1": False,
    "rainbow2": False,
    "bluegreen": False,
    "lightbluebrown": False, 
    "orangepurple1": False, 
    "orangepurple2": False, 
    "greenblack": False,
    "lightblueblack": False, 
    "pistacchioblack": False,
    "redyellow1": False,
    "redyellow2": False,
    "rainbowrent1": False,
    "rainbowrent2": False,
    "rainbowrent3": False,
    "bluegreenrent1": False,
    "bluegreenrent2": False,
    "lightbluebrownrent1": False,
    "lightbluebrownrent2": False,
    "orangepurplerent1": False, 
    "orangepurplerent2": False, 
    "pistacchioblackrent1": False, 
    "pistacchioblackrent2": False, 
    "redyellowrent1": False, 
    "redyellowrent2": False, 
    "10m": False, 
    "1m1": False, 
    "1m2": False, 
    "1m3": False, 
    "1m4": False, 
    "1m5": False, 
    "1m6": False, 
    "2m1": False, 
    "2m2": False, 
    "2m3": False, 
    "2m4": False, 
    "2m5": False, 
    "3m1": False, 
    "3m2": False, 
    "3m3": False, 
    "4m1": False, 
    "4m2": False, 
    "4m3": False, 
    "5m1": False, 
    "5m2": False
}

hands =  []
board = {
    "brown": {
        "brown1": False, 
        "brown2": False,
        "lightbluebrown": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    },
    "blue": {
        "blue1": False, 
        "blue2": False,
        "bluegreen": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    },
    "green": {
        "green1": False, 
        "green2": False,
        "green3": False,
        "bluegreen": False,
        "greenblack": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    },
    "lightblue": {
        "lightblue1": False, 
        "lightblue2": False,
        "lightblue3": False,
        "lightbluebrown": False,
        "lightblueblack": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    },
    "orange": {
        "orange1": False, 
        "orange2": False,
        "orange3": False,
        "orangepurple1": False,
        "orangepurple2": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    },
    "purple": {
        "purple1": False, 
        "purple2": False,
        "purple3": False,
        "orangepurple1": False,
        "orangepurple2": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    },
    "black": {
        "black1": False, 
        "black2": False,
        "black3": False,
        "black4": False,
        "greenblack": False,
        "lightblueblack": False,
        "pistacchioblack": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    },
    "red": {
        "red1": False, 
        "red2": False,
        "red3": False,
        "redyellow1": False,
        "redyellow2": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    },
    "pistacchio": {
        "pistacchio1": False, 
        "pistacchio2": False,
        "pistacchioblack": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    },
    "yellow": {
        "yellow1": False, 
        "yellow2": False,
        "yellow3": False,
        "redyellow1": False,
        "redyellow2": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    }
}
boards = []
sets = []
# make player boards and give first five cardIndices to all players
for player in range(noOfPlayers):
    sets.append({})
    hands.append(dict(cardsDown))
    boards.append(dict(board))
    drawFromDeck(5, player)

# RUN TESTS
giveCardsTest()
drawFromDeckFiveRandomCardsTest()
getPropertyAmountTest()
calculateRentForPlayerTest()
addHouseRentTest()
addHotelRentTest()
placeHouseTest()
placeHotelTest()
placePropertyTest()