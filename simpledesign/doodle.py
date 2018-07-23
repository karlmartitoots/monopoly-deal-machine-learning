import numpy as np
from monopolydeal import giveCards

hands = np.zeros((2, 106))
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
for player in range(2):
    sets.append({})
    boards.append(board)


# more readable representation of players board
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
        "orangepurple": False,
        "orangepurple": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    },
    "purple": {
        "purple1": False, 
        "purple2": False,
        "purple3": False,
        "orangepurple": False,
        "orangepurple": False,
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
        "redyellow": False,
        "redyellow": False,
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
        "redyellow": False,
        "redyellow": False,
        "rainbow1": False,
        "rainbow2": False,
        "house": False,
        "hotel": False
    }
}

# more readable representation of sets
# sets = {
#     "blue1": ["blue1", "bluegreen"],
#     "pistacchio1": ["pistacchioblack", "rainbow2"],
#     "pistacchio2": ["pistacchio", "rainbow1"]
# }

sets[0]["brown1"] = [0,2]
sets[0]["brown2"] = [1,3]
boards[0][0][[0,1,2,3]] = 1
# def makeSets(playerIndex):
#     playerSets = sets[playerIndex]
#     for setIndex in range(10):
#         setColor = setIndexToColor[setIndex]
#         if isFullSet(playerIndex, setColor) :
#             currentSet = sets[playerIndex][setColor]
#             currentSet.append(np.where(boards[playerIndex][setIndex] == 1))

print(list(set(np.where(boards[0][0] == 1)[0])-set(sets[0]["brown1"])))