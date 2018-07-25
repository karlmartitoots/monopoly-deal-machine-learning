import numpy as np
import random

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

x = np.ones((106,))

x[np.random.choice(106, size = 50, replace = False)] = 0

print(np.where(x)[0])