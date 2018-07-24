import numpy as np
import random

# TESTED
def drawFromDeck(amount, forPlayer):
    availableCards = [card for card, cardInDeck in deck.items() if cardInDeck]
    chosenCards = random.sample(availableCards, amount)
    for card in chosenCards:
        deck[card] = False
    giveCards(chosenCards, forPlayer)

# TESTED
def giveCards(cards, toPlayer):
    for card in cards:
        hands[toPlayer][card] = True

# TESTED
def addHouseRent(func):
    def houseRentAdder(player, color):
        return (func(player, color) + 3) if boards[player][color]["house"] else func(player, color)
    return houseRentAdder

# TESTED
def addHotelRent(func):
    def hotelRentAdder(player, color):
        return (func(player, color) + 4) if boards[player][color]["hotel"] else func(player, color)
    return hotelRentAdder

# TESTED
@addHouseRent
@addHotelRent
def calculateRentForPlayer(player, color):
    return colorToRent[color][getPropertyAmount(player, color)-1]

# TESTED
def getPropertyAmount(player, color):
    # actually includes houses and hotels, but can't have them anyway if not complete
    return min(sum(boards[player][color].values()), colorToFullSetAmount[color])

# TOTEST
def placeHouse(player, color, card):
    boards[player][color]["house"] = card
    boards[player][sets][color].append(card)

# TOTEST
def placeHotel(player, color, card):
    boards[player][color]["hotel"] = card
    boards[player][sets][color].append(card)

# TOTEST
def placeProperty(player, card, color):
    if card in ["rainbow1","rainbow2"] and not getPropertyAmount(player,color):
        return False
    
    boards[player][color][card] = 1
    makeSet(player, color)
    return True

# TOTEST
def passGo(player):
    drawFromDeck(2, player)

# TOTEST
def removeProperty(player, card, color):
    boards[player][color][card] = 0

# TOTEST
def makeSets(player):
    for color in ['brown','blue','green','lightblue','orange','purple','black','red','yellow','pistacchio']:
        makeSet(player, color)

# TOTEST
def makeSet(player, setColor):
    playerSets = sets[player]
    setAmount = 0
    props = set()
    for card, exists in boards[player][setColor]:
        if exists and card not in ["house","hotel"]:
            props.add(card)
        elif exists:
            props.add(exists)
    if setColor + "1" in playerSets:
        setAmount += 1
        props -= set(playerSets[setColor + "1"])
    if setColor + "2" in playerSets:
        setAmount += 1
        props -= set(playerSets[setColor + "2"])
    if len(props) == colorToFullSetAmount[setColor]:
        playerSets[setColor + str(setAmount+1)] = list(props)

# TOTEST
def dealBreaker(fromPlayer, toPlayer, setKey):
    cardsInSet = sets[fromPlayer][setKey]
    color = setKey[:-1]
    for card in cardsInSet:
        boards[fromPlayer][color][card] = 0
        boards[toPlayer][color][card] = 1
        sets[toPlayer][color + "1" if color + "1" not in sets[toPlayer] else color + "2"]

# TOTEST
def debtCollector(fromPlayer, currentPlayer):
    askAmount(fromPlayer, currentPlayer, 5)

def doubleRent():
    pass

# TOTEST
def forcedDeal(currentPlayer, otherPlayer, ownCard, otherCard, ownColor, otherColor):
    removeProperty(otherPlayer, otherCard, otherColor)
    removeProperty(currentPlayer, ownCard, ownColor)
    placeProperty(otherPlayer, ownCard, ownColor)
    placeProperty(currentPlayer, otherCard, otherColor)

#TOTEST
def slyDeal(currentPlayer, otherPlayer, card, color):
    removeProperty(otherPlayer, card, color)
    placeProperty(currentPlayer, card, color)

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

def getPropsForPlayer(player):
    allCards = []
    houseAmount = 0
    hotelAmount = 0
    for color in ['brown','blue','green','lightblue','orange','purple','black','red','yellow','pistacchio']:
        allCards.extend([card for card, exists in boards[player][color] if exists])
        if "house" in allCards:
            houseAmount += 1
            allCards -= "house"
            allCards += "house" + str(houseAmount)
        if "hotel" in allCards:
            hotelAmount += 1
            allCards -= "hotel"
            allCards += "hotel" + str(hotelAmount)

def getCashForPlayer(player):
    return [card for card, exists in boards[player]["money"] if exists]

def payOptions(player, amount):
    options = []
    payables = {}
    for card in getCashForPlayer(player):
        payables[card] = cardToValue[card] 
    for card in getPropsForPlayer(player):
        if card not in ["rainbow1","rainbow2"]:
            payables[card] = cardToValue[card]  
    genPayOptions(options, {}, payables, amount)
    if not options:
        options = payables.keys()
    return options

def genPayOptions(options, currentItems, itemsLeft, amount):
    if sum(currentItems.values()) >= amount:
        options.append(currentItems)
        return

    if not itemsLeft:
        return
    
    item, value = itemsLeft.popitem()
    genPayOptions(options, currentItems, itemsLeft, amount)
    currentItemsPlus = dict(currentItems)
    currentItemsPlus[item] = value
    genPayOptions(options, currentItemsPlus, itemsLeft, amount)

def playerWin(player):
    playerSets = boards[player][sets]
    nonDuplicateSets = []
    for color in playerSets.keys():
        if color[:-1] not in nonDuplicateSets:
            nonDuplicateSets.append(color)
    return True if len(nonDuplicateSets) >= 3 else False

# amount of players
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
    },
    "money":{
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
}
boards = []
sets = []
# make player boards and give first five cardIndices to all players
for player in range(noOfPlayers):
    sets.append({})
    hands.append(dict(cardsDown))
    boards.append(dict(board))
    drawFromDeck(5, player)

gameOver = False
while not gameOver:
    cycle = 0
    player = cycle % noOfPlayers
    moves = 0
    while moves <3:
        if not moves:
            waitForMove(player)
        else:
            if wantToMove(player):
                waitForMove(player)
        if playerWin:
            gameOver = True
            break
        moves += 1

def waitForMove(player):
    pass

def wantToMove(player):
    pass

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

# card value
cardToValue = {
    "dealbreaker1": 5,
    "dealbreaker2": 5,
    "debtcollector1": 3,
    "debtcollector2": 3,
    "debtcollector3": 3,
    "doublerent1": 1,
    "doublerent2": 1,
    "forceddeal1": 3,
    "forceddeal2": 3,
    "forceddeal3": 3,
    "placehouse1": 4,
    "placehouse2": 4,
    "placehouse3": 4,
    "placehotel1": 3,
    "placehotel2": 3,
    "placehotel3": 3,
    "sayno1": 4,
    "sayno2": 4,
    "sayno3": 4,
    "birthday1": 2,
    "birthday2": 2,
    "birthday3": 2,
    "passgo1": 1,
    "passgo2": 1,
    "passgo3": 1,
    "passgo4": 1,
    "passgo5": 1,
    "passgo6": 1,
    "passgo7": 1,
    "passgo8": 1,
    "passgo9": 1,
    "passgo10": 1,
    "slydeal1": 3,
    "slydeal2": 3,
    "slydeal3": 3,
    "brown1": 1,
    "brown2": 1,
    "blue1": 4,
    "blue2": 4,
    "green1": 4,
    "green2": 4,
    "green3": 4,
    "lightblue1": 1,
    "lightblue2": 1,
    "lightblue3": 1,
    "orange1": 2,
    "orange2": 2,
    "orange3": 2,
    "purple1": 2,
    "purple2": 2,
    "purple3": 2,
    "black1": 2,
    "black2": 2,
    "black3": 2,
    "black4": 2,
    "red1": 3,
    "red2": 3,
    "red3": 3,
    "pistacchio1": 2,
    "pistacchio2": 2,
    "yellow1": 3,
    "yellow2": 3,
    "yellow3": 3,
    "rainbow1": 0,
    "rainbow2": 0,
    "bluegreen": 4,
    "lightbluebrown": 1,
    "orangepurple1": 2,
    "orangepurple2": 2,
    "greenblack": 4,
    "lightblueblack": 4,
    "pistacchioblack": 2,
    "redyellow1": 3,
    "redyellow2": 3,
    "rainbowrent1": 3,
    "rainbowrent2": 3,
    "rainbowrent3": 3,
    "bluegreenrent1": 1,
    "bluegreenrent2": 1,
    "lightbluebrownrent1": 1,
    "lightbluebrownrent2": 1,
    "orangepurplerent1": 1,
    "orangepurplerent2": 1,
    "pistacchioblackrent1": 1,
    "pistacchioblackrent2": 1,
    "redyellowrent1": 1,
    "redyellowrent2": 1,
    "10m": 10,
    "1m1": 1,
    "1m2": 1,
    "1m3": 1,
    "1m4": 1,
    "1m5": 1,
    "1m6": 1,
    "2m1": 2,
    "2m2": 2,
    "2m3": 2,
    "2m4": 2,
    "2m5": 2,
    "3m1": 3,
    "3m2": 3,
    "3m3": 3,
    "4m1": 4,
    "4m2": 4,
    "4m3": 4,
    "5m1": 5,
    "5m2": 5
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

